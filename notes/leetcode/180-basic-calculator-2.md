# LeetCode 227 基本计算器 II

## 我的思路（60分钟）
- 前15分钟：想到逆波兰表达式的思路，但发现本题运算符在运算数中间（中缀表达式）。不过仍然可以用栈：遍历字符，用变量保存当前数字，遇到运算符时根据上一个运算符的类型决定操作——若是乘除则与栈顶运算，若是加减则入栈。遍历完后栈中只有加减，再求和
- 中间20分钟：边界细节难处理，调试不过
- 后20分钟：看答案，发现还有双栈法（数字栈+运算符栈），拓展性更好。但选择了一个和自己思路一致的题解，边界处理更简洁
- 后5分钟：根据题解重写，通过

## 代码
```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = '+'
        num = 0
        
        for i, char in enumerate(s):
            if char not in "+-*/ ":
                num = num * 10 + int(char)
            
            if i == len(s) - 1 or char in "+-*/":
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    stack.append(stack.pop() * num)
                elif pre_op == "/":
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                
                pre_op = char
                num = 0
        
        return sum(stack)
```

## 关键
- 核心思想：先处理乘除，后处理加减
- pre_op：保存上一个运算符，遇到新运算符时才处理前一个数字
- 数字解析：num = num * 10 + int(char)，处理多位数
- 触发计算：遍历到末尾或遇到运算符时，根据 pre_op 决定操作
- 除法处理：Python 的 // 是向下取整，负数时需要先转浮点 int(top / num) 保证向零取整

## 教训
- 边界：空格跳过、末尾需要触发最后一次计算、负数除法的取整方向
