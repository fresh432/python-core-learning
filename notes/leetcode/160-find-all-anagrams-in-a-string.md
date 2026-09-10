# LeetCode 438 找到字符串中所有字母异位词

## 我的思路（60分钟）
- 前5分钟：没思路，看标签提示"滑动窗口 + 哈希表"
- 中间10分钟：确定思路——固定窗口长度为 len(p)，一个哈希表存 p 的字符频次，另一个存滑动窗口的字符频次，两表相等时记录左边界
- 中间15分钟：卡壳点——担心每次比较两个哈希表需要遍历所有键，时间复杂度高。思考优化方法15分钟无果
- 中间10分钟：看答案，发现 Counter 可以直接用 == 比较，Python 内部实现了高效的字典比较。思路和自己完全一致，只是比较方式用 Counter 更简洁，理解后重写，通过
- 后10分钟：尝试剪枝优化时间，无果
- 最后10分钟：理解手写字符计数数组（[0] * 26）替代 Counter，用 ord(char) - ord('a') 做索引，比较两个数组是否相等。又写了一遍，23ms

## 代码（Counter 法）
```python
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(p), len(s)
        if n > m:
            return []
        
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []
        
        for right, char in enumerate(s):
            cnt_s[char] += 1
            left = right - n + 1
            if left < 0:
                continue
            if cnt_p == cnt_s:
                ans.append(left)
            cnt_s[s[left]] -= 1
        
        return ans
```

## 代码（字符计数数组）
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(p), len(s)
        if n > m:
            return []
        
        cnt_p = [0] * 26
        cnt_s = [0] * 26
        ans = []
        
        for c in p:
            cnt_p[ord(c) - ord('a')] += 1
        
        for right, char in enumerate(s):
            cnt_s[ord(char) - ord('a')] += 1
            left = right - n + 1
            if left < 0:
                continue
            if cnt_p == cnt_s:
                ans.append(left)
            cnt_s[ord(s[left]) - ord('a')] -= 1
        
        return ans
```

## 关键
- 滑动窗口：固定长度 len(p)，右指针遍历 s，左指针 right - n + 1
- 字符频次比较：Counter 可以直接 == 比较，但手写 26 长度数组更快（163ms → 23ms）
- 窗口移动：右边界加入新字符，cnt_s 对应位置 +1；左边界移出旧字符，对应位置 -1
- 剪枝尝试：当 s[right] 不在 p 中时将整个滑动窗口移至 s[right] 的右边,但实际优化起来较复杂

## 教训
- 看到"字符串异位词 / 固定长度子串匹配" → 滑动窗口 + 字符计数数组
- Counter 可以直接 == 比较，但手写 26 数组在字母场景下更快（避免了哈希开销）
- 和 3 题对比：3 是变长滑动窗口（无重复字符最长子串），438 是定长滑动窗口（异位词匹配）

## 滑动窗口系列对比
| 题目                | 窗口类型   | 约束条件       | 核心操作             |
| :---------------- | :----- | :--------- | :--------------- |
| 3 无重复字符最长子串       | 变长     | 无重复字符      | 哈希表记最新下标，动态收缩左边界 |
| 209 长度最小子数组       | 变长     | 和 ≥ target | 右扩左缩             |
| **438 找到所有字母异位词** | **定长** | **字符频次相等** | **字符计数数组，右进左出**  |
