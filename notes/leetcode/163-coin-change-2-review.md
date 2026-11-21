# LeetCode 518 零钱兑换 II（复习）

## 我的思路（25分钟）
- 外层遍历硬币、内层遍历金额，这样算的是组合数；内外层反过来就是排列数
- 初始化：dp 全为 0、dp[0] 初始化为 1（0 元的组合方式只有"不放硬币"这一种）
- 状态转移方程想很久才想起来：每个位置的组合数 = 选了这枚硬币的组合数 + 没选这枚硬币的组合数之和，即 dp[i] += dp[i - coin]

## 代码
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:                     # 外层硬币 → 组合数
            for i in range(coin, amount + 1):  # 内层金额 → 正序
                dp[i] += dp[i - coin]
        return dp[-1]
```

## 教训
- 转移方程的语义要记牢：dp[i] += dp[i-coin] 的含义是"已选 coin 凑成 i-coin 的方案数"，累加所有 coin 即得总数
- 初始化对比：322 求最少硬币（dp[0]=0、其余 amount+1），518 求组合数（dp[0]=1、其余 0），初始值就是答案的"空集语义"