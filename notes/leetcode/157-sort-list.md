# LeetCode 148 排序链表

## 我的思路（60分钟）
- 前15分钟：完全没思路，链表排序不知道从何下手
- 中间15分钟：看答案，了解自顶向下归并排序——快慢指针找中点切分，递归排序左右子链表，再合并。从最小单位（单个节点）开始逐层合并
- 后5分钟：自己写出递归版本
- 后20分钟：看自底向上归并排序——先算链表长度，以 intv=1,2,4,8... 为步长逐层合并，每轮合并完步长翻倍，直到 intv >= length
- 后5分钟：实现自底向上版本

## 代码（自顶向下递归法）
```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 快慢指针找中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid, slow.next = slow.next, None  # 切断链表
        
        left, right = self.sortList(head), self.sortList(mid)
        
        # 合并两个有序链表
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        
        return res.next
```

## 代码（自底向上归并排序）
```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        
        res = ListNode(next=head)
        
        while intv < length:
            pre, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break  # h1 长度不足 intv，无需合并
                
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                
                c1, c2 = intv, intv - i  # 两个子链表的长度
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            
            intv *= 2
        
        return res.next
```

## 关键
- 自顶向下：递归切分 + 合并，时间 O(n log n)，空间 O(log n)（递归栈）
- 自底向上：迭代按步长合并，时间 O(n log n)，空间 O(1)
- 快慢指针找中点：fast 从 head.next 开始，slow 最终指向中点前一个节点
- 切断操作：mid, slow.next = slow.next, None

## 教训
- 看到"链表排序，要求 O(n log n)" → 归并排序，链表场景下自底向上可实现 O(1) 空间
- 快慢指针找中点时，fast 从 head.next 开始而不是 head，这样 slow 会停在中间偏左的位置（前半段尾节点）
- 和 21 题对比：21 是合并两个有序链表，148 是递归/迭代地合并多对有序子链表
