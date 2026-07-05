# LeetCode 151 反转字符串中的单词
 
## 思路（40分钟）
反向遍历：从后往前找单词，直接得到反转顺序。

## 代码
```python
def reverseWords(s):
    L = list(s)
    i = len(L) - 1
    ans = []
    
    while i >= 0:
        if L[i] != " ":
            j = i
            while j >= 0 and L[j] != " ":
                j -= 1
            ans.append("".join(L[j+1:i+1]))
            i = j
        i -= 1
    
    return " ".join(ans)
```

## 关键
- 反向遍历天然得到反转顺序
- j定位单词开头，i定位单词末尾
- 跳过空格：i -= 1

## 教训
- 反向遍历绕晕时，先用正向验证思路
- 边界条件：j+1到i+1的切片