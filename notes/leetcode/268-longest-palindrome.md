# LeetCode 409 最长回文串

## 我的思路（9分钟）
- 先对所有字符计数，然后遍历所有计数
- 计数为偶数时直接加到 ans；计数为奇数时减一再加（凑成偶数对）
- 遍历完后若存在奇数计数，返回时多加一个 1（奇数个字符只能有一个放中心，其余奇数字符都要减一成偶数对，仅保留一个奇数字符）

## 代码
```python
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        ans = 0
        flag = 0
        for cnt in counts.values():
            if cnt % 2 == 0:
                ans += cnt
            else:
                flag = 1
                ans += (cnt - 1)
        return ans + flag
```

## 关键
- 偶数计数全取；奇数计数取 cnt - 1
- flag 记录是否存在奇数计数，存在则中心可以多放一个

## 教训
- 看到"能拼成多长的回文串" → 计数：偶数全取、奇数取 cnt-1、留一个中心
- 和 5/647 对比：5/647 是找已有回文（中心扩展），409 是构造回文（计数配对）——一个是"找"一个是"凑"