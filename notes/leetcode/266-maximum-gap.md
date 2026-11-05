# LeetCode 164 最大间距

## 我的思路（60分钟）
- 前20分钟：没有任何线性排序思路
- 中间30分钟：突然想到用单调栈存倒序，每个递减栈存入另一个桶中，再遍历扫栈顶获取所有栈中的最小值算差值——写完超时，因为忽略了每次扫栈找最小值要花 O(m·n)
- 看答案10分钟：也是分桶，但先用最大值和最小值求平均间距，得出最大间距 d 的下界 d = (max-min+n-2)//(n-1)，按这个间距分桶
  - 每个桶只存该间距内的最大值和最小值，桶内两值之差不会大于 d，所以答案一定在相邻桶之间（前桶 max 与后桶 min 之差）
  - 桶号 = (num - 全局min) // d
  - 最后遍历所有桶，用前桶 max 与当前桶 min 求差、ans 维护最大

## 代码
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        m = min(nums)
        M = max(nums)
        if M - m <= 1:
            return M - m

        n = len(nums)
        ans = d = (M - m + n - 2) // (n - 1)   # 间距下界（鸽巢原理）
        buckets = [[inf, -inf] for _ in range((M - m) // d + 1)]
        for num in nums:                       # 分桶，只存桶内 min/max
            b = buckets[(num - m) // d]
            b[0] = min(b[0], num)
            b[1] = max(b[1], num)

        pre_max = inf
        for mn, mx in buckets:                 # 跨桶求差
            if mn != inf:
                ans = max(ans, mn - pre_max)
                pre_max = mx
        return ans
```

## 关键
- 鸽巢原理：n 个数分布在 [min, max] 上，最大间距 ≥ ⌈(max-min)/(n-1)⌉，记为 d
- 按 d 分桶后，同一个桶内的差 < d，不可能是答案，最大间距只可能出现在相邻桶之间（前桶 max 与后桶 min）
- 桶内只需存 min 和 max 两个值，O(n) 时间 O(n) 空间

## 教训
- 看到"线性时间求数组最大间距" → 桶排序：先求间距下界 d，分桶只存 min/max，跨桶取差
- 自己单调栈方案的失败原因：扫栈找最小值是隐形的 O(n) 每轮，总 O(n²)
- 和 347 题对比：347 桶排序按频率分桶、按桶取数；164 按值域分桶、桶内压缩存极值——都是"用桶把全局问题变局部"
