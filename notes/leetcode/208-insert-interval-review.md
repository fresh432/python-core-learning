# LeetCode 57 插入区间（复习）

## 我的思路（25分钟）
- 前20分钟：想通过一次遍历把非重叠区间加入 ans 的同时更新插入区间的左右边界，最后插入去重后的新区间——特殊情况太多处理不完
- 后5分钟：翻之前通过的代码才想起三段扫描：先遍历不重叠的左段加入 ans；单独处理重叠区间（更新插入区间的左右边界实现合并）；再把剩余元素全部加入 ans

## 代码
```python
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        n = len(intervals)
        i = 0
        # 左段：end 在 newInterval 起点之前的区间，直接加入
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        # 中段：与 newInterval 重叠的区间，合并进 newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        # 右段：剩余的区间全部加入
        while i < n:
            ans.append(intervals[i])
            i += 1  
        return ans
```

## 关键
- 三段扫描：左段（无重叠）→ 中段（合并更新边界）→ 右段（无重叠）
- 重叠判定：intervals[i][0] <= newInterval[1]，合并取左右边界 min/max

## 教训
- 复习时想到了"更新边界去重"的核心，但忘了三段扫描的简洁框架
- 一次遍历同时做两件事容易陷入特殊情况；拆成三段各管一段，代码自然简洁
