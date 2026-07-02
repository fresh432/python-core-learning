# LeetCode 面试题 02.07 链表相交

## 思路（15分钟，看答案）
双指针换头：A走完走B，B走完走A，总路程相同。

## 代码
```python
def getIntersectionNode(headA, headB):
    pa, pb = headA, headB
    while pa != pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa
```

## 关键理解
- 总路程：pa走 a+c+b，pb走 b+c+a
- 有交点必相遇，无交点在None相遇
- 空间O(1)，比哈希表优

## 教训
- 哈希表第一反应，但空间高，放弃正确
- 长度比对可行但复杂，双指针换头最优雅
- 15分钟想不出应及时看答案，理解比死磕重要