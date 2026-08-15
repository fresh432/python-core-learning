# LeetCode 463 岛屿的周长

## 我的思路（40分钟）
- 前25分钟：用 DFS flood fill 写出初版，遍历每个陆地格子的四个方向，遇到边界或水域（'0'）就认为该边是周长的一部分，self.res += 1。因为调整了写法，调试边界花了点时间
- 中间10分钟：看别人的更优解，发现根本不需要 DFS——直接遍历 + 对边判断即可。因为没有内陆湖，一条边的上边和下边长度相同、左边和右边长度相同，所以只需判断上方和左方
- 后5分钟：重写优化版，上方/左方遇到边界或水域就 +2（同时把对边也计算进去）

## 代码（初版 — DFS）
```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0
        m, n = len(grid), len(grid[0])
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def calculate(y, x):
            grid[y][x] = 2
            for a, b in move:
                mi, mj = y + a, x + b
                if (mi >= m) or (mi < 0) or (mj >= n) or (mj < 0) or grid[mi][mj] == 0:
                    self.res += 1
                    continue
                elif grid[mi][mj] == 1:
                    calculate(mi, mj)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    calculate(i, j)
                    return self.res
```

## 代码（优化版 — 直接遍历）
```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    continue
                # 上方：如果是第一行或上方是水域，则上边+下边 = +2
                if i == 0 or grid[i - 1][j] == 0:
                    ans += 2
                # 左方：如果是第一列或左方是水域，则左边+右边 = +2
                if j == 0 or grid[i][j - 1] == 0:
                    ans += 2
        
        return ans
```

## 关键
- DFS 版：从一个陆地出发，向四个方向探索，每遇到边界/水域就 +1，标记已访问避免重复
- 优化版核心洞察：没有内陆湖 → 每条边有且仅有一个对边，只需判断上方和左方：
  - 上方是边界/水域 → 上边和下边都是周长 → +2
  - 左方是边界/水域 → 左边和右边都是周长 → +2

## 教训
- 看到"岛屿周长" → 先想优化解法，对边判断比 DFS 更简洁高效
- 和 200/695 题对比：200 是连通块计数，695 是连通块面积，463 是连通块周长——都是网格 DFS，但统计目标不同
