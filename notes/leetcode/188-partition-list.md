# LeetCode 86 分隔链表

## 我的思路（40分钟）
- 前25分钟：想原地修改——维护快慢指针，slow 指向小于 x 的连续段末尾，fast 配合哨兵节点探测并转移小值节点到前面。指针操作复杂，需要回退
- 后5分钟：看答案，发现双链表法更清晰——不需要回退操作，只需维护两条链表的头尾指针（< x 的和 >= x 的），遍历完原链表后拼接即可
- 后10分钟：按双链表思路写了一遍，通过

## 代码（原地修改法）
```python
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy = head
        slow = ListNode(next=head)
        ans = slow
        
        # 找到第一个 >= x 的节点位置
        while dummy and dummy.val < x:
            slow = dummy
            dummy = dummy.next
        
        fast = dummy
        while dummy:
            if dummy.val < x:
                fast.next = dummy.next
                dummy.next = slow.next
                slow.next = dummy
                dummy = fast
                slow = slow.next
            if not dummy:
                break
            fast = dummy
            dummy = dummy.next
        
        return ans.next
```

## 代码（双链表法）
```python
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy = ListNode(next=head)
        smaller = ListNode()    # < x 的链表
        ans = smaller
        pre, cur = dummy, head
        
        while cur:
            if cur.val < x:
                pre.next = cur.next   # 从原链表移除
                smaller.next = cur    # 接到小链表
                smaller = smaller.next
            else:
                pre = pre.next
            cur = cur.next
        
        smaller.next = dummy.next   # 拼接
        return ans.next
```

## 关键
- 双链表法：遍历一次，< x 的节点拆到 smaller 链表，>= x 的留在原链表，最后拼接
- 原地修改法：指针操作复杂，需要维护多个指针位置，容易出错
- 虚拟头节点：统一边界处理

## 教训
- 看到"链表按值分区" → 双链表拆分+拼接，代码清晰不易错
- 和 21 题对比：21 是合并两个有序链表，86 是按条件拆分成两个链表再合并
