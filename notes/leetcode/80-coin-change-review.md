# LeetCode 322 零钱兑换（复习）

## 我的思路（45分钟）
- 前10分钟：想起一维 DP，但忘了这是完全背包问题，想不出状态转移方程
- 中间：看了答案想起转移方程 dp[j] = min(dp[j], dp[j - coins[i]] + 1)
- 写了20分钟没过：两个低级错误：
  1. +1 写成了 -1
  2. dp[0] 没有初始化为 0
- 后10分钟：对着答案检查，找到问题后通过
- 最后5分钟：看了 BFS 解法，但写得太晦涩没看懂

## 代码
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        
        return dp[-1] if dp[-1] != amount + 1 else -1
```

## 关键
- 完全背包：外层遍历硬币，内层正序遍历金额（正序因为硬币可重复使用）
- 状态转移：dp[j] = min(dp[j], dp[j - coin] + 1)
- 初始化：dp[0] = 0（凑0元需要0枚硬币），其余设为 amount + 1（无穷大）
- 无解判断：dp[amount] == amount + 1 则返回 -1

## 教训
- 第二次写还是错：dp[0] = 0 和 +1 是易错点，必须形成肌肉记忆
- 看到"最少硬币数" → 完全背包，dp[j] = min(dp[j], dp[j - coin] + 1)
- 完全背包 vs 0-1 背包：完全背包内层正序遍历（可重复取），0-1 背包内层倒序遍历（只能取一次）
- 背包问题还是不熟练，需要多加练习