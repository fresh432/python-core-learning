# LeetCode 329 矩阵中的最长递增路径

## 我的思路（40分钟）
- 前20分钟：写出 DFS 框架，从每个格子出发向四个方向走，只往更大的值走
- 中间10分钟：调试记忆化部分，忘记了字典赋值直接用 = 即可，走了弯路
- 后10分钟：优化计数逻辑——之前通过参数传递计数，改为局部变量返回的方式，代码更清晰

## 代码
```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        visited = {}  # 记忆化：缓存每个位置的最长递增路径长度
        
        def dfs(i, j):
            if (i, j) in visited:
                return visited[(i, j)]
            
            res = 1  # 当前格子自身算长度1
            for mi, mj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + mi, j + mj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            
            visited[(i, j)] = res
            return res
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans
```

## 关键
- 记忆化搜索（Memoization）：visited[(i, j)] 缓存从 (i, j) 出发的最长递增路径长度，避免重复计算
- DFS 方向：只往严格更大的值走（matrix[ni][nj] > matrix[i][j]），天然保证无环，不需要判重
- 返回值设计：dfs 返回从当前位置出发的最长路径长度，局部变量 res 初始为 1（当前格子），然后取四个方向的最大值 +1

## 教训
- 看到"矩阵中最长递增路径" → 记忆化搜索 + DFS，每个位置的结果只依赖更大邻居的结果
- 记忆化搜索的本质：自顶向下的 DP，用字典/数组缓存子问题结果
- 参数传递计数 vs 局部变量返回：后者更清晰，res = max(res, 1 + dfs(...)) 是标准写法
- 和 120 题（三角形最小路径）对比：120 是自底向上 DP，329 是自顶向下记忆化搜索——两种 DP 实现方式

## 和 200/695 等网格 DFS 对比
|       题目       | 遍历方向          |         记忆化        | 核心特征       |
| :------------: | :------------ | :----------------: | :--------- |
|    200 岛屿数量    | 四方向（相同值）      |        标记访问        | 连通块计数      |
|    695 岛屿面积    | 四方向（相同值）      |        标记+累加       | 连通块面积      |
| **329 最长递增路径** | **四方向（严格更大）** | **`visited` 缓存长度** | **最长递增路径** |

