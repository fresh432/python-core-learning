# LeetCode 64 最小路径和

## 我的思路（15分钟）
- 前7分钟：根据动态规划思路直接写出——只能向下和向右走，每个格子只能从上方或左方到达，选择两条路径中较小的那个值加上当前格子值
- 后8分钟：优化——直接在原数组上修改，省去 dp 数组空间；同时把初始化（第一行、第一列）和主体 DP 合并到一次循环中，节省初始化时间

## 代码（二维DP）
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            dp[i][1] = dp[i - 1][1] + grid[i - 1][0]
        for j in range(1, n + 1):
            dp[1][j] = dp[1][j - 1] + grid[0][j - 1]
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        
        return dp[-1][-1]
```

## 代码（原地优化）
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]
```

## 关键
- 状态转移：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
- 边界：第一行只能从左边来，第一列只能从上边来
- 原地优化：直接在 grid 上累加，空间从 O(mn) → O(1)

## 教训
- 原地修改是常见优化技巧，但会修改输入数组
- 和 62 题对比：62 是路径计数（加法），64 是最小路径和（取 min + 加法）
