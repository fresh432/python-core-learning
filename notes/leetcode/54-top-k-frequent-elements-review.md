# LeetCode 347 前 K 个高频元素（堆排序版）

## 我的思路（60分钟）
1. 前40分钟：理解堆排序概念、堆的定义（完全二叉树、父节点大于子节点）、以及如何用堆解决"前K高频"
2. 后20分钟：实现和调试。卡在 sift_down 最后一段——largest 和 index 下标的元素忘记交换

## 代码（手动实现大顶堆）
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = list(count.items())  # [(元素, 频率), ...]
        n = len(heap)
        
        # 建堆：从最后一个非叶子节点开始下沉
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(heap, n, i)
        
        ans = []
        # 提取前 K 个最大元素（按频率）
        for j in range(k):
            heap[0], heap[n - 1] = heap[n - 1], heap[0]
            ans.append(heap[n - 1][0])  # 取元素值
            n -= 1
            self.sift_down(heap, n, 0)
        
        return ans
    
    def sift_down(self, heap_data, size, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        
        # 和左子节点比较（按频率）
        if left < size and heap_data[left][1] > heap_data[largest][1]:
            largest = left
        # 和右子节点比较（按频率）
        if right < size and heap_data[right][1] > heap_data[largest][1]:
            largest = right
        
        if largest != index:
            heap_data[index], heap_data[largest] = heap_data[largest], heap_data[index]
            self.sift_down(heap_data, size, largest)
```

## 关键
- 堆的本质：完全二叉树，用数组存储，下标 i 的左右子节点为 2i+1 和 2i+2
- 建堆：从最后一个非叶子节点 n//2 - 1 倒序下沉到根
- 提取最大值：堆顶（heap[0]）和末尾交换，缩小堆范围，再下沉新堆顶
- 本题特殊：堆中存 (元素, 频率)，比较按频率（[1]）

## 教训
- sift_down 最后必须交换 heap_data[index] 和 heap_data[largest]，然后递归下沉
- 手动实现堆排序比 heapq 复杂得多，实际开发优先用 heapq.nlargest()
- 和 347 桶排序版对比：

| 方法      | 时间         | 空间   | 适用场景          |
| ------- | ---------- | ---- | ------------- |
| 桶排序     | O(n)       | O(n) | 频率范围有限        |
| **堆排序** | O(n log n) | O(n) | 通用，K 远小于 n 时优 |

- 看到"前 K 个" → 先想堆，但桶排序在特定场景更优