# LeetCode 213 打家劫舍 II

## 我的思路（45分钟）
- 前30分钟：想过把数组拼接成环形来处理，但感觉逻辑有问题
- 中间5分钟：看答案，核心洞察——环形问题拆成两个线性问题：选头就不能选尾，所以分别求「不偷第一家」和「不偷最后一家」两种情况的最大值，再取 max
- 后10分钟：封装打家劫舍 I 的函数，分别对 nums[1:] 和 nums[:-1] 调用，取较大值

## 代码
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]
        nums2 = nums[:-1]
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        def func(nums):
            n = len(nums)
            dp = [0] * (n + 1)
            dp[1] = nums[0]
            dp[2] = max(dp[1], dp[0] + nums[1])
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
            return dp[-1]
        
        return max(func(nums1), func(nums2))
```

## 关键
- 环形拆线性：max(rob(nums[1:]), rob(nums[:-1]))
  - 偷第一家 → 不能偷最后一家 → 问题变为 nums[:-1]
  - 偷最后一家 → 不能偷第一家 → 问题变为 nums[1:]
  - 两者都不偷 → 被上述两种情况覆盖
- 边界处理：len(nums) == 1 直接返回，len(nums) == 2 取 max
- 状态转移：同 198 题（打家劫舍 I）——dp[i] = max(偷当前 + dp[i-2], 不偷当前 + dp[i-1])

## 教训
- 看到"环形数组的相邻限制" → 拆成两个线性子问题，不要试图在环上直接 DP
- 环形问题的通用套路：断开环，分别处理「包含起点不含终点」和「包含终点不含起点」
- 和 198 题对比：198 是线性，213 是环形，核心 DP 逻辑完全一致，只是多了拆分步骤