# LeetCode 146 LRU 缓存（复习）

## 我的思路（30分钟）
- 前15分钟：想到双向链表 + 虚拟头节点和虚拟尾节点方便增删。设计的是链表节点只存 value、哈希表只存 key→value；get 直接从哈希表返回 value；get 和 put 后都要把改动节点移到链表头部；超容量时弹出链表尾部节点。但运行有问题
- 看了之前提交的答案才发现：要把 key 也放进链表节点里、哈希表存 key→节点，这样后续取节点操作方便很多。后15分钟重构了一遍，并把"移动至头部"单拎成独立函数 move_to_head，通过

## 代码
```python
class ListNode:
    def __init__(self, key=None, val: int = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()          # 虚拟头
        self.tail = ListNode()          # 虚拟尾
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hash_map = {}              # key → 节点

    def move_to_head(self, key):
        node = self.hash_map[key]
        # 摘下
        node.prev.next = node.next
        node.next.prev = node.prev
        # 挂到头后
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.move_to_head(key)
            return self.hash_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].val = value
            self.move_to_head(key)
        else:
            if self.capacity == len(self.hash_map):   # 满了，逐出尾部
                tmp = self.tail.prev
                del self.hash_map[tmp.key]
                tmp.prev.next = self.tail
                self.tail.prev = tmp.prev
            new = ListNode(key, value)
            self.hash_map[key] = new
            new.prev = self.head                       # 头插
            new.next = self.head.next
            self.head.next.prev = new
            self.head.next = new
```

## 关键
- 数据结构组合：哈希表（O(1) 定位）+ 双向链表（O(1) 移动/删除），链表维护使用频率的"时钟序"
- 哈希表存"key → 节点"而不是"key → value"，这是本次复习重要的认知修正：只有拿到节点才能做链表操作
- 虚拟头尾节点：所有插入都变成"头后插入"，所有删除都变成"尾前删除"，无需判空
- move_to_head 复用于 get 和 put 两处，必须抽成独立函数

## 教训
复习： 30 分钟，第一版设计的缺陷（节点不存 key、哈希表存 value）正是上次看答案时绕过的坑，"节点必须能自我定位（存 key）"是 LRU 的隐含约束
