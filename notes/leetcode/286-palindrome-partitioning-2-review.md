# LeetCode 132 分割回文串 II（复习）

## 我的思路（22分钟）
- 前10分钟基本写完；调试12分钟：更新最小切割数的条件范围写错、标记条件关系也写错
- 遍历顺序的本质理清：标记数组中要判断 s[i:j] 是否回文，需先知道 s[i+1:j-1] 是否回文，mk[i][j] 依赖 mk[i+1][j-1]，所以外层倒序；dp[i] 依赖 dp[j]（i > j），所以 dp 外层正序

## 代码
```python
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        mk = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or mk[i + 1][j - 1]):
                    mk[i][j] = True

        dp = [n + 1] * n
        for i in range(n):
            if mk[0][i]:
                dp[i] = 0
                continue
            for j in range(i):
                if mk[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
```

## 教训
- 复习： 22 分钟（55 → 22），两个 DP 的遍历顺序依据彻底理清，依赖决定方向：依赖小下标则正序，依赖大下标则倒序
- 调试 12 分钟仍花在条件范围上，说明核心已会、细节还要靠多写