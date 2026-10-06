# LeetCode 162 寻找峰值

## 我的思路（25分钟）
- 前10分钟：要求 O(log n)，想到二分查找，但卡在边界收缩条件
- 中间5分钟：先写了直接遍历法（O(n)），在数组两端加 -inf 简化边界判断
- 后10分钟：继续想二分查找。从直接遍历中得到启发——只要一边相邻元素更小，该元素就是峰值。所以二分收缩条件：
  - nums[mid] < nums[mid + 1]：右边连续递增，右边必有峰值 → left = mid + 1
  - 否则：左边连续递减或先增后减，左边必有峰值 → right = mid
- 简单调试后通过

## 代码（直接遍历，O(n)）
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-inf] + nums + [-inf]
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i - 1
```

## 代码（二分查找，O(log n)）
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
```

## 关键
- 核心洞察：nums[mid] < nums[mid+1] 说明右边在上升，上升序列必有峰值
- 收缩方向：
  - nums[mid] < nums[mid+1] → 右边递增，峰值在右 → left = mid + 1
  - 否则 → 左边有峰值 → right = mid
- 返回 left：循环结束时 left == right，即为峰值下标

## 教训
- 看到"数组找峰值，要求 O(log n)" → 二分查找，比较 mid 和 mid+1
- 为什么有效：题目保证 nums[-1] 和 nums[n] 都是 -inf，所以数组中必然存在峰值