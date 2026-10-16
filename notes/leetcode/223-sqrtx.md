# LeetCode 69 x 的平方根

## 我的思路（17分钟）
- 前10分钟：想到暴力求解和二分查找，但误以为完全禁止使用运算符。看了眼答案，发现只要不对传进来的 x 做运算就行
- 后7分钟：写出二分查找——在 [0, x] 区间二分，每次取 mid 的平方与 x 比较。若 mid² >= x 则收缩右边界，否则收缩左边界。最后对 left 取平方与 x 比较，若大于则返回 left - 1，否则返回 left

## 代码
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid >= x:
                right = mid
            else:
                left = mid + 1
        return left if left * left <= x else left - 1
```

## 关键
- 二分查找：left = 0, right = x
- 比较 mid * mid 和 x
- 终止后判断 left * left <= x，否则返回 left - 1

## 教训
- 看到"求平方根，不能用内置函数" → 二分查找
