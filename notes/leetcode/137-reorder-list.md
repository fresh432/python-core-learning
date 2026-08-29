# LeetCode 143 重排链表

## 我的思路（35分钟）
- 前15分钟：确定三步走策略——找中点 → 反转后半段 → 交错合并。思路清晰，写好大致框架
- 中间15分钟：调试踩坑
  - 坑1：找到中点后忘记切断前后链表，prev.next = None 没写，导致反转后半段时形成环，遍历死循环
  - 坑2：没考虑链表只有一个节点的情况，边界处理遗漏
- 后5分钟：修复上述问题，成功通过

## 代码
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: 快慢指针找中点
        fast, slow, prev = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if fast == slow:
            return 
        if fast:
            slow = slow.next
            prev = prev.next
        # Step 2: 切断链表，prev 指向前半段末尾
        prev.next = None
        
        # Step 3: 反转后半段
        rev = slow
        ins = None
        while rev:
            tmp = rev.next
            rev.next = ins
            ins = rev
            rev = tmp
        
        # Step 4: 交错合并：前半段 head，后半段 ins
        while ins:
            tmp_h = head.next
            tmp_i = ins.next
            head.next = ins
            ins.next = tmp_h
            head = tmp_h
            ins = tmp_i
```

## 关键
- 三步固定套路：找中点 → 断链 → 反转后半段 → 交错插入
- 切断链表：prev.next = None 是关键，否则后半段反转时会带回环
- 奇数长度处理：快慢指针结束后，slow 指向后半段的头，prev 指向前半段的尾
- 交错合并：用临时变量保存 head.next 和 ins.next，避免断链后丢失后续节点

## 教训
- 看到"链表重排 / L0→Ln→L1→Ln-1..." → 三步走：找中点、反转后半、交错合并
- 切断操作不要漏：prev.next = None 是防止成环的关键
- 边界情况：链表长度为0或1时直接返回
- 和 234 题对比：234 是找中点+反转+比较，143 是找中点+反转+交错合并，前两步几乎一样