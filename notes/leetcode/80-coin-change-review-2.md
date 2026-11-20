# LeetCode 322 零钱兑换（复习）

## 我的思路（30分钟）
- 前15分钟写完：外层遍历硬币、内层遍历面额，状态转移方程 dp[i] = min(dp[i - coin] + 1, dp[i])
- 但一直有问题，调试15分钟没找到；看了眼之前的提交记录才发现是初始化问题，除了 dp 全部初始化为 amount+1，还要把 dp[0] 初始化成 0，不然无法正常进行状态转移。改完后通过

## 代码
```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0                              # 关键初始化：凑 0 元需要 0 枚
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != amount + 1 else -1
```

## 教训
- 完全背包最值模板（硬币外层、正序内层）还记得，但初始化细节隔了几个月就忘了：dp[0] = 0 是状态转移的起点，漏掉后所有 dp[i] 都推不出来
- 和 518 对比：322 求最少硬币数（min 转移），518 求组合数（sum 转移），同一框架两种聚合，518 的初始化是 dp[0] = 1，别记混