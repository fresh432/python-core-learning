# LeetCode 8 字符串转换整数（atoi）

## 我的思路（40分钟）
- 前35分钟：基本流程写完，提交才发现不能用 int()——哪怕对单个字符也不行，快超时只好看答案
- 看答案想起来可以用 ASCII 码：ord(ch) - ord("0") 获取数字，5分钟改完，补充边界后通过
- 思路分模块：去前导空格 → 判断符号（flag 保存正负）→ 截断非数字字符 → 逐字符 ord 相减累加 → 累加中判边界，超出直接返回边界值

## 代码
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        valid = "1234567890+-"

        while s[0] == " ":
            s = s[1:]
            if not s:
                return 0

        if not s or s[0] not in valid:
            return 0

        flag = -1 if s[0] == "-" else 1
        if s[0] in "+-":
            s = s[1:]

        for i, ch in enumerate(s):
            if ch not in "1234567890":
                s = s[:i]
                break

        for ch in s:
            ans = ans * 10 + (ord(ch) - ord("0")) * flag
            if ans > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif ans < -(2 ** 31):
                return -(2 ** 31)

        return ans
```

## 关键
- 模块化四步：去空格 → 符号 flag → 截断非数字 → ord 累加
- ord(ch) - ord("0") 代替 int(ch)
- 乘 flag 后再判边界：一次循环同时处理正溢出（2³¹-1）和负溢出（-2³¹）

## 教训
- 看到"实现 atoi/字符串转数字" → 模块化拆解，ord 代替 int
- 踩坑：这题的限制是不能用 int()，43/415 题限制的是整个字符串，单个字符可以用 int——限制条件每题不同，动手前先看清
