# LeetCode 301 删除无效的括号

## 我的思路（70分钟）
- 前50分钟：自己的思路——统计左右括号数量，判断哪种多了、多几个，递归删除后统一检查有效性。但无法处理左右括号数量相等却位置非法的情况（如 ")("），尝试修复无果
- 后10分钟：看答案
  - BFS：每轮对队列中每个字符串删除一个括号后加回队列，某轮出现合法字符串就返回该轮所有合法字符串
  - DFS：先算出最多能保留多少对括号 target，path 维护路径，剪枝后走到末尾即为合法解，本质是"选与不选"
- 后10分钟：两个方法都实现了一遍

## 代码（BFS）
```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s) -> bool:
            left = 0
            for ch in s:
                if ch == "(":
                    left += 1
                elif ch == ")":
                    if left == 0:
                        return False
                    left -= 1
            if left != 0: return False
            return True

        queue = [s]
        while queue:
            queue = list(set(queue))  # 去重
            ans = [t for t in queue if is_valid(t)]
            if ans:
                return ans

            tmp = queue
            queue = []
            for s in tmp:
                for i, ch in enumerate(s):
                    if ch in "()":
                        queue.append(s[:i] + s[i + 1:])
```

## 代码（DFS）
```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left, target = 0, 0
        for ch in s:
            if ch == "(":
                left += 1
                target += 1
            elif ch == ")" and left > 0:
                left -= 1
        target -= left  # 最多能保留的括号对数

        n = len(s)
        ans = []
        path = []

        def dfs(i, left, right):
            if left < right or left > target or left + right + n - i < target * 2:
                return
            if i == n:
                ans.append(''.join(path))
                return

            ch = s[i]
            if ch == "(" or ch == ")":
                # 不选：跳过连续相同括号，避免重复解
                j = i + 1
                while j < n and s[j] == ch:
                    j += 1
                dfs(j, left, right)

            if ch == "(":
                left += 1
            elif ch == ")":
                right += 1
            path.append(ch)
            dfs(i + 1, left, right)
            path.pop()

        dfs(0, 0, 0)
        return ans
```

## 关键
- BFS 本质：按删除个数分层，第一轮出现合法串的层删除次数最少；每轮 set 去重
- target 计算：遍历一遍，( 使 left+1、target+1；) 且 left > 0 时 left-1；最后 target -= left 减掉配不了对的左括号
- DFS 三个剪枝条件：
  - left < right：右比左多，前缀非法
  - left > target：保留的左括号超上限
  - left + right + n - i < target * 2：剩下的全选也凑不够 target 对

## 教训
- 看到"删除最少括号使合法，返回所有方案" → BFS 逐层删除或 DFS + 剪枝
- BFS 正确性直观但慢（67ms），DFS+剪枝快一个数量级（3ms）
- 自己思路的根本缺陷：只能处理"某一种括号多了"的场景，处理不了数量相等但位置非法的情况。以后括号问题先想"最多保留多少对"，而不是"删多少个"
