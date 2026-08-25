# LeetCode 53 最大子数组和

## 我的思路（35分钟）
- 前20分钟：想不出动态规划的状态转移方程，卡在如何定义状态和转移
- 后15分钟：想到问题关键，当前累加和如果小于0，就对后续没有贡献，应该放弃并重置。如果 current_sum < 0，重置为0，然后继续累加

## 代码
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        current_sum = nums[0]
        
        for i in range(1, n):
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[i]
            ans = max(ans, current_sum)
        
        return ans
```

## 关键
- 贪心/DP：current_sum 记录以当前元素结尾的最大子数组和
- 重置条件：current_sum < 0 时，对后续元素的累加只会"拖后腿"，所以重置为0
- 全局维护：ans = max(ans, current_sum)，记录遍历过程中的最大值

## 教训
- 看到"最大子数组和" → Kadane 算法，当前和为负就重置
- 初始化：ans = nums[0]，不要设为0（全负数时会错）
- 和 560 题对比：560 是前缀和+哈希表（求和为k的子数组个数），53 是贪心/DP（求最大子数组和）