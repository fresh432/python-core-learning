# LeetCode 35 搜索插入位置

## 教训
- 704和35可以用同一模板，循环条件都是 `left <= right`
- 之前误以为35要用 `left < right`，导致边界错误
- 最后返回 `left` 就是插入位置

## 模板
```python
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left &lt;= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] &lt; target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left