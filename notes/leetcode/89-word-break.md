# LeetCode 139 单词拆分

## 我的思路（60分钟）
- 前10分钟：直觉想到二维数组保存状态，试图用 dp[i][j] 记录每个子串的拆分情况
- 中间30分钟：卡在"如何维护上一个有效状态的下标"，逻辑越写越复杂，始终无法正确转移
- 后20分钟：看答案发现完全不需要二维——一维布尔数组即可，dp[i] 直接表示前缀 s[0:i] 能否被拆分，内层遍历终点 j，通过 s[i:j] 切片判断，豁然开朗后写出代码

## 代码
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空串可以被拆分
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        
        return dp[-1]
```

## 关键
- 状态定义：dp[i] = 字符串 s[0:i]（前 i 个字符）能否被拆分成字典中的单词
- 状态转移：若 dp[i] 为 True 且子串 s[i:j] 在 wordDict 中，则 dp[j] = True
- 初始化：dp[0] = True（空串视为可拆分，作为递推起点）
- 遍历方式：外层 i 为起点，内层 j 为终点，切片 s[i:j] 判断——本质是区间 DP 的一维压缩

## 教训
- 看到"字符串能否被拆分成若干合法子串" → 先想一维 DP，不要本能上二维
- 二维思维的陷阱：试图用 dp[i][j] 记录所有子串状态，但本题只需要知道"前缀能否到达"，一维足够
- dp[0] = True 是核心桥梁，没有它整个递推无法启动
- 时间复杂度 O(n²)（切片查找视 wordDict 结构而定，用 set 可优化到平均 O(1)）

