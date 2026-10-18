# LeetCode 973 最接近原点的 K 个点

## 我的思路（7分钟）
- 求"前 K 个" → 第一时间想到堆
- 遍历坐标数组，算每个坐标到原点的欧几里得距离。不需要完全开方，只算 i² + j² 的平方和即可
- 将每个距离与对应坐标存入小顶堆，最后从堆顶弹出 k 个坐标即为答案

## 代码
```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i, j in points:
            dist = i * i + j * j
            heapq.heappush(heap, (dist, [i, j]))
        for _ in range(k):
            _, res = heapq.heappop(heap)
            ans.append(res)
        return ans
```

## 关键
- 距离只算平方和 i² + j²，不用开方（避免浮点误差且更快）
- 小顶堆：堆顶是距离最小的点，弹 k 次即前 K 近
- 另一种写法：维护大小为 k 的大顶堆（存"目前最远的前 k 个"），空间 O(k)、时间 O(n log k)

## 教训
- 看到"前 K 个最近/最小" → 堆（小顶堆全入再弹 k 次，或大顶堆定长 k）
- 和 703 题对比：703 是数据流动态维护第 K 大（小顶堆定长），973 是静态数组求前 K 近（小顶堆弹 k 次）
- 距离比较类问题统一套路：平方和代替开方

