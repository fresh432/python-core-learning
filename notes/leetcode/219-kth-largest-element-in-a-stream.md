# LeetCode 703 数据流中的第 K 大元素

## 我的思路（20分钟）
- 前10分钟：想到用堆，但之前都是手写堆实现，忘了 Python heapq 库的 API，也忘了手写堆的具体代码
- 后10分钟：看答案，用 heapq 实现——维护一个大小为 k 的小顶堆，堆顶就是第 K 大元素。初始化时将所有元素入堆，超过 k 就弹出堆顶。add 时新元素入堆，超过 k 弹出，返回堆顶

## 代码
```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
```

## 关键
- 小顶堆：堆顶是第 K 大的元素（堆中有 k 个最大的元素，堆顶最小）
- heapq.heappush / heappop：Python 标准库的最小堆实现
- 空间 O(k)，每次 add 时间 O(log k)

## 教训
- 看到"动态维护第 K 大/小" → 大小为 K 的堆
- heapq 是 Python 内置最小堆，要熟练掌握
- 和 215 题对比：215 是数组中找第 K 大（快排/堆），703 是数据流中动态维护（固定大小堆）

