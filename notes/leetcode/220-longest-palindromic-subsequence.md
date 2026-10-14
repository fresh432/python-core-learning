# LeetCode 516 最长回文子序列

## 我的思路（45分钟）
- 前15分钟：想到从每个字符出发向两边探索的暴力解法
- 中间15分钟：想 DP 解法，但字符串 DP 的状态定义想不出来，不知道每个维度的含义
- 后15分钟：看答案，理解后写出

## 代码（二维 DP）
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][-1]
```

## 代码（一维优化）
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        
        for i in range(n - 1, -1, -1):
            tmp = dp[i]
            dp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    ori = tmp
                    tmp = dp[j]
                    dp[j] = ori + 2
                else:
                    tmp = dp[j]
                    dp[j] = max(dp[j], dp[j - 1])
        
        return dp[-1]
```

## 关键
- 状态定义：dp[i][j] 表示 s[i:j+1] 中最长回文子序列的长度
- 遍历顺序：i 倒序，j 正序（i < j），因为 dp[i][j] 依赖 dp[i+1][j-1]、dp[i+1][j]、dp[i][j-1]
- 状态转移：
  - s[i] == s[j]：dp[i][j] = dp[i+1][j-1] + 2（两端匹配，长度+2）
  - s[i] != s[j]：dp[i][j] = max(dp[i+1][j], dp[i][j-1])（去掉左边或去掉右边取最大）
- 一维优化：dp[j] 滚动更新，用 tmp 保存每一轮 dp[i] 左下角的值

## 教训
- 看到"最长回文子序列（不要求连续）" → 二维 DP，i 倒序 j 正序
- 和 5/647 题对比：5/647 是回文子串（要求连续，中心扩展），516 是回文子序列（不要求连续，DP）
- 字符串 DP 的状态定义：dp[i][j] 表示子串 s[i:j+1] 的最优解