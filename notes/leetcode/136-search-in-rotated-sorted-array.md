# LeetCode 33 搜索旋转排序数组

## 我的思路（30分钟）
- 前10分钟：想先找到旋转点（最小值位置），把数组分成两段有序数组，再分别二分查找。但这样需要 O(n) 找旋转点或两次二分，不满足题目要求的 O(log n)
- 后20分钟：想到核心优化——直接二分，每次判断 mid 所在的那一半是否有序。如果有序，判断 target 是否在该有序区间内；否则去另一半查找。一次二分即可 O(log n)

## 代码
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[mid]:
                # 左半部分有序
                if nums[left] <= target and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                # 右半部分有序
                if nums[mid] < target and target <= nums[right - 1]:
                    left = mid + 1
                else:
                    right = mid
        
        return -1
```

## 关键
- 核心洞察：旋转排序数组中，mid 所在的一侧必有一侧是有序的
- 判断哪侧有序：nums[left] < nums[mid] → 左半部分有序；否则右半部分有序
- 在有序侧判断 target 是否在范围内：若在则收缩到该侧，否则去另一侧

## 教训
- 看到"旋转排序数组中查找" → 不要先找旋转点再二分，直接在二分过程中判断哪侧有序
- 核心判断逻辑：哪侧有序就先判断 target 是否落在该侧范围内
- 边界条件：nums[left] <= target < nums[mid]（左有序）或 nums[mid] < target <= nums[right-1]（右有序），注意等号
- 和 704 题对比：704 是普通二分（纯有序数组），33 是旋转数组二分（需要额外判断哪侧有序）

## 二分查找变体对比
| 题目              | 数组特征      | 核心技巧         | 额外判断                |
| :-------------- | :-------- | :----------- | :------------------ |
| 704 二分查找        | 纯升序       | 标准二分         | 无                   |
| 35 搜索插入位置       | 纯升序       | 左闭右开，返回 left | 无                   |
| **33 搜索旋转排序数组** | **旋转后升序** | **判断哪侧有序**   | **target 是否在有序区间内** |

