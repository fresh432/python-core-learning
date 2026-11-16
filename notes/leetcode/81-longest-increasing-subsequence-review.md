# LeetCode 300 最长递增子序列（复习）

## 我的思路（8分钟）
- 前4分钟：DP 法
  - dp 数组全初始化为 1（每个元素单独成一个子序列时的长度）
  - 两层遍历，第一层 i 表示当前位置，第二层 j 在 [0, i) 内找小于 nums[i] 的元素，更新 dp[i] = max(dp[i], dp[j] + 1)
  - 全部遍历完后 dp 中的最大值即 LIS 长度
- 后4分钟：二分法
  - 初始化数组 g，g[k] 存"长度为 k+1 的子序列的尾部值"
  - 遍历原数组，用二分查找找合适的插入位置：位置小于 g 长度则替换对应下标的值（该长度下尾部可以优化得更小），等于 g 长度则扩大数组（没有优化空间说明 LIS 可以增长了）
  - 最后 g 的长度就是 LIS 长度

## 代码（DP 版）
```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

## 代码（二分版）
```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        g = []
        for num in nums:
            i, j = 0, len(g)
            while i < j:                # 第一个 >= num 的位置
                mid = (i + j) // 2
                if g[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            if j < len(g):
                g[j] = num              # 替换：该长度下尾部可优化得更小
            else:
                g.append(num)           # 拓展：LIS 增长
        return len(g)
```

## 教训
- 复习： 8 分钟双解法一遍过，DP（O(n²)）与二分（O(n log n)）都已掌握
- g 数组的语义是核心：g[k] = 长度为 k+1 的递增子序列的最小尾部值，"替换"就是在优化每个长度下的尾部，"追加"就是长度增长
- 和 354 对比：354 是套了二维外壳的 LIS，剥壳后就是本题的板子
