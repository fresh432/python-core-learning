# LeetCode 459 重复的子字符串

## 我的思路（50分钟）
暴力枚举子串长度，逐个验证。

## 更优解：拼接法
```python
def repeatedSubstringPattern(s):
    return s in (s + s)[1:-1]
```

## 原理
- s由子串重复 → s+s中间必包含s
- [1:-1]去掉首尾，防止匹配自身

## 教训
- 50分钟暴力，一行搞定
- 字符串题先想性质，不要硬枚举