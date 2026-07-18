# LeetCode 347 前 K 个高频元素

## 我的思路（50分钟）
1. 前30分钟：没有思路，不知道如何在 O(n) 或 O(n log n) 内找到前 K 高频
2. 后20分钟：看答案理解了桶排序方法，但堆排序（优先队列）方法没看懂

## 代码（桶排序）
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        for i in nums:
            h[i] += 1
        
        max_h = max(h.values())
        
        # 桶：下标=频率，值=具有该频率的元素列表
        buckets = [[] for _ in range(max_h + 1)]
        for x, c in h.items():
            buckets[c].append(x)
        
        ans = []
        for bucket in reversed(buckets):
            if bucket:
                ans += bucket
            if len(ans) >= k:
                return ans[:k]
        
        return ans
```

## 关键
- 第一步：哈希表统计频率 h[num] = count
- 第二步：桶排序——以频率为下标，把元素放入对应桶
- 第三步：从高频到低频遍历桶，收集前 K 个
- 时间复杂度 O(n)，空间复杂度 O(n)

## 和堆排序的对比
| 方法      | 核心思想         | 时间复杂度      | 空间复杂度 |
| ------- | ------------ | ---------- | ----- |
| **桶排序** | 频率范围有限，直接分桶  | O(n)       | O(n)  |
| 堆排序     | 维护大小为 K 的小顶堆 | O(n log K) | O(K)  |

## 教训
- 看到"前 K 个" → 先想堆排序（优先队列），但本题频率有上界，桶排序更优
- 桶排序的适用场景：值的范围有限且已知，本题频率最大为 n
- 堆排序没看懂，后续需要补：Python 的 heapq 模块，小顶堆维护前 K 大
- 和 350 题（两个数组的交集 II）都用到了 Counter，但 347 需要排序/分桶，350 只需匹配
- 哈希表 + 桶排序 = "计数 + 按计数分桶" 的经典组合

