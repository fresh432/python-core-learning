# LeetCode 343 整数拆分

## 我的思路（45分钟）
- 前10分钟：想用 DP 拆成最优两个数迭代，但写偏了，试图用队列保存拆分结果，没用 DP
- 中间15分钟：调试无果，转回 DP 但想不出状态转移方程，甚至以为要倒着 DP
- 后10分钟：看答案
  - 数学法：用求极值推断最优拆分数为 3（尽量拆成 3，余数为 1 时拆成 2+2）
  - DP 法：类似爬楼梯，dp[i] 表示整数 i 拆分后的最大乘积，dp[i] = max(j * (i-j), j * dp[i-j])，j 从 1 到 i//2
- 后10分钟：两个方法都实现了一遍

## 代码（动态规划）
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[-1]
```

## 代码（数学计算）
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a = n // 3
        b = n % 3
        if b == 1:
            return 3 ** (a - 1) * 4
        if b == 2:
            return 3 ** a * 2
        else:
            return 3 ** a
```

## 关键
- DP：dp[i] 表示整数 i 拆分后的最大乘积
  - 拆成两个数：j * (i-j)
  - 拆成多个数：j * dp[i-j]
  - 取 max
- 数学法：尽量拆成 3，余数处理：
  - 余 0：3^a
  - 余 1：3^(a-1) * 4（把 3+1 拆成 2+2）
  - 余 2：3^a * 2

## 教训
- 看到"整数拆分成若干正整数，乘积最大" → DP 或数学法（尽量拆 3）
- 数学法的核心：对 f(x) = x^(n/x) 求导，极值点在 x = e ≈ 2.718，所以整数取 3 最优
- 和 322/518 题对比：322 是完全背包最值（最少硬币），518 是完全背包计数（方案数），343 是整数拆分最值（最大乘积）