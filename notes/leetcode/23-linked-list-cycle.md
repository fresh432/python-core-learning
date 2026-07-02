# LeetCode 141 环形链表

## 思路
快慢指针：快指针2步，慢指针1步，相遇则有环。

## 代码
```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
```

## 关键
- 循环条件：fast and fast.next（确保能走2步）
- 无环时fast先到尾