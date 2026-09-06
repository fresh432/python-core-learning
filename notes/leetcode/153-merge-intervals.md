# LeetCode 56 合并区间

## 我的思路（60分钟）
- 前20分钟：想到先排序再遍历，但试图寻找线性解法（不排序），没成功
- 中间30分钟：改用库函数排序，在端点比较逻辑上卡了很久。想减少空间复杂度用了倒序遍历，但倒序有 bug，改回正序遍历
- 后10分钟：解决边界问题——合并时同步缩小边界范围（pop 被合并的区间），成功通过

## 代码
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i, n = 1, len(intervals)
        while i < n:
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                intervals.pop(i)
                n -= 1
                continue
            i += 1
        return intervals
```

## 关键
- 先按区间起点排序，保证只需比较相邻区间
- 重叠条件：intervals[i][0] <= intervals[i-1][1]
- 合并后右端点取 max：intervals[i-1][1] = max(...)
- 原地修改：用 pop(i) 删除被合并区间，n -= 1，i 不动继续检查下一个

## 教训
- 看到"区间合并" → 先排序，线性解法不存在（需要先确定相对顺序）
- 倒序遍历在区间合并场景下容易逻辑混乱，正序遍历+原地 pop 更直观
- pop 后 n 要减1，i 不要自增（继续检查当前位置的新邻居）
- 和 57 题对比：56 是合并所有重叠区间，57 是插入一个新区间再合并