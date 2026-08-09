# LeetCode 97 交错字符串

## 我的思路（35分钟）
- 前15分钟：误解题意，以为 s1 和 s2 分成的"块"数量相差不能超过一，试图把字符串拆分成组来进行状态迭代，越想越复杂
- 中间10分钟：看答案，发现根本不需要分组——就是简单的二维布尔数组，dp[i][j] 表示 s1 前 i 个字符和 s2 前 j 个字符能否交错组成 s3 前 i+j 个字符
- 后10分钟：写出代码，分别处理第一行/第一列的边界初始化，再填一般状态

## 代码
```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        
        # 第一列：只用 s1
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # 第一行：只用 s2
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # 一般状态
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                           (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        
        return dp[-1][-1]
```

## 关键
- 状态定义：dp[i][j] = s1[0:i] 和 s2[0:j] 能否交错组成 s3[0:i+j]
- 状态转移（两种来源）：
  - 当前字符来自 s2：dp[i][j-1] 为 True 且 s2[j-1] == s3[i+j-1]
  - 当前字符来自 s1：dp[i-1][j] 为 True 且 s1[i-1] == s3[i+j-1]
- 初始化：先处理边界（只用 s1 或只用 s2 的情况），dp[0][0] = True
- 前置剪枝：n1 + n2 != n3 时直接返回 False

## 教训
- 看到"两个字符串交错/合并" → 二维布尔 DP，dp[i][j] 分别对应两个字符串的前缀长度
- 不要过度解读题意，"交错"就是字符逐个交替，不需要分组或块的概念
- 和 1143 题（LCS）对比：都是二维字符串 DP，但 1143 是"最长公共子序列"，97 是"能否交错组成"