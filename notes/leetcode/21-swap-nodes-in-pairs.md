# LeetCode 24 两两交换链表中的节点

## 我的思路（25分钟)
虚拟头节点 + 三指针操作，cur每次移动两步。

## 代码
```python
def swapPairs(head):
    dummy = cur = ListNode(next=head)
    a = head
    while a and a.next:
        b = a.next
        temp = b.next
        b.next = a
        a.next = temp
        cur.next = b      # ← 关键！前面节点要指向新头
        cur = a
        if cur.next:
            a = cur.next
    return dummy.next
```

## 教训
- 交换节点时，三个连接都要处理
- 别忘了 cur.next = b，否则链表断开
- 卡了10分钟，下次画图确认连接