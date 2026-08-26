# LeetCode 121 买卖股票的最佳时机

## 我的思路（10分钟）
- 直觉很清晰：只需要维护一个历史最低买入价，然后遍历每天的价格，计算当天卖出的利润，取全局最大即可

## 代码
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            ans = max(ans, prices[i] - min_val)
        return ans if ans > 0 else 0
```

## 关键
- 一次遍历，同时维护两个变量：
  - min_val：历史最低买入价
  - ans：历史最大利润
- 每天先更新最小值，再计算当天卖出利润 prices[i] - min_val
- 最后返回 ans（若价格单调递减则返回0）

## 教训
- 看到"只能交易一次的最大利润" → 一次遍历维护历史最小值，贪心思路即可
- 初始化 min_val = prices[0]，ans = 0
- 注意最后 ans 可能为0（没有交易发生）