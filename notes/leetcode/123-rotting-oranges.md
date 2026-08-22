# LeetCode 994 腐烂的橘子

## 我的思路（60分钟）
- 前30分钟：纠结如何保存腐烂时间，想过把时间和坐标一起保存，但又想用一个临时队列来保存每分钟感染的橘子，再统一把时间加一，然后传回主队列——思路绕来绕去，写不出来
- 后15分钟：看答案，发现就是一开始的想法——队列直接存 (i, j, time)，每个橘子带着自己的腐烂时间入队
- 后15分钟：写出代码并通过

## 代码
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m, n, time = len(grid), len(grid[0]), 0
        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # 所有腐烂橘子入队
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        
        while queue:
            i, j, time = queue.pop(0)
            for a, b in move:
                mi, mj = i + a, j + b
                if 0 <= mi < m and 0 <= mj < n and grid[mi][mj] == 1:
                    grid[mi][mj] = 2  # 变腐烂
                    queue.append((mi, mj, time + 1))
        
        # 检查是否还有新鲜橘子
        for row in grid:
            if 1 in row:
                return -1
        
        return time
```

## 关键
- 多源 BFS：所有腐烂橘子同时入队，作为 BFS 的多个起点
- 队列元素：(i, j, time)，当前橘子的坐标和腐烂时间
- 扩散条件：相邻格子是新鲜橘子（== 1），将其变腐烂（== 2）并入队，time + 1
- 最后检查：若还有 1 则返回 -1（无法全部腐烂）

## 教训
- 看到"网格中多源扩散 / 最短分钟数" → 多源 BFS，所有起点同时入队，队列直接带时间戳
- 不要过度设计临时队列，(i, j, time) 三元组足够
- 和 127 题对比：127 是单源 BFS（从一个单词出发），994 是多源 BFS（多个腐烂橘子同时扩散）