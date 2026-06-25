# LeetCode 344 反转字符串

## 思路
左右指针交换，原地修改。

## 代码
```python
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```
## 感悟
- 题目要求"原地修改" = 考双指针
- 库函数 reverse() 更快，但面试要写算法
- 简单题是练熟练度，不是追求最优