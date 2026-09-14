# LeetCode 5 最长回文子串

## 我的思路（60分钟）
- 前20分钟：想到暴力枚举（O(n³) 放弃）和中心扩展（从中间向两边扩展）。但误以为要从中点开始向两边扩展，且需要区分奇偶长度，觉得实现不了就没写
- 中间20分钟：看答案，Manacher 算法看不懂；看了中心扩展法——原来是从每个字符（及每对相邻字符）作为中心向两边扩展，不是只从中点扩展
- 后10分钟：理解后自己写了一遍
- 最后10分钟：尝试动态规划写法，无果

## 代码（中心扩展法）
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_left, ans_right = 0, 0
        
        # 奇数长度回文：中心是一个字符
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - 1) - (l + 1) + 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r
        
        # 偶数长度回文：中心是两个字符
        for i in range(n - 1):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - 1) - (l + 1) + 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r
        
        return s[ans_left:ans_right]
```

## 关键
- 中心扩展：枚举每个位置作为回文中心，向两边扩展直到不相等
- 奇偶两种情况：奇数长度中心是一个字符，偶数长度中心是两个相邻字符
- 扩展后 l 和 r 会多走一步，实际回文边界是 l+1 到 r-1
- 长度计算：(r - 1) - (l + 1) + 1 = r - l - 1

## 教训
- 看到"最长回文子串" → 中心扩展法，枚举每个字符作为中心向两边扩
- 不要只从中点开始扩展，要从每个位置都开始尝试
- Manacher 算法 O(n) 但代码复杂
- 和 234 题对比：234 是判断链表回文（找中点+反转+比较），5 是找最长回文子串（中心扩展）
