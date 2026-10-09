# LeetCode 57 插入区间

## 我的思路（60分钟）
- 前15分钟：想先用二分查找找插入位置，然后把前面区间直接加入 ans，再合并重叠区间，最后加入剩余区间。但边界问题调试了40分钟始终调不通
- 后5分钟：看答案，改用三段遍历法：
  1. 第一段：遍历左边界，条件 intervals[i][1] < newInterval[0]（当前区间右边界小于新区间左边界，即完全不重叠），直接加入 ans
  2. 第二段：遍历重叠区间，条件 intervals[i][0] <= newInterval[1]（当前区间左边界小于等于新区间右边界），只更新 newInterval 的左右边界（min 左边界，max 右边界）
  3. 第三段：将更新后的 newInterval 加入 ans，再把剩余区间全部加入
- 核心差异：二分找插入点会引入大量边界特殊情况，三段遍历更直观

## 代码
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        i = 0
        
        # 第一段：左边不重叠的区间直接加入
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        # 第二段：合并所有重叠区间到 newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        ans.append(newInterval)
        
        # 第三段：右边剩余的区间直接加入
        while i < n:
            ans.append(intervals[i])
            i += 1
        
        return ans
```

## 关键
- 三段法：左边不重叠 → 中间合并 → 右边不重叠
- 合并条件：intervals[i][0] <= newInterval[1]（左边界小于等于新区间右边界）
- 不重叠条件：intervals[i][1] < newInterval[0]（右边界严格小于新区间左边界）
- 更新 newInterval：左边界取 min，右边界取 max

## 教训
- 看到"插入新区间到有序区间列表" → 三段遍历法，不要先二分找位置（边界情况太多）
- 区间题的边界处理是弱项，需要多练

