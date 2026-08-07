# LeetCode 416 分割等和子集

## 我的思路（90分钟）
- 前30分钟：完全没思路，不知道从何下手，试图暴力枚举子集但意识到复杂度爆炸
- 中间40分钟：看答案，虽然没完全看懂背包问题的完整推导，但抓住了两个关键线索——"总和的一半"和"一维布尔数组"
- 后20分钟：自己琢磨，把问题抽象成"能否从数组中选一些数，使其和恰好等于 sum/2"，顺着这个思路写出代码并通过

## 代码
```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2
        dp = [True] + [False] * s
        
        for num in nums:
            if num > s:
                return False
            for i in range(s, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[-1]
```

## 关键
- 问题转化：数组总和为 s，若 s 为奇数直接返回 False；目标是能否凑出 s/2
- 状态定义：dp[i] = 能否从数组中选出若干个数，使其和恰好为 i
- 状态转移：dp[i] = dp[i] or dp[i - num]（不选当前数 / 选当前数）
- 初始化：dp[0] = True（和为 0 不需要选任何数），其余为 False
- 内层倒序：range(s, num-1, -1)，确保每个 num 只被使用一次（0-1 背包）

## 教训
- 看到"将数组分成两个和相等的子集" → 先算总和，奇数直接 False，转化为 0-1 背包判定问题
- 0-1 背包 vs 完全背包的核心区别在遍历方向：0-1 背包内层倒序（每个物品只能用一次），完全背包内层正序（可重复使用）
- 本题是0-1 背包的判定版（dp 存布尔值），下一题 494 是0-1 背包的计数版（dp 存整数）
- num > s 时直接返回 False 是剪枝优化
