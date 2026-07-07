# LeetCode 387 字符串中的第一个唯一字符

## 思路（20分钟）
哈希表统计，第一次出现=1，重复出现=0，再找第一个值为1的字符。

## 代码
```python
def firstUniqChar(s):
    h = {}
    for i in s:
        if i not in h:
            h[i] = 1
        else:
            h[i] = 0
    
    if 1 not in h.values():
        return -1
    
    for index, i in enumerate(s):
        if h[i] == 1:
            return index
```

## 关键
- 哈希表值：1=唯一，0=重复
- 两次遍历：先统计，再找第一个

## 教训
- 10分钟想"如何清除重复"，突然想到置0
- 哈希表值可以灵活定义，不只是计数