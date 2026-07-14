# LeetCode 150 逆波兰表达式求值

## 我的思路（25分钟）
前10分钟：理解什么是逆波兰表达式（后缀表达式），数字入栈，遇到运算符弹出两个数计算.
后15分钟调试：
a 和 b 取值顺序搞反了：b = ans.pop() 先弹出的是右操作数，a = ans.pop() 是左操作数
忘记转换为 int 类型
向零取整：直接用 int(b/a) 即可截断小数（Python3的//是向下取整，负数时不对）

## 代码
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        anl = ['+', '-', '*', '/']
        for i in tokens:
            if i in anl:
                a = ans.pop()
                b = ans.pop()
                match i:
                    case '+':
                        ans.append(b + a)
                    case '-':
                        ans.append(b - a)
                    case '*':
                        ans.append(b * a)
                    case '/':
                        ans.append(int(b / a))
            else:
                ans.append(int(i))
        return ans[0]
```

## 关键
- 栈的经典应用：数字入栈，运算符出栈两个数计算
- 弹出顺序：b = pop()（右操作数），a = pop()（左操作数），计算 b op a
- 向零取整：int(b/a) 而不是 b//a（Python3的//对负数是向下取整）
- match-case 语法清晰处理多分支

## 教训
- 栈中弹出两个元素的顺序容易搞反，建议命名 right = pop(); left = pop() 更清晰
- Python3 除法取整的坑：// 向下取整，int() 向零取整，题目要求向零截断
- 逆波兰表达式 = 后缀表达式，核心就是"数字入栈，运算符出栈计算"
- 和 20 题（有效的括号）同属栈的应用，但场景不同：一个是匹配，一个是计算