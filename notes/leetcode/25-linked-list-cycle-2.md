# LeetCode 142 环形链表 II

## 思路（30分钟，独立解出）
1. 快慢指针找相遇点（141题已会）
2. 相遇后，头指针和慢指针同步走
3. 相遇点即环入口

## 代码
```python
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:          # 相遇
            ans = head
            while ans != slow:    # 同步走
                ans = ans.next
                slow = slow.next
            return ans            # 入口
    return None
```

## 数学原理
- 慢指针走：a + x
- 快指针走：a + x + nb = 2(a + x)
- 推导：a = (n-1)b + (b-x)
- 即：从头走a步 = 从相遇点走(n-1)圈 + 剩余
- 所以同步走必在入口相遇

## 关键
- 快慢指针找环是经典套路
- 找入口的数学推导要理解，不要死记
- 调试10分钟正常，注意边界条件