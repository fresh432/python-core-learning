# LeetCode 205 同构字符串

## 思路（15分钟）
单向映射 + 值去重，防止多对一。

## 我的代码
```python
def isIsomorphic(s, t):
    h = {}
    for i in range(len(s)):
        if s[i] not in h:
            if t[i] in h.values():  # 值已被映射
                return False
            h[s[i]] = t[i]
        else:
            if t[i] != h[s[i]]:       # 映射不一致
                return False
    return True
```

## 更优解：双向映射
```python
def isIsomorphic(s, t):
    s_to_t, t_to_s = {}, {}
    for c1, c2 in zip(s, t):
        if c1 in s_to_t and s_to_t[c1] != c2: return False
        if c2 in t_to_s and t_to_s[c2] != c1: return False
        s_to_t[c1] = c2
        t_to_s[c2] = c1
    return True
```

## 关键
- 同构 = 双向一对一映射
- zip(s, t) 同时遍历两个字符串
- 双向映射比单向+values检查更优

## 教训
- 嵌套if可以简化，但可读性更重要
- 追求代码优雅是好的，但别牺牲清晰度
- 双向映射是标准解法

