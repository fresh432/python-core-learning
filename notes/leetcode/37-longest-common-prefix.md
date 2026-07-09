# LeetCode 14 最长公共前缀

## 思路（15分钟）
以第一个字符串为基准，逐个对比其他字符串，不匹配就截断。

## 代码
```python
def longestCommonPrefix(strs):
    ans = strs[0]
    for i in range(1, len(strs)):
        j = min(len(ans), len(strs[i]))
        k = 0
        while k < j:
            if ans[k] != strs[i][k]:
                break
            k += 1
        ans = ans[:k]
    return ans
```

## 关键
- 纵向比较，逐字符对比
- 内层while比for更方便处理break


