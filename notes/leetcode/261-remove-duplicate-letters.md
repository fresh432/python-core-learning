# LeetCode 316 去除重复字母

## 我的思路（40分钟）
- 用 cnt 对原字符串字母全部计数，然后遍历：用单调递增栈，若当前字母小于栈顶元素、且栈顶元素在后续字符串中还会出现（cnt > 1），则弹出栈顶并将该字母计数减一，直到栈顶为小于当前元素的字母，再将当前字母入栈
- 每遍历一个元素先判断：若已在栈中，则计数减一并直接跳过
- 中间调试较多，最后做了简写；栈中判断用普通 in 而非哈希——栈最多保留 26 个字母，视为 O(1)

## 代码
```python
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        stack = []

        for ch in s:
            if ch in stack:
                cnt[ch] -= 1
                continue
            while stack and ord(ch) < ord(stack[-1]) and cnt[stack[-1]] > 1:
                cnt[stack.pop()] -= 1
            stack.append(ch)

        return "".join(stack)
```

## 关键
- 弹出条件（同时满足）：当前字母更小 且 栈顶字母在后续还会出现（cnt[栈顶] > 1）
- 跳过条件：当前字母已在栈中（栈内字母始终保持唯一）
- cnt 一身二职：初始化是"总数"，遍历中是"剩余计数"，每过一个字母减一

## 教训
- 看到"去除重复字母/结果字典序最小" → 单调递增栈 + 剩余计数
- 弹出的前提必须是"后面还有这个字母"，否则弹出去就凑不齐了
