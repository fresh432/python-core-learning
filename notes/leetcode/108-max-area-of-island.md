# LeetCode 695 岛屿的最大面积

## 我的思路（10分钟）
- 和 200 题几乎完全一样，只是需要在 DFS 过程中统计每个连通块的面积
- 花了点时间调试 count 的作用域问题——用 self.count 在嵌套函数中共享变量

## 代码
```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        self.count = 0
        
        def makefire(y, x):
            grid[y][x] = 2
            self.count += 1
            if y + 1 < m and grid[y + 1][x] == 1:
                makefire(y + 1, x)
            if x + 1 < n and grid[y][x + 1] == 1:
                makefire(y, x + 1)
            if y - 1 >= 0 and grid[y - 1][x] == 1:
                makefire(y - 1, x)
            if x - 1 >= 0 and grid[y][x - 1] == 1:
                makefire(y, x - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.count = 0
                    makefire(i, j)
                    ans = max(ans, self.count)
        
        return ans
```

## 关键
- 在 200 题的基础上，DFS 内部增加 self.count += 1，每访问一个陆地格子面积 +1
- 每次启动新的 DFS 前重置 self.count = 0
- 用 self.count 解决嵌套函数作用域问题（或用 nonlocal）

## 教训
- 看到"网格中最大连通块面积" → 在 flood fill 基础上计数即可
- Python 嵌套函数修改外部变量：用 self.xxx 或 nonlocal，直接用 count += 1 会报 UnboundLocalError
- 和 200 题对比：

|       题目       | 目标            | DFS 内部操作      | 结果                |
| :------------: | :------------ | :------------ | :---------------- |
|    200 岛屿数量    | 统计连通块个数       | 标记访问          | 启动 DFS 的次数        |
| **695 岛屿最大面积** | **统计最大连通块面积** | **标记访问 + 计数** | **所有 count 的最大值** |
