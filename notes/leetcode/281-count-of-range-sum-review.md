# LeetCode 327 区间和的个数（复习）

## 我的思路（25分钟）
- 问题转换：原问题是"区间和落在 [lower, upper] 的区间个数"，转换成"每个前缀和 s 中，匹配到的其他前缀和落在 [s-upper, s-lower] 中的个数"，从统计区间个数换成统计符合条件的前缀和个数
- 离散化要存：每个前缀和匹配区间的端点 + 所有前缀和，0 也要提前作为前缀和存进去。端点离散化把负数端点和端点稀疏问题解决
- 分工理解：前缀和负责存值部分，端点负责取值部分，端点离散化是为了取值时有边界排名好查找
- 树状数组部分：正常取排名，查区间中匹配的前缀和个数，再把当前前缀和存入，累计返回

## 代码
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        vals = set()
        s = 0
        vals.add(s)
        for num in nums:
            s += num
            vals.add(s)
            vals.add(s - lower)
            vals.add(s - upper)

        def add(i):
            while i <= n:
                tr[i] += 1
                i += i & -i

        def query(i):
            cnt = 0
            while i > 0:
                cnt += tr[i]
                i -= i & -i
            return cnt

        sorted_vals = sorted(vals)
        rank_map = {v: i + 1 for i, v in enumerate(sorted_vals)}
        n = len(rank_map)
        tr = [0] * (n + 1)

        ans = 0
        s = 0
        add(rank_map[s])
        for num in nums:
            s += num
            a = rank_map[s - lower]
            b = rank_map[s - upper] - 1
            ans += (query(a) - query(b))
            add(rank_map[s])
        return ans
```

## 教训
- 复习： 25 分钟（首次 55），问题转换和离散化都记住了，一次通过
- 本次复习最大的收获是"存值 与 取值"的分工表述：前缀和入库（存值），匹配端点造排名（取值边界）
