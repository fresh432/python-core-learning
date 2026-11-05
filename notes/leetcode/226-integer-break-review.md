# LeetCode 343 整数拆分（复习）

## 我的思路（5分钟）
- 用数学法：将整数尽可能拆出多个 3，再看 n 除以 3 的余数
  - 余 0：直接返回 3^count
  - 余 2：答案再乘 2
  - 余 1：取出一个 3，把它和 1 合到一起拆成两个 2（因为 2×2 > 1×3）
  - n ≤ 3 特判：最大只能拆成 n - 1
- 数学论证：拆分后各数尽可能相等时乘积最大，求极值得该数为 e，2 和 3 最接近 e，3 最优、2 次优
- DP 方法不记得了，看答案补了一下

## 代码（数学法）
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        count = n // 3
        num = n % 3
        if num == 1:
            return 3 ** (count - 1) * 4
        elif num == 2:
            return 3 ** count * 2
        else:
            return 3 ** count
```

## 代码（DP 版）
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                # j 与 (i-j) 拆或不拆，取最大；j 有多种取值
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[-1]
```

## 教训
- 复习： 5 分钟写出数学法，公式已记牢；但 DP 转移方程忘了，数学法依赖记忆结论，DP 才是通用方法，两种都要会