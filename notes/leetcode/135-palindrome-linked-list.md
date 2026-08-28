# LeetCode 234 回文链表

## 我的思路（60分钟）
- 前20分钟：想用快慢指针找到中点后，再反转后半部分链表。但写的过程中发现，可以在快慢指针前进的同时就反转链表，于是推翻重来
- 中间20分钟：尝试边走边反转，但反转链表的指针操作细节没处理好（tmp、slow.next、pre 的赋值顺序混乱），一直调试不出来
- 后10分钟：看答案，核心洞察——快慢指针 + 原地反转 + pre/slow 双指针比较。需要额外用一个 pre 节点配合 slow 做反转，反转完成后 pre 指向前半段的头，slow 指向后半段的头（或中点偏移）
- 最后10分钟：根据思路写出，并通过恢复链表操作（比较过程中对 pre 重新反转一遍）

## 代码
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        pre = None
        
        # 快慢指针找中点，同时反转前半部分链表
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        
        # 链表长度为奇数时，slow 再进一步（跳过中间节点）
        if fast is not None:
            slow = slow.next
        
        # 比较前半部分（pre）和后半部分（slow）
        while slow:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        
        return True
```

## 关键
- 快慢指针：fast 走两步，slow 走一步，当 fast 到达末尾时，slow 到达中点
- 原地反转前半部分：在 slow 前进的同时，把 slow.next 指向 pre，实现前半段反转
- 奇数长度处理：fast 不为 None（说明链表长度为奇数），slow 需要再进一步跳过中间节点
- 恢复链表：比较过程中对 pre 重新做一遍反转即可（本题未展示恢复代码，但思路是再遍历一次反转回来）

## 教训
- 看到"链表回文判断" → 快慢指针找中点 + 反转前半部分 + 双指针比较
- 反转链表的指针操作顺序：先保存 tmp = slow.next，再 slow.next = pre，最后移动 pre 和 slow。顺序错一步就会断链
- 不要试图"先找中点再反转"，一边找一边反转更简洁
- 和 206 题对比：206 是纯反转链表，234 是在找中点的过程中同时反转前半部分