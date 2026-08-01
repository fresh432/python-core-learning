# LeetCode 1143 最长公共子序列

## 我的思路（50分钟）
1. 前20分钟：想到了状态定义，但用的是一维数组，导致状态转移方程想不出来
2. 后30分钟：看答案理解——需要二维数组 dp[i][j]，表示 text1[0:i] 和 text2[0:j] 的最长公共子序列长度

## 代码
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[M][N]
```

## 关键
- 状态定义：dp[i][j] = text1[0:i] 和 text2[0:j] 的最长公共子序列长度
- 状态转移：
  - 字符相等：dp[i][j] = dp[i-1][j-1] + 1（继承左上角 + 1）
  - 字符不等：dp[i][j] = max(dp[i][j-1], dp[i-1][j])（取左边或上边的最大值）
- 二维数组：两个字符串的问题，一维无法同时保存两个维度的信息

## 教训
- 看到"两个字符串的比较/匹配" → 二维 DP，dp[i][j] 分别对应两个字符串的前缀
- 一维 DP 适合单个序列的问题（如 LIS），两个序列必须用二维
- 初始化多一行一列（M+1 × N+1），方便处理空字符串边界