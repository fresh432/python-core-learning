# LeetCode 345 反转字符串中的元音字母

## 思路（6分钟）
344题同款双指针，跳过非元音再交换。

## 代码
```python
def reverseVowels(s):
    L = list(s)
    l, r = 0, len(s) - 1
    y = set("aeiouAEIOU")
    
    while l < r:
        while l < r and L[l] not in y:
            l += 1
        while l < r and L[r] not in y:
            r -= 1
        L[l], L[r] = L[r], L[l]
        l += 1
        r -= 1
    
    return "".join(L)
```

## 关键
元音集合：大小写都要包含
双指针，跳过非元音

## 教训
用set比list更快（O(1)查找）
模式和344/125一致：双指针+跳过条件
