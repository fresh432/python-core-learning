# LeetCode 125 验证回文串

## 思路（10分钟）
双指针，跳过非字母数字，转小写比较。

## 代码
```python
def isPalindrome(s):
    s = s.lower()
    i, j = 0, len(s) - 1
    while i &lt; j:
        while i &lt; j and not s[i].isalnum(): i += 1
        while i &lt; j and not s[j].isalnum(): j -= 1
        if s[i] != s[j]: return False
        i += 1; j -= 1
    return True
```

## 关键
- isalnum() 判断字母或数字
- isalpha() 纯字母，isdigit() 纯数字
- 先转小写再比较

## 教训
- 不知道isalnum，查了文档才知道
- Python字符串方法要熟悉