# LeetCode 327 区间和的个数

## 我的思路（55分钟）
- 前10分钟：想到前缀和 + 暴力，O(n²) 必须优化
- 想前缀和 + 双指针滑动窗口，花15分钟尝试，发现这个方法会错过一些区间（数组有负数，前缀和不单调，滑动窗口不成立）
- 看提示说树状数组可以做；之前也想到过，但这个题的离散化怎么做实在想不出，不知道怎么排名存值
- 挣扎10分钟放弃，看答案20分钟：
  - 把边界转换成"每个前缀和可以接受的另一个前缀和的边界"，s1 - s2 ∈ [lower, upper] 转成找落在 [s1-upper, s1-lower] 的 s2
  - 问题变成"每个前缀和的匹配区间内有几个前缀和"。离散化时以每个前缀和及其匹配边界（s-lower、s-upper）进行排名
  - 顺序遍历，对每个前缀和先查匹配区间内已入树的个数再累加入 ans，最后把自己加入树
  - 注意点：需提前将前缀和 0 加入排名和树中（把数组下标 0 作为边界左端点的情况提前考虑进去）

## 代码
```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        vals = set()
        s = 0
        vals.add(s)                    # 前缀和 0
        for num in nums:
            s += num
            vals.add(s)
            vals.add(s - lower)        # 匹配边界也要进离散化集合
            vals.add(s - upper)

        sorted_vals = sorted(vals)
        rank = {v: i + 1 for i, v in enumerate(sorted_vals)}
        n = len(sorted_vals)
        tr = [0] * (n + 1)

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

        ans = 0
        s = 0
        add(rank[s])                   # 空前缀先入库
        for num in nums:
            s += num
            a = rank[s - lower]        # 匹配区间 [s-upper, s-lower]
            b = rank[s - upper] - 1
            ans += query(a) - query(b)
            add(rank[s])
        return ans
```

## 关键
- 核心转换：count(区间和 ∈ [lower, upper]) = 对每个前缀和 s1，数有多少个在它之前的 s2 满足 s2 ∈ [s1-upper, s1-lower]
- 离散化集合 = 所有前缀和 + 每个前缀和的两个匹配边界（s-lower、s-upper），查询边界值也要进离散化集合，这是与 315 的差别
- 顺序遍历：树里只有当前位置之前的前缀和，天然保证"区间"语义；先查后加
- 空前缀 0 必须先入库（对应区间从下标 0 开始的情况）

## 教训
- 看到"区间和在 [lower, upper] 内的个数" → 前缀和 + 离散化 + 树状数组；关键一步是 s2 ∈ [s1-upper, s1-lower] 的转换
- 自己卡死的原因：以为离散化只排"数组里的值"，实际当查询对象是"值域区间"时，区间的端点也必须进离散化集合
- 双指针失败的根源：含负数的数组前缀和不单调，一切依赖单调性的窗口/双指针都失效