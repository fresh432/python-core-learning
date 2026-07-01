# LeetCode 19 删除链表的倒数第 N 个结点

## 我的思路 (15分钟)

## 代码
```python
def removeNthFromEnd(head, n):
    dummy = ptr = ListNode(next=head)
    count = head
    len = 0
    while count:
        count = count.next
        len += 1
    for _ in range(len - n):
        ptr = ptr.next
    ptr.next = ptr.next.next
    return dummy.next
```

## 更优解：快慢指针
```python
def removeNthFromEnd(head, n):
    dummy = fast = slow = ListNode(next=head)
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
```

## 教训
- 我的解法正确，但两次遍历
- 快慢指针一次遍历，表现更优
- 快指针先走n+1步是关键