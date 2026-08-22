# LeetCode 542 01 矩阵

## 我的思路（60分钟）
- 前30分钟：想从 1 出发找最近的 0，但不知道如何避免距离被重复覆盖，思路卡死
- 中间15分钟：看答案，核心洞察——反向思维：从所有 0 出发往 1 扩散，思路和 994 的橘子类似，跑一层赋一次距离值，天然保证最短距离
- 后15分钟：理解并自己写了一遍

## 代码
```python
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        visited = [[0] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        
        # 所有 0 入队作为多源起点
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                if mat[x][y] == 1:
                    res[x][y] = step  # 当前层数就是最短距离
                
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= m or newy < 0 or newy >= n or visited[newx][newy] == 1:
                        continue
                    queue.append((newx, newy))
                    visited[newx][newy] = 1
            
            step += 1
        
        return res
```

## 关键
- 多源 BFS：所有 0 同时入队作为起点，visited 标记已访问
- 按层扩散：size = len(queue) 控制每层步数一致，step 记录当前层数（距离）
- 遇到 1 时：res[x][y] = step，由于 BFS 的层次特性，第一次访问就是最短距离
- 反向思维：不从 1 找 0，而是从 0 扩散到 1

## 教训
- 看到"矩阵中每个点到最近 0 的距离" → 多源 BFS，所有 0 同时入队
- 正向（从1找0）会重复覆盖且复杂，反向（从0扩散到1）天然保证最短
- 按层遍历（size = len(queue)）是 BFS 记录距离的标准写法
- 和 994 题对比：两题都是多源 BFS，994 的扩散目标是新鲜橘子，542 的扩散目标是 1，核心套路完全一致

## BFS 系列总结
|       题目      | BFS 类型     | 起点          | 扩散目标        | 核心技巧        |
| :-----------: | :--------- | :---------- | :---------- | :---------- |
|    127 单词接龙   | 单源 BFS     | `beginWord` | 字典中差一个字母的单词 | 逐位替换        |
| **994 腐烂的橘子** | **多源 BFS** | **所有腐烂橘子**  | **新鲜橘子**    | **队列带时间戳**  |
| **542 01 矩阵** | **多源 BFS** | **所有 0**    | **1**       | **按层扩散记步数** |
