# LeetCode 151 反转字符串中的单词（复盘）

## 时间
15分钟（之前40分钟）

## 代码
```python
def reverseWords(s):
    n = len(s)
    i = n - 1
    ans = []
    while i >= 0:
        if s[i] == " ":
            i -= 1
            continue
        j = i
        while i >= 0 and s[i] != " ":
            i -= 1
        ans.append("".join(s[i+1:j+1]))
    return " ".join(ans)
```

## 进步
- 40分钟→15分钟，模式巩固
- 注意：and/or循环条件别搞混