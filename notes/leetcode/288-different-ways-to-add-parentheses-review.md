# LeetCode 241 为运算表达式设计优先级（复习）

## 我的思路（7分钟）
- 构造一个递归函数，传字符串窗口的下标 (l, r)；每次递归开始先判断窗口内是否为纯数字，是则直接返回数字
- 正式递归：创建局部数组保存本次运算的结果；循环遍历窗口，遍历到运算符时将该窗口按此运算符分为左右子窗口递归；再用两个结果数组与当前运算符运算；结果数组返回

## 代码
```python
from functools import cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def dfs(l, r):
            if expression[l:r].isdigit():
                return [int(expression[l:r])]
            res = []
            for i in range(l, r):
                if expression[i] in ['+', '-', '*']:
                    left = dfs(l, i)
                    right = dfs(i + 1, r)
                    for a in left:
                        for b in right:
                            if expression[i] == '+':
                                res.append(a + b)
                            elif expression[i] == '-':
                                res.append(a - b)
                            elif expression[i] == '*':
                                res.append(a * b)
            return res
        return dfs(0, len(expression))
```

## 教训
- 复习： 7 分钟一遍过（80 → 7），记忆化 DFS 已熟悉；这次改用 (l, r) 下标版，避免字符串切片开销
- 与 DP 版对比：递归版自上而下 + 哈希辅助记忆化拆解子问题；DP 版自下而上填表、用子问题组合结果