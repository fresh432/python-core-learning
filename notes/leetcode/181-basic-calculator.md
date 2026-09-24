# LeetCode 224 基本计算器

## 我的思路（60分钟）
- 前40分钟：根据 227 题模板修改，去掉乘除，增加括号处理。思路：遇左括号将当前运算符和左括号入栈，遇右括号循环弹出累加直到左括号，再弹出之前保存的运算符，根据正负将结果入栈。最后累加栈中元素。但最坏情况需要两遍遍历（先处理括号再求和）
- 后15分钟：看答案，发现可以一次遍历完成——用栈模拟递归：
  - 正常累加遍历到的数字
  - 遇左括号：将之前累加的 res 和当前 sign 入栈，然后 res = 0, sign = 1 重置
  - 遇右括号：括号内累加结果 res *= 栈顶sign + 栈顶res，一次运算完成
- 后5分钟：按优化思路重写，通过

## 代码
```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        pre_op = "+"
        
        for i, char in enumerate(s):
            if char not in "()+-" :
                num = num * 10 + int(char)
            
            if i == len(s) - 1 or char in "+-()":
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                
                if char != "(":
                    pre_op = char
                num = 0
                
                if char == "(":
                    stack.append(pre_op)
                    stack.append(char)
                    pre_op = "+"
                elif char == ")":
                    n = 0
                    while n != "(":
                        num += n
                        n = stack.pop()
                    pre_op = stack.pop()
                    stack.append(num if pre_op == "+" else -num)
                    num = 0
        
        return sum(stack)
```

## 代码（优化版，单遍历）
```python
class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        
        for c in s:
            if c not in "+-() ":
                num = num * 10 + int(c)
            elif c in "+-":
                res += num * sign
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += num * sign
                num = 0
                res *= stack.pop()      # 括号前的符号
                res += stack.pop()      # 括号前的累加结果
        
        res += num * sign
        return res
```

## 关键
- 优化版核心：栈保存递归状态（res 和 sign），遇到括号相当于进入新的一层计算
- res：当前层的累加结果
- sign：当前数字的符号（1 或 -1）
- 左括号：将当前 res 和 sign 压栈，重置为新的一层
- 右括号：完成当前层计算，res = res * sign(栈顶) + res(栈顶)
- 数字处理：遇到运算符或括号时，将 num * sign 加到 res，然后重置 num

## 教训
- 看到"含括号的字符串计算器" → 栈模拟递归，一次遍历完成
- 和 227 题对比：227 是四则运算（先乘除后加减），224 是加减+括号（用栈模拟递归层级）
