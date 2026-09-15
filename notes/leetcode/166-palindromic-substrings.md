# LeetCode 647 回文子串

## 我的思路（20分钟）
- 前10分钟：和 5 题基本一致，从"求最长"改为"求个数"。用中心扩展法，枚举每个节点为中心向两边扩展，每成功扩展一次计数加一。上次奇偶分开写，这次用奇偶合并写法（2*n - 1 个中心点），10分钟通过
- 后10分钟：看了动态规划法——从下往上、从左往右遍历，dp[i][j] 表示 s[i:j+1] 是否为回文。当 s[i] == s[j] 且内部子串也是回文（j - i <= 1 或 dp[i+1][j-1]）时，dp[i][j] = True 且计数加一

## 代码（中心扩展法）
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(2 * n - 1):
            left, right = i // 2, (i + 1) // 2
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
        
        return ans
```

## 代码（动态规划法）
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    ans += 1
                    dp[i][j] = True
        
        return ans
```

## 关键
- 中心扩展奇偶合并：i 从 0 到 2n-2，left = i // 2, right = (i + 1) // 2
  - i 为偶数：left == right，奇数长度中心
  - i 为奇数：right = left + 1，偶数长度中心
- DP 法：dp[i][j] 依赖 dp[i+1][j-1]，所以 i 倒序遍历，j 正序遍历
- 边界：j - i <= 1 时（单个字符或两个相邻字符），只需判断 s[i] == s[j]

## 教训
- 看到"回文子串计数" → 中心扩展法最简洁，奇偶合并代码更短
- DP 法时间 O(n²)、空间 O(n²)，中心扩展时间 O(n²)、空间 O(1)
- 和 5 题对比：5 是求最长回文子串（中心扩展+记录边界），647 是求回文子串个数（中心扩展+计数）
