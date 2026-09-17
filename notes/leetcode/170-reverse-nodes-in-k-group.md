# LeetCode 25 K 个一组翻转链表

## 我的思路（35分钟）
- 用迭代法，不拆分主函数和子函数，整体一个循环处理
- 先用计数指针 c 探测后续是否还有 k 个节点，不够则直接返回结果
- 够 k 个则边走边反转：用 tmp 保存当前节点，pre 前进，tmp.next = t 实现头插法反转
- 反转完成后重接链表：
  - hd（原反转段头，现变尾）连接后续片段 hd.next = pre
  - ht（反转段前的父节点）连接新头 ht.next = tmp
  - ht = hd 移动父节点指针，准备处理下一段
- 中间指针关系复杂，理清思路花了点时间

## 代码
```python
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        ans = ListNode(next=head)
        pre = head
        ht = ans
        
        while pre:
            t = None
            hd = pre
            c = pre
            count = 0
            
            # 探测后续是否有 k 个节点
            while c and count < k:
                c = c.next
                count += 1
            
            if count != k:
                return ans.next
            
            # 反转 k 个节点（头插法）
            while count > 0:
                tmp = pre
                pre = pre.next
                tmp.next = t
                t = tmp
                count -= 1
            
            # 重接链表
            hd.next = pre      # 反转后的尾部连接后续
            ht.next = tmp      # 前一段的尾部连接反转后的新头部
            ht = hd            # 移动父节点指针
        
        return ans.next
```

## 关键
- 探测阶段：先走 k 步确认节点足够，不够直接返回
- 反转阶段：头插法，tmp.next = t，t 始终指向新链表的头
- 重接阶段：hd 是反转前的头（反转后的尾），ht 是反转段前面的节点
- 虚拟头节点 ans：统一处理头节点的边界情况

## 教训
- 看到"每 k 个反转链表" → 探测 + 头插法反转 + 重接前后
- 指针多的时候先在纸上画清楚：pre（当前遍历）、hd（段头）、ht（段前父节点）、t（反转后的新头）
- 和 92 题对比：92 是反转指定区间 [left, right]，25 是每 k 个分组反转，核心都是头插法+重接，但 25 需要循环处理多段
