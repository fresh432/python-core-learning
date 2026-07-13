# LeetCode 20 有效的括号

## 思路（15分钟）
栈：左括号入栈，右括号匹配栈顶。

## 代码
```python
def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0
```

## 关键
- 字典映射右括号→左括号
- 栈顶不匹配直接返回False
- 最后栈为空才有效

## 教训
- 变量名打错：ans打成s