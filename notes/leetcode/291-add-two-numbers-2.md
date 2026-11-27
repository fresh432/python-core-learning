# LeetCode 445 两数相加 II

## 我的思路（16分钟）
- 一开始想翻转链表再相加、同时构建新链表；看到进阶要求"不能翻转链表"
- 想到栈：先分别遍历两个链表将值存入栈中，再分别弹栈得到同位的数字进行相加，进位需要额外记录，然后用新值构建新链表节点（头插），最后返回链表头。简单调试后通过

## 代码
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        tail = None
        extra = 0
        while s1 or s2 or extra:
            num = extra
            if s1:
                num += s1.pop()      # 栈顶 = 个位
            if s2:
                num += s2.pop()
            extra = num // 10
            new = ListNode(num % 10)
            new.next = tail          # 头插：高位在前
            tail = new
        return tail
```

## 关键
- 栈把"高位在前"的链表转成"个位先出"的顺序，等价于翻转链表的效果但不修改原链表
- 循环条件 s1 or s2 or extra：处理末位进位
- 头插法构建结果：每次新节点接在 tail 前面，自然形成高位在前的顺序

## 教训
- 看到"逆序存储的数字相加，但不允许翻转链表" → 栈
- 和 2 对比：2 是低位在前（正向遍历即可），445 是高位在前（栈或翻转），先看清数字的存储顺序再选工具