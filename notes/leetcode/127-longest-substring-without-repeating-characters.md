# LeetCode 3 无重复字符的最长子串

## 我的思路（30分钟）
- 前15分钟：暴力解法，用哈希表记录字符，遇到重复就把哈希表清零，快指针回退到第一个重复位置的后一个位置——时间复杂度 O(n²)
- 后15分钟：改用滑动窗口，调试时卡在"字符没有重复时返回的答案会少一个"——后来发现是窗口长度计算或左边界初始化的问题

## 代码
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        ans, j = 0, 0
        
        for i, ch in enumerate(s):
            # 如果 ch 在窗口内重复，收缩左边界
            if ch in dic and dic[ch] >= j:
                j = dic[ch] + 1
            dic[ch] = i
            ans = max(ans, i - j + 1)
        
        return ans
```

## 关键
- 滑动窗口：j 是左边界，i 是右边界，窗口为 [j, i]
- dic[ch] 记录字符 ch 的最新下标
- 收缩条件：ch in dic and dic[ch] >= j —— 只有重复字符在当前窗口内才需要收缩左边界
- 窗口长度：i - j + 1

## 教训
- 看到"最长无重复子串" → 滑动窗口 + 哈希表记录最新下标
- 不要回退快指针（暴力），只移动左边界 j，保证 O(n)
- dic[ch] >= j 是关键判断，避免被窗口外的旧下标干扰
- 和 26 题对比：26 是快慢指针原地覆盖（有序数组去重），3 是滑动窗口动态收缩（最长无重复子串）