# LeetCode 328 奇偶链表

## 我的思路（5分钟）
- 设置两个哨兵节点——dummy1 存奇数位置节点，dummy2 存偶数位置节点
- 遍历原链表，每次循环将当前节点接在奇链表后，下一个节点接在偶链表后
- 最后将两个链表连接：pre1.next = dummy2.next

## 代码
```python
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        dummy1 = ListNode()
        dummy2 = ListNode()
        pre1, pre2 = dummy1, dummy2
        
        while head:
            pre1.next = head
            head = head.next
            pre1 = pre1.next
            
            if not head:
                break
            
            pre2.next = head
            head = head.next
            pre2 = pre2.next
        
        if pre2:
            pre2.next = None
        
        pre1.next = dummy2.next
        return dummy1.next
```

## 关键
- 双哨兵节点：奇链表和偶链表分开维护
- 每次循环处理两个节点（一奇一偶）
- 注意奇数个节点时，最后一个奇数节点处理后 head 为空，需要 break
- 最后将偶链表尾部置空，防止成环

## 教训
- 看到"链表奇偶位置重排" → 双哨兵拆分+拼接，一次遍历完成
- 和 86 题对比：86 是按值分区，328 是按位置分区，都是双链表法的应用
