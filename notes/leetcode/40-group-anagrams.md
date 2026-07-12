# LeetCode 49 字母异位词分组

## 思路（30分钟卡住，看答案）
排序作为key，相同key的字符串分到同一组。

## 代码
```python
def groupAnagrams(strs):
    h = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        h[sorted_s].append(s)
    return list(h.values())
```

## 关键
- 排序后的字符串是异位词的"唯一标识"
- 不需要两两比较（242题思维陷阱）
- defaultdict(list) 自动创建空列表

## 教训
- 242题思维惯性：想双层循环判断
- 哈希表分组的核心是设计好key
- 排序是字符串问题的常用预处理

## 和242题的关系
| 题目           | 核心操作            |
| ------------ | --------------- |
| 242 有效的字母异位词 | 判断两个字符串是否排序后相同  |
| 49 字母异位词分组   | 把所有字符串排序后按key分组 |
