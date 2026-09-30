# LeetCode 135 分发糖果

## 我的思路（40分钟）
- 前15分钟：想遍历一遍，比前一个大就取前一个糖果数+1，其他情况默认1。但发现递减情况处理不了
- 中间15分钟：思考递减怎么处理，没想出来
- 后10分钟：看答案，核心洞察——左右各遍历一遍：
  - 从左往右：若 ratings[i] > ratings[i-1]，则 dp[i] = dp[i-1] + 1（左递增）
  - 从右往左：若 ratings[i] > ratings[i+1]，则 dp[i] = max(dp[i], dp[i+1] + 1)（右递增，取最大值）
- 最后10分钟：根据思路写出，通过

## 代码
```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp = [1] * n
        
        # 从左往右：处理左递增
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        
        # 从右往左：处理右递增，取最大值
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i + 1] + 1, dp[i])
        
        return sum(dp)
```

## 关键
- 两次遍历：左→右处理"比左边大"的情况，右→左处理"比右边大"的情况
- 右→左遍历时用 max：因为该位置可能已经被左遍历赋了更大的值
- 初始化：dp = [1] * n，每个孩子至少1颗糖

## 教训
- 看到"相邻比较，求最小分配" → 左右两次遍历，分别处理两个方向的约束
- 单次遍历无法同时处理左右两个方向的递增关系
- 和 134 题对比：134 是加油站（贪心重置起点），135 是糖果分配（两次遍历取 max）
