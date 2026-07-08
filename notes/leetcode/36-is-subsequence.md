# LeetCode 392 判断子序列

## 思路 (10分钟)
双指针，s的字符按顺序在t中匹配。

## 我的代码
```python
def isSubsequence(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        i, j = 0, 0
        while i < n1:
            if s[i] in t:
                while j < n2:
                    if t[j] == s[i]:
                        j += 1
                        break
                    j += 1
                else:
                    return False
            else:
                return False
            i += 1
        return True
```

## 可以优化：
```python
# 更简洁的双指针
def isSubsequence(self, s: str, t: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1          # s匹配了一个，前进
        j += 1              # t始终前进
    return i == len(s)      # s是否全部匹配完
```

## 关键
- t始终前进，s匹配才前进
- 最后看s是否全部匹配完
- 不需要预检查 s[i] in t

## 教训
- 双指针不一定需要嵌套循环
