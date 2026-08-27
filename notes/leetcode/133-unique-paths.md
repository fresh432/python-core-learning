# LeetCode 62 不同路径

## 我的思路（30分钟）
- 前10分钟：审题失误，没看完题目就默认机器人可以上下左右自由移动，完全没头绪
- 中间10分钟：重新审题，发现只能向右和向下移动，立刻想到二维DP——每个格子的路径数 = 上方格子路径数 + 左方格子路径数
- 后10分钟：二维DP通过后，进一步压缩为一维滚动数组

## 代码（二维DP）
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1  # 初始化：让dp[1][1] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m][n]
```

## 代码（一维优化）
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        
        return dp[-1]
```

## 关键
- 状态定义：dp[i][j] 表示到达 (i, j) 的不同路径数
- 状态转移：dp[i][j] = dp[i-1][j] + dp[i][j-1]（只能从上或左来）
- 一维优化：按行遍历，dp[j] 表示当前行第 j 列的路径数，原地更新

## 教训
- 审题！审题！审题！ 不要没看完题目就假设约束条件，"只能向右和向下"是核心限制
- 看到"网格路径计数" → 二维DP，状态转移来自上方和左方
- 一维优化技巧：滚动数组，dp[j] += dp[j-1]，空间从 O(mn) → O(n)