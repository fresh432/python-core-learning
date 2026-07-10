# LeetCode 242 有效的字母异位词（复习）

## 思路
哈希表计数：s加，t减，最后全0即为异位词。

## 代码
```python
def isAnagram(s, t):
    if len(s) != len(t): return False
    dic = defaultdict(int)
    for c in s: dic[c] += 1
    for c in t: dic[c] -= 1
    return all(v == 0 for v in dic.values())
```

## 关键
- 先比较长度，不同直接False
- 和387题哈希表思路一致
