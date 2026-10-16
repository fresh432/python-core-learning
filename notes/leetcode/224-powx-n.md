# LeetCode 50 Pow(x, n)

## 我的思路（40分钟）
- 前15分钟：想用递归累乘，但超时了
- 中间15分钟：想将幂拆成两半分别递归再相乘，奇数时额外乘一次。超时
- 后10分钟：看提示，核心洞察——快速幂：不是将幂拆成两半分别递归，而是将当前数字平方后，对平方后的数字做减半幂的递归。即 x^n = (x²)^(n/2)，奇数时额外乘 x

## 代码（递归法）
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        def dfs(num, times):
            if times == 0:
                return 1
            res = num * num
            res = dfs(res, times // 2)
            if times % 2:
                res *= num
            return res
        
        ans = dfs(x, n) if n >= 0 else 1 / dfs(x, -n)
        return ans
```

## 代码（迭代法）
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        ans = 1
        times = n if n >= 0 else -n
        
        while times > 0:
            if times % 2:
                ans *= x
            x *= x
            times //= 2
        
        return ans if n >= 0 else 1 / ans
```

## 关键
- 快速幂：x^n = (x²)^(n/2)
- 递归：先平方再递归减半幂
- 迭代：ans 累积结果，x 不断平方，times 不断减半
- 负数处理：n < 0 时取倒数

## 教训
- 看到"求幂，要求 O(log n)" → 快速幂，平方+减半
