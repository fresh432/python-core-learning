# LeetCode 215 数组中的第K个最大元素（复习）

## 我的思路（60分钟）
- 前10分钟：想到堆排序和快速排序两种方法，觉得堆排序太复杂，决定用快排
- 中间20分钟：卡壳在递归逻辑，以为要把左右两边都完全排序，想不出如何只排一边就找到第 K 大
- 中间10分钟：看答案，理解核心——每次 partition 分三块（大于 pivot、小于 pivot、等于 pivot），然后根据 len(big) 与 k 的大小关系决定继续排哪一边，不需要全排序
- 后10分钟：自己写出快速选择版本
- 最后10分钟：重新理解堆排序写法（第一次做用的堆排序，这次快排写出来了，堆排序没独立写出来）

## 代码（快速选择）
```python
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            
            if k <= len(big):
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                return quick_select(small, k - len(nums) + len(small))
            
            return pivot
        
        return quick_select(nums, k)
```

## 关键
- 快速选择：基于快排 partition 思想，但只递归需要的那一边
- 三分区：big（> pivot）、equal（= pivot）、small（< pivot）
- 递归方向：
  - k <= len(big)：第 K 大在 big 中，递归 big
  - k > len(big) + len(equal)：第 K 大在 small 中，递归 small（调整 k）
  - 否则：pivot 就是第 K 大
- 随机 pivot：避免最坏情况 O(n²)，期望时间 O(n)

## 教训
- 不要试图完全排序左右两边，根据 k 和分区大小决定递归方向
- 复习价值：快排和堆排序都要掌握，快排实现更简单，堆排序空间更优
