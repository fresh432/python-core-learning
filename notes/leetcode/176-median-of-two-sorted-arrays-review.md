# LeetCode 4 寻找两个正序数组的中位数（二分查找法）

## 我的思路（120分钟）
- 前30分钟：自己尝试摸索切分边界位置，始终想不出来
- 中间80分钟：看了大量题解，大多只懂一点——知道要把两个数组各自切成左右两部分，且左边总元素数 = (m+n+1)//2，但始终没看懂边界如何制定
- 关键突破：看到一篇简洁清晰的题解，终于搞懂核心逻辑
- 后10分钟：根据理解写出代码，通过

## 核心思路
- 在较短的数组上进行二分切分，时间复杂度 O(log min(m, n))
- 设 nums1（长度 m）和 nums2（长度 n），保证 m <= n
- k = (m + n + 1) // 2：左边部分总共需要 k 个元素
- 在 nums1 的 [0, m] 范围内二分，切分点 i 表示 nums1 左边取 i 个元素
- 则 nums2 的切分点 j = k - i，左边取 j 个元素
- 切分正确条件：nums1_left_max <= nums2_right_min 且 nums2_left_max <= nums1_right_min
  - 即 nums1[i-1] <= nums2[j] 且 nums2[j-1] <= nums1[i]
- 若不满足则收敛边界：
  - nums1[i] < nums2[j-1]：nums1 左边最大值太小，i 需要右移（imin = i + 1）
  - nums1[i-1] > nums2[j]：nums1 左边最大值太大，i 需要左移（imax = i - 1）

## 代码
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是较短的数组，只在短数组上二分
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        k = (m + n + 1) // 2  # 左边部分的总元素个数
        
        while imin <= imax:
            i = (imin + imax) // 2  # nums1 左边取 i 个
            j = k - i               # nums2 左边取 j 个
            
            if i < m and nums1[i] < nums2[j - 1]:
                # nums1 左边最大值太小，i 右移
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # nums1 左边最大值太大，i 左移
                imax = i - 1
            else:
                # 找到正确切分，计算左边最大值
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])
                
                # 总长度为奇数，中位数就是左边最大值
                if (m + n) % 2 == 1:
                    return max_left
                
                # 总长度为偶数，还需计算右边最小值
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                
                return (max_left + min_right) / 2
```

## 关键
- 只在较短数组上二分：imin = 0, imax = m，保证 m <= n
- k = (m + n + 1) // 2：左边部分元素个数（奇数时左边多一个）
- 切分点：i（nums1 左边取 i 个），j = k - i（nums2 左边取 j 个）
- 收敛条件：
  - nums1[i] < nums2[j-1] → imin = i + 1（nums1 左边太小）
  - nums1[i-1] > nums2[j] → imax = i - 1（nums1 左边太大）
- 边界处理（切分点在数组边缘）：
  - i == 0：nums1 左边为空，max_left = nums2[j-1]
  - i == m：nums1 右边为空，min_right = nums2[j]
  - j == 0 和 j == n 同理
- 奇数：返回 max_left
- 偶数：返回 (max_left + min_right) / 2

## 教训
- 核心难点是切分点的边界处理，i 和 j 可能在数组的头部或尾部，需要4种边界情况的分类讨论
- 不要试图用完全二叉树的公式（index*2+1），那是完全二叉树的特性，普通有序数组不适用
- 和昨天的合并法对比：合并法 O(m+n) 直观但超标，二分切分法 O(log(min(m,n))) 是标准解
