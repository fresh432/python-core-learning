# LeetCode 34 在排序数组中查找元素的第一个和最后一个位置

## 我的思路（60分钟）
- 前20分钟：想先二分找到目标值，再向两边扩展找边界。但这样当目标值出现次数极多时，扩展过程会退化到 O(n)，不满足 O(log n) 要求
- 中间：看提示，核心洞察——分别二分查找左边界和右边界。用 target - 0.5 找左边界，target + 0.5 找右边界，这样二分天然停在目标值的两侧
- 后20分钟：大致写出，但因为边界偏移和特殊处理，又调试了20分钟才通过

## 代码
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 1:
            return [-1, -1]
        
        target_left = target - 0.5
        target_right = target + 0.5
        
        # 找左边界
        left, right = 0, n
        ans_left = 0
        while left < right:
            ans_left = (left + right) // 2
            if nums[ans_left] < target_left:
                left = ans_left + 1
            if nums[ans_left] > target_left:
                right = ans_left
        
        # 找右边界
        left, right = 0, n
        ans_right = 0
        while left < right:
            ans_right = (left + right) // 2
            if nums[ans_right] < target_right:
                left = ans_right + 1
            if nums[ans_right] > target_right:
                right = ans_right
        
        # 边界修正和校验
        if nums[ans_right] != target:
            ans_right -= 1
        if nums[ans_left] != target:
            ans_left += 1
        if nums[ans_right] != target:
            return [-1, -1]
        
        return [ans_left, ans_right]
```

## 关键
- 核心技巧：target - 0.5 和 target + 0.5 作为虚拟目标进行二分
  - 找 target - 0.5 的插入位置 → 目标值的左边界
  - 找 target + 0.5 的插入位置 → 目标值的右边界
- 左闭右开区间：right = n，while left < right
- 边界修正：二分结果可能偏移，需要校验并调整 ans_left 和 ans_right

## 教训
- 看到"排序数组中找目标值的左右边界" → 两次二分，用 target ± 0.5 技巧，O(log n)
- 不要先找到目标再向两边扩展（最坏 O(n)）
- 边界修正是易错点，最后要校验 nums[ans] == target
- 和 35 题对比：35 是找插入位置（一个边界），34 是找左右边界（两个边界）
