# LeetCode 140 单词拆分 II

## 我的思路（20分钟）
- 前5分钟：读完题立刻判断这是"求所有方案"，直觉上回溯法
- 后15分钟：写出回溯框架，start 参数控制当前扫描位置，尝试所有可能的单词切片，如果在字典中就加入路径并递归，到达字符串末尾时将路径加入结果集

## 代码
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        ans = []
        path = []
        
        def func(start):
            if start == n:
                ans.append(" ".join(path))
                return
            for i in range(start, n):
                if s[start:i+1] in wordDict:
                    path.append(s[start:i+1])
                    func(i + 1)
                    path.pop()
        
        func(0)
        return ans
```

## 关键
- 回溯三要素：
  - 参数：start 表示当前从 s 的哪个位置开始扫描
  - 终止条件：start == n 时，说明已拆分完所有字符，将 path 用空格连接加入 ans
  - 选择：for i in range(start, n)，切片 s[start:i+1] 判断是否在字典中
- 状态维护：path.append() 做选择，path.pop() 撤销选择（标准回溯模板）

## 教训
- 139 判断"能否" → 用 DP；140 求"所有方案" → 用回溯，这是经典的"判定问题 vs 枚举问题"组合
- 当前回溯解法在最坏情况下是指数级复杂度（O(2ⁿ)），如果测试用例很强会 TLE
- 优化方向：先用 139 题的 DP 预处理判断 s 是否可被拆分（剪枝），或给回溯加 记忆化搜索（@cache 记录 start 位置的所有拆分结果），可将复杂度降至多项式级别
- wordDict 务必先转成 set，将查找优化到 O(1)

## 和 139 题的对比
|        题目       | 目标         | 方法 | 状态设计               |     复杂度    |
| :-------------: | :--------- | :- | :----------------- | :--------: |
|     139 单词拆分    | **能否**拆分成功 | DP | `dp[i]` 布尔值，前缀可否到达 |   `O(n²)`  |
| **140 单词拆分 II** | **所有**拆分方案 | 回溯 | `path` 列表，收集当前路径   | `O(2ⁿ)` 最坏 |
