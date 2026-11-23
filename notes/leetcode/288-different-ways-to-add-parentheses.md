# LeetCode 241 为运算表达式设计优先级

## 我的思路（80分钟）
- 前30分钟：想到 DP，以为类似戳气球按窗口大小找最后一个运算操作；先把数字和字符拆开存，但想不出操作符数组和数字数组之间怎么联系
- 看答案10分钟：递归法
  - 进入递归先判定传入字符串是否为数字，是则直接返回
  - 每次递归新建数组存本次所有结果
  - 遍历字符串，遇到运算符按该位置分成左右两部分递归，拿左右结果数组按运算符做笛卡尔积运算，结果数组返回
  - 函数前加 @cache 记忆化，已算过的子问题直接返回
- 再看递归写法，发现思路和戳气球确实类似，也分数字和操作符两部分，且操作符与"两个被运算数中第一个数"的下标相同（ops[k] 在 num[k] 与 num[k+1] 之间），下标关系打通后，又花40分钟尝试区间 DP 版：
  - 分窗口大小、起始左边界、最后运算的符号三层遍历，初始化先给对角线 dp 赋予对应数字
  - dp 里放数组，状态转移是把左右两部分数组按当前运算符运算后拼接到当前窗口列表，初始化和边界调试了一会，通过

## 代码（记忆化 DFS）
```python
from functools import cache

class Solution:
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():          # 纯数字直接返回
            return [int(expression)]

        res = []
        for i, ch in enumerate(expression):
            if ch in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:            # 笛卡尔积合并
                    for r in right:
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res
```

## 代码（区间 DP）
```python
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        num, ops, tmp = [], [], ""
        for ch in expression:
            if ch in "+-*":
                ops.append(ch)
                num.append(tmp)
                tmp = ""
            else:
                tmp += ch
        num.append(tmp)

        n = len(num)
        dp = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].append(int(num[i]))      # 对角线初始化数字

        for i in range(1, n):
            for l in range(n - i):
                r = l + i
                for k in range(l, r):         # k：最后运算的运算符
                    if ops[k] == '+':
                        tmp = [a + b for a in dp[l][k] for b in dp[k + 1][r]]
                    if ops[k] == '-':
                        tmp = [a - b for a in dp[l][k] for b in dp[k + 1][r]]
                    if ops[k] == '*':
                        tmp = [a * b for a in dp[l][k] for b in dp[k + 1][r]]
                    dp[l][r] += tmp
        return dp[0][n - 1]
```

## 关键
- 分治本质：每个运算符都可能是"最后运算"的那个，左右子问题独立求解后组合
- 数字与运算符的映射：n 个数字配 n-1 个运算符，ops[k] 位于 num[k] 与 num[k+1] 之间，分开存数组就靠这个下标关系联系
- DFS 版用 @cache 记忆化（子串重复计算）；DP 版用区间套路（对角线初始化、按窗口长度扩展）

## 教训
- 看到"为运算表达式设计优先级/所有加括号结果" → 分治 DFS（@cache）或区间 DP（dp 存结果数组）
- 和 312 对比：同为"最后操作者"型分治/区间 DP，312 的 dp 存标量最值、241 的 dp 存结果列表，结构同构，状态值类型不同而已