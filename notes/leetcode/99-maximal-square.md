# LeetCode 221 最大正方形

## 我的思路（60分钟）
- 前15分钟：直觉想到用 DP，只需要保存以每个位置为右下角的最大正方形边长即可
- 中间30分钟：状态转移写复杂了，给每种情况写了独立的 if 判断，逻辑越绕越晕，调试了很久
- 后15分钟：发现状态转移其实很简单——只要当前格子是 '1'，且左上、左边、上边都不为 0，当前边长就是三者最小值 + 1

## 代码
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1
                    if dp[i - 1][j - 1] != 0 and dp[i - 1][j] != 0 and dp[i][j - 1] != 0:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(res, dp[i][j])
        
        return res ** 2
```

## 关键
- 状态定义：dp[i][j] = 以 matrix[i-1][j-1] 为右下角的最大正方形边长
- 状态转移：当前为 '1' 时，dp[i][j] = min(左上, 上边, 左边) + 1
  - 为什么取 min：正方形的扩展受限于三个方向中最短的那条边，只有三个方向都能支撑边长 k，才能扩展成 k+1
- 初始化：dp 数组多一行一列，初始为 0，天然处理边界（第一行/列的正方形边长最多为 1）
- 结果：最大边长的平方（题目要的是面积）

## 教训
- 看到"矩阵中最大正方形" → 二维 DP，dp[i][j] 表示以 (i,j) 为右下角的最大边长
- 状态转移不要写复杂：实际上可以简化为一句 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1，不需要额外的 if 判断（dp 初始化为 0，min(0,0,0)+1 = 1 正好覆盖边界）