# LeetCode 767 重构字符串（复习）

## 我的思路（5分钟）
- 先统计所有字符的频数；频数最多的字符若大于字符串长度一半，就绝对会相邻，直接返回空字符串
- 按频数从大到小填充偶数下标，偶数位填满后换成奇数位
- 前面已判定最大频数不超过一半，把大的全填偶数位不可能出现相邻

## 代码
```python
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s).most_common()
        if counts[0][1] > (n + 1) // 2:
            return ""
        i = 0
        ans = [""] * n
        for ch, cnt in counts:
            for _ in range(cnt):
                ans[i] = ch
                i += 2
                if i >= n:
                    i = 1
        return "".join(ans)
```

## 教训
- 复习： 5 分钟一遍过（40 → 6 → 5 分钟），"半数判定 + 奇偶位填充"已掌握
- 这是典型的"可行性定理 + 构造性填充"两步套路，可迁移到类似的间隔排列题