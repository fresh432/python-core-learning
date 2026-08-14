# LeetCode 200 岛屿数量

## 我的思路（40分钟）
- 前20分钟：完全没思路，不知道如何统计独立的连通块
- 后20分钟：看了提示，核心思路是DFS 放火——遍历网格，每遇到一个未被访问过的 '1'（陆地），就启动 DFS 把与它横竖相邻的所有 '1' 全部"烧掉"（标记为已访问），每烧一次就代表一个独立的岛屿

## 代码
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        def makefire(x, y):
            grid[y][x] = "2"  # 标记为已访问（烧过）
            if y + 1 < m and grid[y + 1][x] == '1':
                makefire(x, y + 1)
            if x + 1 < n and grid[y][x + 1] == '1':
                makefire(x + 1, y)
            if y - 1 >= 0 and grid[y - 1][x] == '1':
                makefire(x, y - 1)
            if x - 1 >= 0 and grid[y][x - 1] == '1':
                makefire(x - 1, y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    makefire(j, i)
                    ans += 1
        
        return ans
```

## 关键
- DFS  flood fill：从一个未访问的陆地出发，向上下左右四个方向递归蔓延，把所有连通的陆地标记为已访问
- 标记方式：将访问过的 '1' 改为 '2'（或 '0'），避免重复访问和死循环
- 统计逻辑：外层双重循环每遇到一个 '1' 就启动一次 DFS，ans += 1，最终 ans 就是岛屿数量

## 教训
- 看到"网格中连通块的数量" → DFS/BFS flood fill，遍历网格 + 标记已访问
- 方向数组可以用 [(0,1),(1,0),(0,-1),(-1,0)] 简化四个方向的判断
- 注意坐标不要搞混：grid[y][x] 还是 grid[i][j]，保持一致
- 和 695 题对比：200 是统计连通块个数，695 是统计连通块的最大面积