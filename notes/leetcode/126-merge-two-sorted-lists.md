# LeetCode 21 合并两个有序链表

## 我的思路（10分钟）
- 构建虚拟头节点（dummy），用哨兵节点 head 逐个拼接两个链表中较小的节点
- 最后返回 dummy.next

## 代码
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head
        
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        # 剩余节点直接接上
        if not list1:
            head.next = list2
        elif not list2:
            head.next = list1
        
        return ans.next
```

## 关键
- 虚拟头节点 dummy：避免处理头节点的特殊边界，代码更统一
- 双指针比较：谁小接谁，head = head.next 推进
- 剩余节点：其中一个链表遍历完后，另一个链表剩余部分直接接上（已有序）
- 返回 ans.next（跳过多余的虚拟头节点）

## 教训
- 和 26 题对比：都是双指针，26 是数组原地覆盖，21 是链表指针拼接