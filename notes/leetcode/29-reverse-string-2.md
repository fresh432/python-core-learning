# LeetCode 541 反转字符串 II

## 思路（40分钟）
range步长2k，每段反转前k个字符。

## 代码
```python
def reverseStr(s, k):
    L = list(s)
    for i in range(0, len(L), 2 * k):
        l, r = i, min(i + k - 1, len(L) - 1)
        while l &lt; r:
            L[l], L[r] = L[r], L[l]
            l += 1
            r -= 1
    return "".join(L)
```

## 关键
- 字符串不可变，先转列表
- range(0, n, 2*k) 控制处理窗口
- min(i+k-1, n-1) 防止越界

## 教训
- 字符串操作先想"要不要转列表"