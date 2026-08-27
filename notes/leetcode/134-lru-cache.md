# LeetCode 146 LRU 缓存

## 我的思路（75分钟）
- 前30分钟：用 deque 实现，思路是访问已有 key 时删除旧位置再追加到队尾，超容量时 popleft()。虽然通过了，但时间复杂度 O(n)（remove 操作遍历队列），1443ms
- 中间30分钟：看答案，理解核心数据结构——哈希表 + 双向链表，哈希表 O(1) 定位节点，双向链表 O(1) 移动/删除节点
- 后15分钟：跟着写了一遍双向链表版本，11ms

## 代码（deque 版，超时边缘）
```python
from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.queue = deque()
        self.capacity = capacity
        self.current_c = 0

    def get(self, key: int) -> int:
        for k, v in self.queue:
            if k == key:
                self.queue.remove([k, v])
                self.queue.append([k, v])
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.queue.pop()
            self.current_c -= 1
        self.queue.append([key, value])
        self.current_c += 1
        if self.current_c > self.capacity:
            self.queue.popleft()
            self.current_c -= 1
```

## 代码（哈希表 + 双向链表，最优）
```python
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_node_to_tail(key)
            return self.hashmap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new
```

## 关键
- 核心数据结构：哈希表 + 双向链表
  - 哈希表：key → ListNode，O(1) 定位
  - 双向链表：维护访问顺序，越靠近尾部越新，头部最旧
- move_node_to_tail：把访问过的节点移到尾部（标记为最新使用）
- put 超容量：删除头部最旧节点（head.next），同时从哈希表中移除

## 教训
- 看到"LRU / 最近最少使用" → 哈希表 + 双向链表，不要想当然用 deque.remove()（O(n) 会超时）
- deque 的 remove 是线性扫描，数据量大时性能极差，1443ms vs 11ms 的差距就在这里
- 双向链表操作要细心：node.prev.next = node.next 和 node.next.prev = node.prev 成对出现，不要漏
- 哨兵节点（dummy head/tail）简化边界处理，避免空指针判断

## 数据结构选择对比
| 数据结构           | get      | put      | 原因                |
| :------------- | :------- | :------- | :---------------- |
| `deque` + 遍历   | O(n)     | O(n)     | `remove` 线性扫描     |
| **哈希表 + 双向链表** | **O(1)** | **O(1)** | **哈希定位 + 链表指针操作** |
