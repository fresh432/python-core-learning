# LeetCode 344 反转字符串（复习）

## 时间
1分钟，条件反射

## 代码
```python
def reverseString(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
```

