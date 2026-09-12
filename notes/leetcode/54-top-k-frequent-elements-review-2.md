# LeetCode 347 前 K 个高频元素（复习）

## 我的思路（40分钟）
- 前15分钟：想到桶排序，但误解了实现方式——以为要动态更新频率并实时转移元素在桶中的位置，且不知道桶该创建多大
- 中间5分钟：看答案，理解正确流程：
  1. 先用哈希表统计每个元素的频率
  2. 根据最大频数确定桶数组的大小（max_freq + 1）
  3. 把频率为 q 的元素放到 buckets[q] 中
  4. 从高频到低频遍历桶，取前 K 个
- 后5分钟：重写桶排序版本
- 最后15分钟：用堆排序写了一遍（手写 sift_down 建堆 + 弹出 K 次）

## 代码（桶排序）
```python
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        for num in nums:
            h[num] += 1
        
        h_max = max(h.values())
        buckets = [[] for _ in range(h_max + 1)]
        
        for num, q in h.items():
            buckets[q].append(num)
        
        ans = []
        for bucket in reversed(buckets):
            ans += bucket
            if len(ans) == k:
                return ans
        
        return ans
```

## 代码（堆排序）
```python
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        for num in nums:
            h[num] += 1
        
        n = len(h)
        heap = list(h.items())
        
        # 建堆（大顶堆，按频率）
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(heap, n, i)
        
        ans = []
        for i in range(k):
            heap[0], heap[n - 1] = heap[n - 1], heap[0]
            ans.append(heap[n - 1][0])
            n -= 1
            self.sift_down(heap, n, 0)
        
        return ans
    
    def sift_down(self, heap, size, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < size and heap[left][1] > heap[largest][1]:
            largest = left
        if right < size and heap[right][1] > heap[largest][1]:
            largest = right
        
        if largest != index:
            heap[largest], heap[index] = heap[index], heap[largest]
            self.sift_down(heap, size, largest)
```

## 关键
- 桶排序：时间 O(n)，空间 O(n)。先统计频率，再按频率分桶，从高频往低频取
- 堆排序：时间 O(n log k) 或 O(n + k log n)，空间 O(n)。手写 sift_down 建堆，弹出 K 次
- 桶的大小：max_freq + 1，下标即频率，天然有序

## 教训
- 看到"前 K 个高频" → 桶排序最直观（频率做下标），或堆排序（维护 K 大小堆）
- 桶排序不是动态更新：先完整统计频率，再一次性分桶
- 复习价值：桶排序和堆排序都要会写，桶排序代码更短，堆排序更通用

## Top K 问题方法对比
| 方法      | 时间复杂度      | 空间复杂度    | 适用场景           |
| :------ | :--------- | :------- | :------------- |
| 排序      | O(n log n) | O(1)     | 简单场景           |
| 堆排序     | O(n log k) | O(k)     | 数据流 / 内存受限     |
| 快速选择    | O(n) 期望    | O(log n) | 找第 K 大（215）    |
| **桶排序** | **O(n)**   | **O(n)** | **频率统计类（347）** |
