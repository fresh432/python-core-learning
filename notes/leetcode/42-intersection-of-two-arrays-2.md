# LeetCode 350 两个数组的交集 II

## 思路（30分钟，看答案）
Counter计数：先统计nums1中各数字出现次数，再遍历nums2匹配。

## 代码
```python
def intersect(nums1, nums2):
    ans = []
    cnt = Counter(nums1)
    for x in nums2:
        if cnt[x] &gt; 0:
            ans.append(x)
            cnt[x] -= 1
    return ans
```

## 关键
- Counter(nums1) 一行完成计数
- 遍历nums2，匹配一个计数减1

## Counter用法
```python
from collections import Counter
Counter([1,2,2,3])  # {2:2, 1:1, 3:1}
```

## 教训
- 30分钟想手动实现计数，复杂且易错
- Python标准库要熟悉，Counter是利器
- 和12题（交集）的区别：保留重复，需计数
