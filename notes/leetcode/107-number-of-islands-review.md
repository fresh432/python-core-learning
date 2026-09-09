# LeetCode 200 岛屿数量（复习）

## 我的思路（10分钟）
- 看到"岛屿"立刻想到 DFS 遍历连通块
- 6分钟写好核心逻辑：遇到 '1' 就启动 DFS，把连通的所有 '1' 标记为 '0'
- 踩坑：边界条件漏写了等号，导致 i == 0 或 j == 0 时不会进入 DFS，花了 4 分钟定位并修复

## 代码
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            grid[i][j] = '0'
            for mi, mj in move:
                ci, cj = mi + i, mj + j
                if 0 <= ci < m and 0 <= cj < n and grid[ci][cj] == '1':
                    dfs(ci, cj)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        
        return ans
```

## 关键
- DFS 标记访问：进入 DFS 立刻把当前格子改为 '0'，避免重复访问
- 四方向扩散：上下左右四个方向递归
- 边界检查：0 <= ci < m and 0 <= cj < n，注意等号不能漏

## 教训
- 看到"网格连通块计数" → DFS/BFS 均可，DFS 代码更短
- 边界条件 0 <= 的等号容易漏写，导致最外层行列无法遍历
- 复习价值：经典 DFS 模板，边界条件是易错点