# LeetCode 283 移动零

## 思路
快慢指针：快指针找非零，慢指针写入位置。

## 代码
```python
def moveZeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
```
## 关键
- 交换而非覆盖，保留非零元素顺序
- 快指针遍历，慢指针只在非零时前进