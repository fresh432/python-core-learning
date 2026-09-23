# LeetCode 460 LFU 缓存

## 我的思路（150分钟）
- 前30分钟：想到桶计数法——维护一个频率桶哈希表，cnts[freq] 用双向队列存对应频率的所有 key。get/put 时操作围绕计数桶进行，但这个方法删除最小频率元素时需要从频率1开始往上遍历找非空桶，做不到严格的 O(1)
- 中间20分钟：看提示说可以用链表，但想了20分钟完全没思路
- 后10分钟：先在纸上用桶计数法写流程，感觉可行
- 后40分钟：实现桶计数法，调试通过（176ms）
- 后30分钟：看双向链表法的题解，发现核心也是"频率桶"，但每个频率桶内不是队列而是双向链表（带哨兵头尾节点），同时维护 min_freq 来 O(1) 定位最小频率桶
- 后20分钟：边看答案边写，用双向链表法实现了一遍（164ms）

## 代码（双向队列法）
```python
from collections import deque, defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}      # key -> [value, freq]
        self.cnts = {}       # freq -> deque of keys
        self.cnts[1] = deque()
        self.count = 0       # 当前元素个数
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        e = self.cache[key]
        self.move(key, e[1])
        e[1] += 1
        return e[0]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            e = self.cache[key]
            e[0] = value
            self.move(key, e[1])
            e[1] += 1
        else:
            if self.count == self.capacity:
                self.remove()
            else:
                self.count += 1
            self.cache[key] = [value, 1]
            self.cnts[1].append(key)
    
    def move(self, key: int, cnt: int) -> None:
        self.cnts[cnt].remove(key)
        if cnt + 1 not in self.cnts:
            self.cnts[cnt + 1] = deque()
        self.cnts[cnt + 1].append(key)
    
    def remove(self) -> None:
        i = 1
        while True:
            if i in self.cnts and self.cnts[i]:
                key = self.cnts[i].popleft()
                self.cache.pop(key)
                return
            i += 1
```

## 代码（双向链表法，最优）
```python
from collections import defaultdict

class Node:
    __slots__ = 'prev', 'next', 'key', 'value', 'freq'
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}           # key -> Node
        self.min_freq = 1
        
        def new_list():
            dummy = Node()
            dummy.prev = dummy
            dummy.next = dummy
            return dummy
        
        self.freq_to_dummy = defaultdict(new_list)
    
    def get_node(self, key: int):
        if key not in self.cache:
            return None
        node = self.cache[key]
        self.remove(node)
        
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:
            del self.freq_to_dummy[node.freq]
            if self.min_freq == node.freq:
                self.min_freq += 1
        
        node.freq += 1
        self.push_front(self.freq_to_dummy[node.freq], node)
        return node
    
    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1
    
    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        
        if len(self.cache) == self.capacity:
            dummy = self.freq_to_dummy[self.min_freq]
            back_node = dummy.prev
            del self.cache[back_node.key]
            self.remove(back_node)
            if dummy.prev == dummy:
                del self.freq_to_dummy[self.min_freq]
        
        self.cache[key] = node = Node(key, value)
        self.push_front(self.freq_to_dummy[1], node)
        self.min_freq = 1
    
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
    
    def push_front(self, dummy: Node, x: Node) -> None:
        x.prev = dummy
        x.next = dummy.next
        x.prev.next = x
        x.next.prev = x
```

## 关键
- 核心数据结构：哈希表 + 频率桶 + 双向链表
  - cache：key → Node，O(1) 定位
  - freq_to_dummy：频率 → 哨兵头节点，每个频率桶是一个双向链表
  - min_freq：当前最小频率，O(1) 定位要淘汰的桶
- get 操作：
  - 找到节点，从原频率链表中移除
  - 若原频率桶为空且 min_freq 等于该频率，min_freq += 1
  - 节点频率 +1，插入新频率桶的头部
- put 操作：
  - key 存在：更新值 + get_node（频率+1+换桶）
  - key 不存在且满容量：淘汰 min_freq 桶的尾部节点（最久未使用），插入新节点到频率1桶
- 双向链表操作：remove（断链）和 push_front（头插），都是 O(1)

## 教训
- 看到"LFU / 最不经常使用" → 哈希表 + 频率桶 + 双向链表 + min_freq
- 和 146 LRU 对比：146 是最近最少使用（只关心时间顺序），460 是最不经常使用（关心频率+同频率下的时间顺序）
- min_freq 是关键优化：没有它，淘汰时需要从1开始遍历找非空桶，不是严格 O(1)
- 双向链表法的每个频率桶独立维护一个链表，同频率下按时间顺序排列，淘汰时去掉尾部最旧的
- 双向队列法虽然也能过，但 remove() 需要遍历频率找非空桶，最坏 O(freq)，不是严格 O(1)
- __slots__ 类似白名单，可以节省内存

## 缓存淘汰策略对比
| 题目             | 策略         | 核心数据结构                           | 淘汰依据                |
| :------------- | :--------- | :------------------------------- | :------------------ |
| 146 LRU 缓存     | 最近最少使用     | 哈希表 + 双向链表                       | 时间顺序（最久未访问）         |
| **460 LFU 缓存** | **最不经常使用** | **哈希表 + 频率桶 + 双向链表 + min\_freq** | **频率最低 + 同频率最久未访问** |
