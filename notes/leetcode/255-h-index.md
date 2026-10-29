# LeetCode 274 H 指数

## 我的思路（30分钟）
- 前20分钟：排序后遍历找最靠后且满足"剩余文章数 ≥ 当前引用数"的位置，再加条件判断处理特殊情况，写得太复杂，花5分钟重构后通过
- 后5分钟：看答案的其他解法——二分代替遍历找边界（有排序约束，复杂度一致）；计数排序：数组存调用次数对应的书数，答案不超过 n，大于 n 次调用的都存到 n 位置，倒序遍历累计总数，总数 ≥ 当前调用次数则返回，O(n) 时间 O(n) 空间

## 代码（降序 + 遍历，最简）
```python
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        for i, c in enumerate(citations):
            if c <= i:
                return i
        return n
```

## 代码（计数排序，O(n)）
```python
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)

        for c in citations:
            cnt[min(c, n)] += 1

        ans = 0
        for i in range(n, -1, -1):
            ans += cnt[i]
            if ans >= i:
                return i
```

## 代码（降序 + 二分）
```python
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if citations[mid] > mid:
                left = mid + 1
            else:
                right = mid
        return left
```

## 关键
- H 指数定义：有 h 篇文章引用数 ≥ h。降序排序后，第一个满足 c ≤ i 的位置 i 就是答案
- 计数排序：cnt[min(c, n)] 统计，倒序累加 ans，ans ≥ i 时返回 i——答案上界为 n，所以引用数超 n 的都归到 n

## 教训
- 看到"求 H 指数" → 降序排序找边界，或计数排序 O(n)
- 三种解法对比：降序+遍历最简、降序+二分只是换查找方式、计数排序免排序但费空间——值域与答案同界时优先考虑计数排序