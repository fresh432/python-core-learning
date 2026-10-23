# LeetCode 367 有效的完全平方数

## 我的思路（4分钟）
- 二分，判断 mid * mid 与 num：不等则缩边界，相等返回 True；遍历结束说明不是完全平方数，返回 False
- num = 1 时需特殊判断

## 代码
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 0, num
        while left < right:
            mid = (left + right) // 2
            if mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid
            else: return True
        return False
```

## 关键
- 二分查找：mid² 与 num 比较，缩小边界
- 相等即返回 True，循环结束返回 False
- num = 1 特判

## 教训
- 看到"判断完全平方数，不能用 sqrt" → 二分，mid * mid 比较
- 和 69 题对比：69 是求平方根（返回开方结果），367 是判断能否开方（返回布尔），框架完全一样
