# LeetCode 164 最大间距（复习）

## 我的思路（20分钟）
- 思路都还记得：先求出间距下界 d，按 d 分桶；每个桶存该桶内的最大值和最小值；同一个桶内的跨度不会超过 d，所以答案从相邻有效桶之间求出（前桶 max 与后桶 min 之差）
- 卡在分桶的地方：以为是分成 n - 1 个桶，后来才想起是分成（总跨度 // d）个，改完通过

## 代码
```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        if max_num - min_num <= 1:
            return max_num - min_num
        n = len(nums)
        d = (max_num - min_num + n - 2) // (n - 1)   # 间距下界
        buckets = [[inf, -inf] for _ in range((max_num - min_num) // d + 1)]
        for num in nums:
            b = buckets[(num - min_num) // d]
            b[0] = min(b[0], num)
            b[1] = max(b[1], num)
        pre_max = buckets[0][1]
        ans = d
        for b in buckets:
            if b[0] == inf:        # 空桶跳过
                continue
            ans = max(ans, b[0] - pre_max)
            pre_max = b[1]
        return ans
```

## 教训
- 复习：20 分钟通过，核心思路（d 下界 + 分桶存极值 + 跨桶取差）已记住
- 踩坑点：桶数 = (max-min) // d + 1，由值域跨度决定，与 n 无关，n-1 是"平均间隔数"的思维惯性，分桶时别混淆
- 空桶要跳过（首次做时的代码 pre_max 处理要小心：遍历时只更新非空桶）