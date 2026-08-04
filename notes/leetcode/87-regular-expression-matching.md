# LeetCode 10 正则表达式匹配

## 我的思路（70分钟）
1. 前20分钟：画图找规律想不出来
2. 中间20分钟：想分三种情况讨论（*、.、正常字符），逻辑太绕写不下去
3. 后30分钟：看答案理解——只要分是不是 * 两种情况，* 的处理是关键

## 代码
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        
        # 初始化：s为空，p为 a*b*c* 形式时可能匹配
        for j in range(2, n2 + 1, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if p[j - 1] == "*":
                    # * 让前一个字符出现0次：dp[i][j-2]
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    # * 让前一个字符出现多次：需要s[i-1]匹配p[j-2]
                    elif dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == "."):
                        dp[i][j] = True
                else:
                    # 正常匹配或 .
                    if dp[i - 1][j - 1] and (p[j - 1] == "." or s[i - 1] == p[j - 1]):
                        dp[i][j] = True
        
        return dp[n1][n2]
```

## 关键
- 状态定义：dp[i][j] = s[0:i] 和 p[0:j] 是否匹配
- "*" 的处理（核心难点）：
    - "*" 让前一个字符出现 0 次：dp[i][j-2]
    - "*" 让前一个字符出现 多次：dp[i-1][j] 且 s[i-1] 匹配 p[j-2]
- . 的处理：匹配任意单个字符
- 初始化：dp[0][j] 处理 a*b*c* 匹配空串的情况

## 教训
- 看到"正则/通配符匹配" → 二维 DP，* 是核心难点
- 不要分太多种情况，围绕 * 分两种（出现0次/多次）即可
- 画矩阵时特别注意 * 的列，初始化 dp[0][j] 容易漏
