# LeetCode 435 无重叠区间

## 我的思路（45分钟）
- 前25分钟：想用 DP 法，按起点排序后比较是否重叠，但想不出状态转移方程
- 中间：看提示，核心洞察——贪心法：按起点排序后，维护一个 tail（当前保留区间的最小右端点）。遇到重叠时，选尾巴更小的那个作为新的 tail，因为更小的尾巴能为后续留下更多空间
- 后10分钟：根据思路写出，注意非重叠时也要更新 tail 为当前区间的右端点
- 后10分钟：看了 DP 解法（按终点排序 + 双层遍历，O(n²)），时间不如贪心，没写

## 代码
```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        count = 0
        tail = intervals[0][1]
        
        for i in range(1, n):
            if tail > intervals[i][0]:      # 重叠
                count += 1
                tail = min(intervals[i][1], tail)  # 选尾巴小的
            else:                            # 不重叠
                tail = intervals[i][1]
        
        return count
```

## 关键
- 按起点排序，保证只需比较相邻区间
- 重叠时 count += 1，并选右端点更小的作为 tail
- 不重叠时更新 tail 为当前区间右端点
- 贪心正确性：选尾巴小的保留，为后续区间留下更多空间

## 教训
- 看到"最少移除多少个区间使剩余不重叠" → 贪心，按起点排序，重叠时选尾巴小的
- 和 56 题对比：56 是合并重叠区间，435 是移除最少区间使不重叠，都是先排序再遍历
- DP 法 O(n²) 也能做，但贪心 O(n log n) 更优
