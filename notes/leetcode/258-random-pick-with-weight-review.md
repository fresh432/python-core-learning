# LeetCode 528 按权重随机选择（复习）

## 我的思路（12分钟）
- 把每个下标的权重转换为区间，区间用前缀和构成
- 随机数范围取 [0, 总权重)，二分查找比较随机数与区间边界进行收缩，返回对应下标
- 二分边界调试了几分钟

## 代码
```python
class Solution:

    def __init__(self, w: list[int]):
        self.n = len(w)
        self.ans = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.ans[i] = self.ans[i - 1] + w[i - 1]
        self.total = sum(w)
    
    def pickIndex(self) -> int:
        target = random.randint(0, self.total - 1)
        left, right = 1, self.n
        while left < right:
            mid = (left + right) // 2
            if self.ans[mid] > target:
                right = mid
            else:
                left = mid + 1

        return right - 1
```

## 教训
- 看到"按权重随机选择" → 前缀和 + 二分，O(log n) 每次
- 二分边界仍是薄弱点：ans[mid] <= target 收缩左边界、返回 right-1（对应数组下标），这类"第一个大于 target"的二分要多练