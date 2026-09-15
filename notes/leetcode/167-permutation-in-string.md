# LeetCode 567 字符串的排列

## 我的思路（50分钟）
- 前10分钟：想到用 76 题的反向记录 + ge_cnt 维护方法，但想尝试换成数组记录频率优化，10分钟后感觉实现不了，放弃
- 中间20分钟：低级错误排查——统计 cnt_s1 种类数的语句写在了哈希表记录 s1 数据前面，导致 ge_cnt 一直为 0，误以为是逻辑问题，排查了 20 分钟
- 后10分钟：又一个低级错误——ge_cnt 减一的逻辑写在了弹出左窗口字符逻辑的后面，导致窗口收缩时判断错误，又调试 10 分钟，解决后通过

## 代码
```python
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = defaultdict(int)
        n, m = len(s1), len(s2)
        
        for char in s1:
            cnt_s1[char] -= 1
        
        ge_cnt = len(cnt_s1)  # s1 中不同字符的种类数
        
        for i in range(m):
            left = i - n + 1
            
            if s2[i] in cnt_s1:
                cnt_s1[s2[i]] += 1
                if cnt_s1[s2[i]] == 0:
                    ge_cnt -= 1
            
            if left < 0:
                continue
            
            if ge_cnt == 0:
                return True
            
            if s2[left] in cnt_s1:
                if cnt_s1[s2[left]] == 0:
                    ge_cnt += 1
                cnt_s1[s2[left]] -= 1
        
        return False
```

## 关键
- 反向记录：先遍历 s1，cnt_s1[char] -= 1（需求为负）
- ge_cnt：初始值为 s1 中不同字符种类数，当某个字符计数从负变零时 ge_cnt -= 1
- 窗口固定长度 len(s1)：右指针遍历 s2，左指针 i - n + 1
- 满足条件：ge_cnt == 0，说明 s1 中所有字符种类都刚好满足
- 移出左边界：若移出前 cnt_s1[x] == 0，移出后变负，ge_cnt += 1

## 教训
- 看到"判断 s2 是否包含 s1 的排列" → 固定长度滑动窗口 + 反向哈希表 + ge_cnt
- 低级错误：ge_cnt = len(cnt_s1) 必须在哈希表填充之后，左边界移出的 ge_cnt += 1 必须在 cnt_s1[x] -= 1之前
- 和 438 题对比：438 也是定长窗口+字符频次，但 438 是比较两个计数数组是否相等，567 是用 ge_cnt 维护满足种类数

## 滑动窗口定长对比
| 题目             | 目标           | 核心技巧                | 判断条件              |
| :------------- | :----------- | :------------------ | :---------------- |
| 438 找到所有字母异位词  | 找所有异位词起始位置   | 字符计数数组              | `cnt_p == cnt_s`  |
| **567 字符串的排列** | **判断是否存在排列** | **反向哈希表 + ge\_cnt** | **`ge_cnt == 0`** |
