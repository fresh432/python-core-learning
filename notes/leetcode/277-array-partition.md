# LeetCode 561 数组拆分

## 我的思路（5分钟）
- 观察题目可知：要得到最大和，就要让最小的和最小的配成一对、最大的和最大的配成一对
- 先排序，然后两两取最小再累加返回即可

## 代码
```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(1, n, 2):
            ans += min(nums[i - 1], nums[i])
        return ans
```

## 教训
- 看到"2n 个数两两配对、每对取 min 求最大总和" → 排序取奇数位（或偶数位）求和