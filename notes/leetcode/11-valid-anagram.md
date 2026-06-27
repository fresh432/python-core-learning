# LeetCode 242 有效的字母异位词

## 思路
哈希表计数：统计每个字母出现次数，比较是否相同。

## 代码
```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    h = {}
    for char in s:
        h[char] = h.get(char, 0) + 1
    for char in t:
        if char not in h:
            return False
        else:
            h[char] -= 1
            if h[char] < 0:
                return False
    return True
```

## 关键
- 先比较长度，不同直接返回 False
- 一个字符串加，一个字符串减
- 最后所有计数应为 0