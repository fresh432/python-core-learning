# LeetCode 76 最小覆盖子串

## 我的思路（80分钟）
- 前30分钟：想到用哈希表保存 t 和 s 窗口中的字符数，遍历 s 时逐个比对。但这样每次比对需要遍历哈希表，时间复杂度达不到 O(m+n)
- 中间20分钟：想优化比对方法，无果
- 后20分钟：看答案，核心洞察——反着存 t 的字符数（先减后加），用 ge_cnt 维护"已满足要求的字符种类数"。当某个字符的计数从负变零时，ge_cnt += 1；当 ge_cnt == kinds（t 中不同字符种类数）时，窗口已覆盖 t，开始收缩左边界找最小窗口
- 后10分钟：跟着写了一遍通过

## 代码
```python
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = defaultdict(int)
        for c in t:
            cnt_t[c] += 1
        
        kinds = len(cnt_t)  # t 中不同字符的种类数
        
        ans_left, ans_right = -1, len(s)
        ge_cnt = 0          # 已满足要求的字符种类数
        left = 0
        
        for right, c in enumerate(s):
            cnt_t[c] += 1
            if cnt_t[c] == 0:   # 从负变零，说明该字符刚好满足要求
                ge_cnt += 1
            
            # 窗口已覆盖 t，尝试收缩左边界
            while ge_cnt == kinds:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                
                x = s[left]
                if cnt_t[x] == 0:   # 移出后该字符将不满足要求
                    ge_cnt -= 1
                cnt_t[x] -= 1
                left += 1
        
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
```

## 关键
- 反着存：cnt_t 先记录 t 中每个字符的需求（正值），遍历 s 时遇到字符就 +1
- ge_cnt：当 cnt_t[c] == 0 时，说明该字符的需求刚好被满足（之前是负的，表示有多余；现在是零，表示刚好够）
- 收缩条件：ge_cnt == kinds，即 t 中所有字符种类都满足
- 移出左边界时：若 cnt_t[x] == 0，移出后会变负，该字符不再满足，ge_cnt -= 1
- 时间复杂度：O(m+n)，每个字符最多被访问两次（右指针一次，左指针一次）

## 教训
- 看到"最小覆盖子串 / 包含 t 所有字符的最短窗口" → 滑动窗口 + 反着存字符计数 + ge_cnt 维护满足种类数
- 不要逐个比对哈希表所有键，用 ge_cnt 记录"已满足的种类数"是 O(1) 判断
- 反着存的技巧：cnt_t[c] == 0 表示刚好满足，>0 表示还缺，<0 表示多余
- 和 3 题对比：3 是变长滑动窗口（无重复字符），76 是变长滑动窗口（覆盖所有目标字符），都需要动态收缩左边界

## 滑动窗口系列对比
| 题目            | 窗口类型   | 约束条件          | 核心技巧                    |
| :------------ | :----- | :------------ | :---------------------- |
| 3 无重复字符最长子串   | 变长     | 无重复字符         | 哈希表记最新下标                |
| 209 长度最小子数组   | 变长     | 和 ≥ target    | 右扩左缩                    |
| **76 最小覆盖子串** | **变长** | **覆盖 t 所有字符** | **反着存 + ge\_cnt 维护种类数** |
| 438 找到所有字母异位词 | 定长     | 字符频次相等        | 字符计数数组                  |
