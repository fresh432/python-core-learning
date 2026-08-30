# LeetCode 876 链表的中间节点

## 我的思路（5分钟）
- 快慢指针找中点已经是熟练模板，之前写过多次（234、143 等题都用到）
- 这次优化了循环条件：判断 fast.next 和 fast.next.next 是否为 None，这样可以直接返回 slow.next，省去判断链表奇偶长度的额外操作

## 代码
```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = ListNode(next=head), ListNode(next=head)
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        ans = slow.next
        return ans
```

## 关键
- 虚拟头节点：fast 和 slow 都从 ListNode(next=head) 出发
- 循环条件：fast.next and fast.next.next，确保 fast 能安全走两步
- 返回 slow.next：循环结束时 slow 指向中点前一个节点（或中间偏左），slow.next 即为所求中点

## 教训
- 看到"链表找中点" → 快慢指针模板，5秒出思路
- 虚拟头节点统一边界处理，避免对头节点的特殊判断
- 和 234/143 题对比：876 是纯找中点，234/143 是在找中点的基础上做后续操作（反转/比较/重排）