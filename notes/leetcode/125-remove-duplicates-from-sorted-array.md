# LeetCode 26 删除有序数组中的重复项

## 我的思路（20分钟）
- 前10分钟：用双指针遍历，遇到重复就 pop，但 pop 操作时间复杂度 O(n)，整体变成 O(n²)
- 后10分钟：想到更优方法——快慢指针原地覆盖，遇到重复跳过，遇到不同就把快指针元素覆盖到慢指针后一个位置

## 代码
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
```

## 关键
- 快慢指针：i 快指针遍历数组，j 慢指针指向最后一个不重复元素的位置
- nums[i] != nums[j] 时：j += 1，然后 nums[j] = nums[i]，原地覆盖
- 返回 j + 1（不重复元素的个数）
- 空间 O(1)，时间 O(n)

## 教训
- 看到"有序数组去重/原地修改" → 快慢指针，不要用 pop 或新建数组
- j 从 0 开始，第一个元素天然不重复，最后返回 j + 1