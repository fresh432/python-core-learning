# LeetCode 160 相交链表（复习）

## 时间
3分钟，独立解出

## 思路
双指针换头，和面试题02.07完全相同。

## 代码
```python
def getIntersectionNode(headA, headB):
    pa, pb = headA, headB
    while pa != pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa
```

## 关键
- pa走A+B，pb走B+A
- 总长度相同，有交点必相遇