# LeetCode 767 重构字符串（复习）

## 我的思路（6分钟）
- 先将字符串中所有字符计数，如果出现次数最多的字符数量超过字符串长度的一半（(n+1)//2），就不可能全都不相邻，直接返回空字符串
- 可行性判定通过，则按出现次数从高到低填充：优先将字符串的偶数下标位填满，再切换奇数位继续填充
- 因为前面的判定已保证出现次数最多的字符小于字符串一半，所以隔位填充的方式不会出现相邻填充

## 代码
```python
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = Counter(s).most_common()   # 按频次降序
        max_cnt = counts[0][1]
        if max_cnt > (n + 1) // 2:          # 可行性判定
            return ""

        ans = [""] * n
        i = 0
        for ch, cnt in counts:
            for _ in range(cnt):
                ans[i] = ch
                i += 2                      # 先填偶数位
                if i >= n:                  # 偶数位填满，转奇数位
                    i = 1
        return "".join(ans)
```

## 教训
- 复习： 6 分钟一遍通过：可行性判定 + 奇偶位填充已完全掌握（首次 40 分钟 → 复习 6 分钟）
- 口诀："半数判定保可行，偶位先填奇位续"