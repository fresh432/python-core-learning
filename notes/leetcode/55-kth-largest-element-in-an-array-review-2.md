# LeetCode 215 数组中的第 K 个最大元素（复习）

## 我的思路（23分钟）
- 前3分钟：堆解法，用小顶堆，遍历数组入堆，堆中只保留 k 个元素、多了弹堆顶；遍历完堆顶即第 K 大
- 后15分钟尝试快速选择：只记得随机选基数、按基数把其余数字划分成比它大和小的两部分，后面想不出来
- 看答案5分钟：还要用递归，按基数划分到 big、small、equal 三个数组，通过各数组元素个数与 k 的比较判断下一步去哪个数组递归划分，不断递归直到定位第 K 大

## 代码（堆解法）
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)
```

## 代码（快速选择）
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            big, small, equal = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):                          # 第k大在 big 里
                return quick_select(big, k)
            if len(nums) - len(small) < k:             # 第k大在 small 里
                return quick_select(small, k - len(nums) + len(small))
            return pivot                               # 在 equal 里
        return quick_select(nums, k)
```

## 教训
- 堆解法 3 分钟一遍过，快速选择只记得"随机 pivot + 划分"，三路划分（big/small/equal）后的 k 定位逻辑忘了，平均 O(n) 的分治细节是薄弱点