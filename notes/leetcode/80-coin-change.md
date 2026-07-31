# LeetCode 322 零钱兑换

## 我的思路（90分钟）
- 前10分钟：想到递归 + 倒序遍历，但没实现出来
- 中间60分钟：看题解，看了好几篇都没太懂，原理写得比较绕
- 后20分钟：找到一篇通俗易懂的题解，理解后写出代码

## 代码
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [(amount + 1)] * (amount + 1)  # 初始化为不可能的大值
        dp[0] = 0                            # 凑成0元需要0个硬币
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
```

## 关键
- 状态定义：dp[i] = 凑成金额 i 所需的最少硬币数
- 状态转移：dp[i] = min(dp[i], dp[i-coin] + 1)
  - 不选当前硬币：dp[i]（保持原值）
  - 选当前硬币：dp[i-coin] + 1（凑成 i-coin 的硬币数 + 1）
- 初始化：dp[0] = 0，其余设为 amount+1（表示不可能）
- 外层循环硬币，内层循环金额：完全背包问题，每种硬币无限使用

## 教训
- 看到"最少硬币数/最小数量" → 完全背包 DP
- 完全背包 vs 0-1 背包：外层循环是物品，内层循环从小到大（可重复选）
- 和 39 题（组合总和）对比：

| 题目           | 方法     | 目标         |
| ------------ | ------ | ---------- |
| 39 组合总和      | 回溯     | 找出所有组合     |
| **322 零钱兑换** | **DP** | **求最少硬币数** |

- 回溯适合"找出所有解"，DP 适合"求最值"