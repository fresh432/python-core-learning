# LeetCode 290 单词规律

## 思路（25分钟）
双向映射：pattern字符↔单词，双向一对一。

## 代码
```python
def wordPattern(pattern, s):
    c1, c2 = {}, {}           # 两个独立字典！
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    for i in range(len(pattern)):
        # pattern→word映射检查
        if pattern[i] in c1 and c1[pattern[i]] != words[i]:
            return False
        # word→pattern映射检查
        if words[i] in c2 and c2[words[i]] != pattern[i]:
            return False
        
        c1[pattern[i]] = words[i]
        c2[words[i]] = pattern[i]
    
    return True
```

## 关键
- 双向映射防止多对一（如 pattern="abba", s="dog dog dog dog"）
- c1, c2 = {}, {} 不是 c1 = c2 = {}
- s.split() 按空格分割字符串

## Python经典坑
```python
# ❌ 同一个对象
a = b = {}
a['x'] = 1
print(b)  # {'x': 1}

# ✅ 两个独立对象
a, b = {}, {}
```

## 教训
- 赋值语句的坑排查了很久
- 双向映射是标准解法，和205题同构

