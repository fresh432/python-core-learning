# LeetCode 132 分割回文串 II

## 我的思路（55分钟）
- 前20分钟：只知道是 DP，想类似戳气球的窗口遍历，想不出状态转移方程
- 看提示要用 647 的方法；又花20分钟：dp[i] = min(dp[i], dp[j] + 1) 的转移想到了，但把"回文标记"和"状态转移"同时做，两者遍历顺序冲突（标记要外层倒序内层正序，转移要外层正序内层从 0 到 i），没写出来
- 看答案15分钟：要分开处理，先用 647 的标记法预处理所有窗口是否回文，再 DP：dp[i] 表示 s[:i+1] 的最小切割数
  - 外层 i 正序、内层 j 从 0 到 i，若 j+1~i 是回文则 dp[i] = min(dp[i], dp[j] + 1)
  - 剪枝：0~i 本身回文则 dp[i] = 0（一刀不切）直接跳过，结果返回 dp[-1]

## 代码
```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [n + 1] * n
        mk = [[False] * n for _ in range(n)]
        # 第一步：预处理回文标记（647 的方法，外层倒序）
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or mk[i + 1][j - 1]):
                    mk[i][j] = True

        # 第二步：最小切割 DP（外层正序）
        for i in range(n):
            if mk[0][i]:          # 整体回文，零刀
                dp[i] = 0
                continue
            for j in range(i):
                if mk[j + 1][i]:  # 后段回文，前段 j 的最小刀数 + 1
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]
```

## 教训
- 看到"最少切割使每段回文" → 回文标记矩阵预处理 + 一维 DP，两步分开走
- 踩坑核心：两个 DP 的遍历顺序冲突时必须拆开，标记矩阵外层要倒序（依赖 i+1），切割 DP 外层要正序（依赖 dp[j], j < i）
- 和 131 对比：131 是求所有分割方案（回溯），132 是求最少刀数（DP），同族问题，问"方案"用回溯、问"最值"用 DP