# LeetCode 1046 最后一块石头的重量

## 我的思路（9分钟）
- 用 heapq 库实现大顶堆——Python 的 heapq 是最小堆，所以入堆时取负数，这样堆顶就是最大的石头
- 每次弹出两个最大的（最负的），相减后将结果入堆
- 最后如果堆中还有值，取负数返回；否则返回 0

## 代码
```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, x - y)
        
        return -heap[0] if heap else 0
```

## 关键
- Python heapq 是最小堆，用大顶堆需要取负数
- 每次取两个最大的相减，结果入堆
- 终止：堆中只剩一个或零个元素

## 教训
- 看到"每次取最大/最小的两个" → 堆