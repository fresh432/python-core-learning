# LeetCode 77 组合

## 我的思路（60分钟）
1. 前20分钟：没有思路，不知道"从 n 个数中选 k 个"怎么系统枚举
2. 中间30分钟：看答案，第一种回溯解法看了很久才理解——递归选或不选，每次从 i 开始往后选，避免重复
3. 后10分钟：理解剪枝优化——当剩余数字不够凑够 k 个时，直接返回

## 基础解法（回溯）
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        
        def func(i):
            if k == len(path):      # 选够了 k 个
                ans.append(path[:])
                return
            
            for j in range(i, n + 1):
                path.append(j)
                func(j + 1)         # 从下一个数开始选，避免重复
                path.pop()          # 回溯
        
        func(1)
        return ans
```

## 剪枝优化
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        
        def func(i):
            d = k - len(path)       # 还需要选 d 个
            if d == 0:
                ans.append(path[:])
                return
            
            # 剪枝：如果 i > d，说明 i 太大，选 d 个不够
            if i > d:
                func(i - 1)
            
            path.append(i)
            func(i - 1)
            path.pop()
        
        func(n)
        return ans
```

## 关键
- 回溯模板：选择（append）→ 递归 → 撤销选择（pop）
- 避免重复：func(j + 1) 保证每次从当前数的后面选，组合不讲究顺序
- 剪枝：d = k - len(path) 计算还需选几个，i > d 时说明当前数太大，即使全选也不够

## 教训
- 看到"从 n 选 k" → 回溯法，核心是"选或不选"的递归树
- 剪枝是回溯的灵魂，能大幅减少搜索空间
- 和 113 题（路径总和 II）对比：都是回溯，但 113 是"找路径"，77 是"选组合"