# LeetCode 707 设计链表

## 我的思路（70分钟）
- 设计双向链表，节点类包含 pre、val、next 三个属性
- 初始化时创建 dummy 哨兵头节点和 tail 哨兵尾节点，length 维护链表长度
- 前30分钟：写出大致框架
- 中间30分钟：调试地狱
  - index 含义混淆：get 需要走 index+1 步（从 dummy 到目标），而 addAtIndex/deleteAtIndex 需要走 index 步（找到前驱节点）
  - pre/next 修改遗漏：添加和删除时总是漏改 dummy 或 tail 的指针
  - 长度忘记更新：添加/删除后 length 没同步修改
- 后10分钟：重构。之前图省事，只有 tail 节点用了 pre，导致添加删除需要大量特殊处理。重构后所有操作统一处理 pre 指针，代码简洁后通过

## 代码
```python
class MyLinkedList:
    class ListNode:
        def __init__(self, val=0):
            self.val = val
            self.next = None
            self.pre = None
    
    def __init__(self):
        self.tail = ListNode()
        self.dummy = ListNode()
        self.dummy.next = self.tail
        self.tail.pre = self.dummy
        self.length = 0
    
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.dummy
        for _ in range(index + 1):
            cur = cur.next
        return cur.val
    
    def addAtHead(self, val: int) -> None:
        cur = ListNode(val=val)
        cur.next = self.dummy.next
        cur.pre = self.dummy
        self.dummy.next.pre = cur
        self.dummy.next = cur
        self.length += 1
    
    def addAtTail(self, val: int) -> None:
        cur = ListNode(val=val)
        self.tail.pre.next = cur
        cur.pre = self.tail.pre
        cur.next = self.tail
        self.tail.pre = cur
        self.length += 1
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        tmp = self.dummy
        for _ in range(index):
            tmp = tmp.next
        cur = ListNode(val=val)
        cur.next = tmp.next
        cur.pre = tmp
        tmp.next.pre = cur
        tmp.next = cur
        self.length += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        tmp = self.dummy
        for _ in range(index):
            tmp = tmp.next
        tmp.next = tmp.next.next
        tmp.next.pre = tmp
        self.length -= 1
```

## 关键
- 双向链表 + 双哨兵（dummy 头 + tail 尾），统一边界处理
- pre 和 next 必须成对修改，不要漏任何一边
- get 走 index+1 步，addAtIndex/deleteAtIndex 走 index 步（找前驱）
- 长度维护：每次添加/删除后同步 length

## 教训
- 看到"设计链表" → 双向链表 + 双哨兵，所有指针操作成对出现
- 不要图省事省略 pre 指针的处理，否则重构代价更大
- 和 146/460 题对比：146/460 是缓存设计（哈希表+双向链表），707 是基础链表操作
