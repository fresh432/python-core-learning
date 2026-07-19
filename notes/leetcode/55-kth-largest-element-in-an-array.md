# LeetCode 215 数组中的第K个最大元素

## 我的思路（30分钟）
- 前5分钟：写出第一版——直接排序取倒数第 K 个，简洁通过
- 后25分钟：觉得应该用堆排序实现，手动写大顶堆。结果时间 793ms，反而比排序更慢

## 代码
# 第一版（排序，5分钟）
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = sorted(nums)
        n = len(nums)
        return ans[n - k]
```

# 第二版（堆排序，25分钟）
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 建堆
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(nums, n, i)
        
        # 提取 k-1 次最大值，堆顶就是第 K 大
        for j in range(k - 1):
            nums[0], nums[n - 1] = nums[n - 1], nums[0]
            n -= 1
            self.sift_down(nums, n, 0)
        
        return nums[0]
    
    def sift_down(self, heap, size, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < size and heap[largest] < heap[left]:
            largest = left
        if right < size and heap[largest] < heap[right]:
            largest = right
        
        if largest != index:
            heap[largest], heap[index] = heap[index], heap[largest]
            self.sift_down(heap, size, largest)
```

## 关键
- 第 K 大 = 排序后倒数第 K 个 = sorted(nums)[n-k]
- 堆排序思路：建大顶堆后，提取 k-1 次最大值，堆顶就是第 K 大
- 堆排序时间 O(n log n)，排序也是 O(n log n)，但常数因子堆排序更大

## 教训
- 不要过度追求"高级"算法：排序法 61ms（击败63.77%），堆排序 793ms（击败5.01%）
- Python 的 sorted() 是 Timsort，高度优化，手动堆排序很难超越
- 面试时可以先写排序法，再讨论堆排序的优化空间（K 很小时用小顶堆维护前 K，O(n log K)）
- 和 347 题对比：

| 题目         | 排序法        | 堆排序优势场景          |
| ---------- | ---------- | ---------------- |
| 347 前 K 高频 | O(n log n) | K 很小时 O(n log K) |
| 215 第 K 大  | O(n log n) | 数据流/不能全排序时       |

- 手动实现堆排序是练基本功，但实际用 heapq 模块