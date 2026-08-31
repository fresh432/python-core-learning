# LeetCode 83 删除排序链表中的重复元素

## 我的思路（7分钟）
- 快慢指针遍历，快指针 fast 逐个检查节点值
- 若 slow.val == fast.val：slow.next = fast.next（跳过重复节点，slow 不动）
- 若不同：slow = fast（慢指针推进到快指针位置）
- 踩坑：写漏了比较条件，导致调试了几分钟才通过

## 代码
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow, fast = head, head.next
        ans = head
        
        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        
        return ans
```

## 关键
- 链表已排序，重复元素必然相邻
- 保留一个重复元素：遇到重复只修改 slow.next，不移动 slow
- 遇到不同值时才移动 slow = fast
- 边界：head 为空或只有一个节点直接返回

## 教训
- 看到"排序链表去重（保留一个）" → 快慢指针，相同则 slow.next = fast.next，不同则 slow = fast
- 不要漏写 slow.val == fast.val 的比较条件
- 和 26 题对比：26 是数组原地去重（快慢指针覆盖），83 是链表跳过重复节点（修改 next 指针）