# LeetCode 495 提莫攻击

## 我的思路（15分钟）
- 维护中毒时间结束的边界 edge
- 遍历 timeSeries：
  - 遇到重复攻击时间直接跳过
  - 若当前攻击时间 <= edge（在上次中毒期间）：ans += 当前攻击时间 + duration - edge（只加重叠后的额外时间），更新 edge
  - 若当前攻击时间 > edge（上次已结束）：ans += duration，更新 edge = 当前攻击时间 + duration

## 代码
```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        i = 0
        ans = 0
        edge = timeSeries[0]
        
        while i < len(timeSeries):
            while i != 0 and timeSeries[i] == timeSeries[i - 1]:
                i += 1
            
            if timeSeries[i] <= edge:
                ans += timeSeries[i] + duration - edge
                edge = timeSeries[i] + duration
            else:
                ans += duration
                edge = timeSeries[i] + duration
            
            i += 1
        
        return ans
```

## 关键
- edge：当前中毒效果结束的时间点
- 重叠处理：若新攻击在上次中毒期间，只加额外时间（timeSeries[i] + duration - edge）
- 不重叠：直接加 duration

## 教训
- 看到"时间序列重叠区间求总时长" → 维护结束边界，重叠时只加额外时间