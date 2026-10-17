# LeetCode 746 使用最小花费爬楼梯

## 我的思路（11分钟）
- 每层楼的花费由前两阶台阶的花费决定，状态转移方程：dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
- 踩坑：
  1. 初始可以从第0阶或第1阶开始，所以 dp[0] = dp[1] = 0，不需要给 dp[1] 做额外初始化
  2. cost 数组最后一个元素不是顶层，顶层是 n+1（dp 数组长度为 n+1）
- 解决后通过

## 代码
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
```

## 关键
- dp[i]：到达第 i 阶的最小花费
- 可以从第0或第1阶开始，所以 dp[0] = dp[1] = 0
- 状态转移：从 i-1 阶跨一步，或从 i-2 阶跨两步，取最小
- 顶层是 n（dp 数组下标 n），cost 数组下标到 n-1

## 教训
- 看到"爬楼梯最小花费" → DP，dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
- 和 70 题对比：70 是爬楼梯方案数（斐波那契），746 是爬楼梯最小花费（带权DP）

