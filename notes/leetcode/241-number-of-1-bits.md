# LeetCode 191 位 1 的个数

## 我的思路（2分钟）
- 用 n & (n-1) 提取并消去最低位的 1，循环直到 n 为 0（没有 1 可提取），每次提取计数加一

## 代码
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n - 1)
            ans += 1
        return ans
```

## 关键
- n & (n-1) 的作用：将 n 最低位的 1 变为 0
- 循环次数 = 二进制中 1 的个数，与总位数无关

## 教训
- 看到"统计二进制中 1 的个数" → n & (n-1) 循环计数
- 位运算基础技巧：n & (n-1) 消最低位 1，n & (-n) 取最低位 1
