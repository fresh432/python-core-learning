# LeetCode 28 找出字符串中第一个匹配项的下标

## 第一版：暴力双指针（15分钟）
- 执行用时：3601ms，击败4.87%
- 问题：j重置逻辑混乱，回退处理不当

## 第二版：切片法（6分钟，看答案后）
```python
def strStr(haystack, needle):
    n1, n2 = len(haystack), len(needle)
    if n1 &lt; n2: return -1
    for i in range(n1 - n2 + 1):
        if haystack[i:i+n2] == needle:
            return i
    return -1
```

## 关键
Python切片底层优化，实际很快
要学会用KMP，但这是暴力优化版
