# LeetCode 392 判断子序列（DP 版）

## 我的思路（30分钟）
- 前15分钟：想用 DP，想保留 t 中匹配 s 长度的状态，最后和 s 长度比较——有 bug
- 后15分钟：调整思路，改为保存子序列的组合数，最后判断是否 > 0

## 代码
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 == 0:
            return True
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n2 + 1):
            dp[0][i] = 1  # s为空串，t的前i个字符都能匹配
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i - 1] == t[j - 1] and i <= j:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        
        return True if dp[n1][n2] > 0 else False
```

## 关键
- 状态定义：dp[i][j] = s[0:i] 作为 t[0:j] 的子序列的方案数
- 初始化：dp[0][i] = 1（空串是任何串的子序列）
- 状态转移：
  - 字符相等：dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
  - 字符不等：dp[i][j] = dp[i][j-1]
- 最后判断 dp[n1][n2] > 0

## 教训
- 392 题之前用双指针做过（10分钟），这次用 DP 反而更复杂
- DP 版适合批量查询场景（多个 s 查询同一个 t），可以预处理
- 和 115 题对比：

| 题目            | 目标         | 返回值                  |
| ------------- | ---------- | -------------------- |
| 115 不同子序列     | 求个数        | `dp[n1][n2]`         |
| **392 判断子序列** | **判断是否存在** | **`dp[n1][n2] > 0`** |
