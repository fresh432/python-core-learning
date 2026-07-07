# LeetCode 58 最后一个单词的长度

## 思路 (5分钟)
倒序遍历，从后往前找到最后一个单词，统计长度。

## 代码
```python
def lengthOfLastWord(s):
    n = len(s)
    for i in range(n - 1, -1, -1):
        if s[i] != " ":
            j = i
            ans = 0
            while j &gt;= 0 and s[j] != " ":
                ans += 1
                j -= 1
            return ans
    return 0
```

## 关键
- 倒序遍历，跳过尾部空格
- 找到非空格后开始计数

## 教训
- 151题反向遍历的经验直接复用
- 字符串题先想遍历方向