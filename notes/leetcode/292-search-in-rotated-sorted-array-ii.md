# LeetCode 81 搜索旋转排序数组 II

## 我的思路（55分钟）
- 前20分钟：想到二分，先判断中点落在哪边的有序部分，再按落点收敛边界；但左右端点可能重复，导致无法正常判断哪侧有序
- 想先把两侧相同元素收敛边界，只比较左右两边元素是否相等，还是过不了
- 看提示：收敛旋转处两侧边界还要带上 mid 一起判断，只有当 mid、left、right 三者都相同时才能整体收缩一位。之后用 33 题的二分框架
- 但又花 25 分钟调试边界：一开始按 mid 值与 target 比较来分支，写到后面绕晕了；重构改成按左边界值与 mid 值分支，nums[mid] ≥ nums[left] 说明 mid 落在左侧数值更大的非递减序列，再判断 target 是否落在 [left, mid] 区间内收缩；mid 落右侧同理处理。查找中没找到则返回最后指针处的值是否等于 target

## 代码
```python
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return nums[0] == target
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 三者全同才收缩：只比较两端不够，mid 可能正是"伪装"的重复值
            while nums[mid] == nums[left] == nums[right] and left < right:
                right -= 1
                left += 1
            if nums[mid] >= nums[left]:              # mid 在左段（大值升序）
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:                                    # mid 在右段（小值升序）
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return nums[left] == target
```

## 关键
- 与 33 题的唯一差别：元素可重复。去重条件必须是 nums[mid] == nums[left] == nums[right] 三者同时相等，只比较两端会在"整段同值"时误判有序侧
- 分支主轴：先看 nums[mid] 与 nums[left] 判断 mid 落在哪段有序序列，再看 target 是否在该段区间内
- 循环结束返回 nums[left] == target（循环里可能把 target 挤出去）

## 教训
- 看到"旋转排序数组含重复、搜索" → 33 框架 + 三值相等去重
- 自己卡死的点：只比较 left/right 相等就去收缩，mid 本身可能就是那个"伪装成有序段"的重复值，去重判定必须包含 mid
- 调试 25 分钟的教训：按"mid 与 target 比较"分支在含重复时极易绕晕；旋转数组二分的分支主轴永远是"mid 与 left 比较判落侧"，target 只是二级判断