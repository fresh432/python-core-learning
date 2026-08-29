# LeetCode 153 寻找旋转排序数组中的最小值

## 我的思路（45分钟）
- 前30分钟：想套用 33 题的思路，用左边值与中间值比较。逻辑是：若 nums[left] < nums[mid]，则左侧有序，用 ans 保存最小值，再把左边界收敛到 mid。但这样处理不了一些特殊情况（比如最小值恰好在左侧有序区间的边界，或数组未旋转的纯升序情况），逻辑越写越绕
- 后15分钟：换比较方向，改为比较 nums[mid] 和 nums[right]：
  - 若 nums[mid] > nums[right]：说明最小值在右半部分（旋转点在这里），left = mid + 1
  - 否则：最小值在左半部分（含 mid），right = mid
  - 最终 nums[left] 即为最小值

## 代码
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
```

## 关键
- 核心洞察：与右边界比较比与左边界比较更简洁
- nums[mid] > nums[right] → 旋转断点在右侧，最小值在 [mid+1, right]
- nums[mid] < nums[right] → 右侧有序，最小值在 [left, mid]
- nums[mid] == nums[right] 时（本题无重复元素），归入 else 即可
- 终止条件：left == right，返回 nums[left]
- 左闭右闭区间：right = len(nums) - 1

## 教训
- 看到"旋转数组找最小值" → 二分，与右边界比较，不要与左边界比较（特殊情况多）
- 为什么与右边界更好：旋转数组的最小值右侧一定是有序的，通过与最右值比较可以直接判断最小值在哪一侧
- 与 33 题对比：33 是找 target，需要判断哪侧有序再看 target 是否在范围内；153 是找最小值，只需要判断 mid 与 right 的大小关系即可，逻辑更简单

## 旋转数组二分系列对比
| 题目           | 目标       | 比较对象                             | 核心逻辑                       |
| :----------- | :------- | :------------------------------- | :------------------------- |
| 33 搜索旋转排序数组  | 找 target | `nums[left]` vs `nums[mid]`      | 哪侧有序，target 是否在有序区间        |
| **153 找最小值** | **找最小值** | **`nums[mid]` vs `nums[right]`** | **mid > right 则最小在右，否则在左** |
