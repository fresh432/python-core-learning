# LeetCode 452 用最少数量的箭引爆气球

## 我的思路（20分钟）
- 和 435 题思路类似，按起点排序，维护一个 edge 边界
- 遍历气球，若当前气球起点 > edge（不重叠），则需要新的一支箭，ans += 1，edge 更新为当前气球的右边界
- 若重叠，则 edge = min(edge, 当前右边界)，保留最小的右边界作为新的重叠区域边界
- edge 初始化为 -inf

## 代码
```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        n = len(points)
        ans = 0
        edge = -inf
        
        for i in range(n):
            if points[i][0] > edge:
                ans += 1
                edge = points[i][1]
            else:
                edge = min(points[i][1], edge)
        
        return ans
```

## 关键
- 按起点排序，保证只需比较相邻气球
- 重叠时保留最小右边界：edge = min(edge, points[i][1])
- 不重叠时：ans += 1，edge 更新为当前气球右边界

## 教训
- 看到"最少箭射爆所有气球" → 贪心保留最小右边界
- 和 435 题对比：435 是移除最少区间使不重叠，452 是最少箭射爆所有重叠气球，核心都是贪心维护最小右边界
