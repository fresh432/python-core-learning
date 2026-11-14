# LeetCode 312 戳气球（复习）

## 我的思路（17分钟）
- 前7分钟写完：
  - 数组初始化拼接首尾 1
  - 先遍历窗口大小，再遍历每个窗口的左边界 l（右边界 r = l + i）
  - 接着遍历窗口中每个元素 k，假定它是最后一个被戳破的气球，该区间价值 = dp[l][k] + nums[l]·nums[k]·nums[r] + dp[k][r]，每个窗口取最大值，最后返回完整区间的最大值
- 排查10分钟：始终不通过，最后发现是初始拼接数组的首尾 1 不小心填成了 0

## 代码
```python
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(2, n):          # 窗口大小
            for l in range(n - i):
                r = l + i
                for k in range(l + 1, r):   # k 为最后戳破的气球
                    dp[l][r] = max(dp[l][r],
                                   dp[l][k] + nums[l] * nums[k] * nums[r] + dp[k][r])
        return dp[0][n - 1]
```

## 教训
- 状态定义和转移已完全掌握（60 → 29 → 17 分钟），这次卡在把哨兵 1 写成 0 的笔误上 10 分钟
- 踩坑提醒：nums = [1] + nums + [1] 里的哨兵值参与乘法，写错数值静默出错、不报错。下次拼接后先打印一眼数组