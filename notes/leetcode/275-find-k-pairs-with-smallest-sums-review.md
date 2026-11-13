# LeetCode 373 查找和最小的 K 对数字（复习）

## 我的思路（8分钟）
- 将 (sum, i, j) 三元组入堆，初始化时仅加入 (0, 0) 坐标的三元组
- 遍历 k 轮：每次弹出堆顶元素加入 ans，再将弹出元素的右邻（i, j+1）和下邻（i+1, j）入堆
- 下邻仅在弹出元素的下标 j 为 0 时才添加，用这个规则代替 visited 数组保证无重复三元组入堆

## 代码
```python
import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        h = [(nums1[0] + nums2[0], 0, 0)]
        n1, n2 = len(nums1), len(nums2)
        ans = []
        for _ in range(k):
            _, i, j = heapq.heappop(h)
            ans.append([nums1[i], nums2[j]])
            if i == 0 and j + 1 < n2:    # 列首（j==0）才向右开新行，防重
                heapq.heappush(h, (nums1[0] + nums2[j + 1], 0, j + 1))
            if i + 1 < n1:               # 向下邻必入堆
                heapq.heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        return ans
```

## 教训
- 复习： 8 分钟一遍过（首次 50 分钟），堆 + 防重入堆规则已掌握
- 与首次写法互为转置：上次是"右邻常入、j==0 时 i+1 入"，这次用对称的"下邻常入、i==0 时 j+1 入"，两种防重规则等价，选顺手的记
