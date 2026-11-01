# LeetCode 312 戳气球

## 我的思路（60分钟）
- 前25分钟：毫无头绪
- 看提示"区间 DP"，尝试15分钟还是想不出来
- 看答案20分钟：dp[l][r] 假设区间 (l, r) 内最后戳破的气球下标是 k，则该区间价值 = dp[l][k] + dp[k][r] + nums[l]·nums[k]·nums[r]，问题拆成两个更小的子区间；从最小窗口开始求，逐步扩大窗口
- 感觉答案有些部分没看太懂，跟着答案写了一遍

## 代码
```python
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(3, n + 1):          # 窗口长度从 3 开始
            for l in range(0, n - i + 1):
                r = l + i - 1
                for k in range(l + 1, r):  # k 是 (l, r) 内最后戳破的气球
                    dp[l][r] = max(dp[l][r],
                                   dp[l][k] + dp[k][r] + nums[l] * nums[k] * nums[r])
        return dp[0][n - 1]
```

## 关键
- 首尾补 1 作为虚拟边界；dp[l][r] 表示开区间 (l, r) 内戳破所有气球的最大得分
- k 是区间内最后戳破的气球：戳它时左右邻居就是 nums[l] 和 nums[r]，得分 nums[l]·nums[k]·nums[r]
- 遍历顺序：按窗口长度从小到大（dp[l][r] 依赖 dp[l][k]、dp[k][r]，k 严格在区间内部）

## 教训
- 看到"区间内操作求最值、最后一步决定得分" → 区间 DP，状态定义抓"最后一个被操作的元素"
- 和 516 题对比：516 是回文子序列（端点匹配转移），312 是"最后操作者"型——区间 DP 的状态要么看端点、要么看最后操作，想不出时从这两个角度试
