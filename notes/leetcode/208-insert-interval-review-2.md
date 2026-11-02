# LeetCode 57 插入区间（复习）

## 我的思路（4分钟）
- 三段扫描：第一段将右边界小于待插入区间左边界的区间加入 ans；第二段扫描通过扩张待插入区间的左右边界达到去重目的，再将去重后的新区间加入 ans；第三段将剩下的所有区间加入 ans，返回 ans

## 代码
```python
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        n = len(intervals)
        i = 0
        # 第一段：右边界在 newInterval 起点之前的，无重叠，直接加入
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        # 第二段：与 newInterval 重叠的，合并（扩张边界）
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        # 第三段：剩余区间全部加入
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
```

## 教训
- 复习 4 分钟一遍通过，三段扫描已完全掌握（上次复习 25 分钟还想一次遍历，这次直接三段）