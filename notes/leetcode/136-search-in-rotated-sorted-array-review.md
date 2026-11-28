# LeetCode 33 搜索旋转排序数组（复习）

## 我的思路（4分钟）
- 二分查找：判断当前 mid 落入哪个有序区间，再根据 target 的落点决定边界收缩
- mid 在左侧数值更大的有序区间时：target 落在 [left, mid] 区间则收敛右边界，反之收敛左边界；mid 落在右侧数值更小的有序区间时同理

## 代码
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:               # mid 在左段
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:                                     # mid 在右段
                if nums[mid] < target <= nums[right - 1]:
                    left = mid + 1
                else:
                    right = mid
        return -1
```

## 教训
- 复习： 4 分钟一遍过，分支主轴（nums[mid] vs nums[left]）已熟悉
- 和 81 对比：无重复时不需要三值去重，其余框架完全一样，81 就是 33 + 去重补丁
