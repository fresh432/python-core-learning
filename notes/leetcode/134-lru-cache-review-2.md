# LeetCode 146 LRU 缓存（复习）

## 我的思路（17分钟）
- 用双向链表存值：对已存在的值查询或修改时移到链表头；添加新值超容量时弹出链表尾部元素
- 哈希表存放所有节点方便查询存在性；链表维护数据可快速更新位置，两个操作都保证 O(1)

## 代码
```python
class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hash_map = {}

    def move_to_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
    # get / put 略（与上次相同）
```

## 教训
- 复习: 17 分钟（30 → 17），"哈希存节点 + move_to_head 独立函数"的结构一次成型