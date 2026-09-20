# LeetCode 4 寻找两个正序数组的中位数

## 我的思路（60分钟）
- 前30分钟：想到合并两个有序数组（类似 21 题思路），提前算出中位数的下标 target，双指针合并到 target 位置时停止，然后判断奇偶返回中位数。但时间复杂度 O(m+n)，不满足要求的 O(log(m+n))
- 后30分钟：看参考答案的二分查找法，但有点看不懂，改天再补二分查找法

## 代码（合并法，非最优）
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        count = 0
        total = m + n
        
        if total % 2 == 1:
            target = (total - 1) // 2
            flag = 1  # 奇数
        else:
            target = total // 2
            flag = 0  # 偶数
        
        nums3 = []
        i, j = 0, 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
            count += 1
            if count > target:
                if flag == 1:
                    return nums3[target]
                else:
                    return (nums3[target] + nums3[target - 1]) / 2
        
        # 处理剩余元素
        if i == m:
            while count <= target:
                nums3.append(nums2[j])
                j += 1
                count += 1
        elif j == n:
            while count <= target:
                nums3.append(nums1[i])
                i += 1
                count += 1
        
        if flag == 1:
            return nums3[target]
        else:
            return (nums3[target] + nums3[target - 1]) / 2
```

## 关键
- 合并法：双指针按序合并，合并到 target 位置即可停止，不需要合并完
- 奇数：target = (m+n-1)//2，返回 nums3[target]
- 偶数：target = (m+n)//2，返回 (nums3[target] + nums3[target-1]) / 2

## 教训
- 看到"两个有序数组的中位数" → 第一反应应该是二分查找O(log(m+n))，而不是合并O(m+n)
- 二分查找法的核心：在较短的数组中二分，找到一个分割点使得左右两部分元素个数相等且左边最大值 <= 右边最小值
- 和 88 题对比：88 是合并到 nums1（从后往前 O(1) 空间），4 是找中位数，合并法 O(m+n) 或二分 O(log(m+n))