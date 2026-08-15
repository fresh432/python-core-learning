# LeetCode 130 被围绕的区域

## 我的思路（50分钟）
- 前30分钟：正向思维——先把所有 'O' 变成 'X' 并保存坐标，然后找到边界上的 'O' 再恢复成 'O'。虽然通过了，但时间很差（135 ms，击败 5.35%）
- 中间10分钟：看优化代码，发现应该反过来——先找边界上的 'O'，用 DFS 把所有与边界连通的 'O' 标记为特殊符号（如 '#'），这些是不被围绕的；最后遍历矩阵，'O' 变 'X'（被围绕的），'#' 变 'O'（恢复的）
- 后10分钟：重写优化版，时间大幅优化（7 ms）

## 代码（优化版）
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        
        def dfs(y, x):
            if y >= m or y < 0 or x >= n or x < 0 or board[y][x] != "O":
                return
            board[y][x] = "#"  # 标记为与边界连通
            dfs(y + 1, x)
            dfs(y - 1, x)
            dfs(y, x + 1)
            dfs(y, x - 1)
        
        # 从四条边界的 'O' 出发 DFS
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == "O":
                    dfs(i, j)
        
        # 统一更新
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"      # 被围绕的变 X
                elif board[i][j] == "#":
                    board[i][j] = "O"      # 恢复的变 O
```

## 关键
- 反向思维：不找"被围绕的"，而是找"不被围绕的"（与边界连通的 'O'）
- 步骤：
  1. 从四条边界的 'O' 出发 DFS，标记所有连通的 'O' 为 '#'
  2. 遍历整个矩阵：'O' → 'X'（被围绕），'#' → 'O'（恢复）
- 为什么反向更快：边界上的 'O' 数量远少于内部，DFS 范围小

## 教训
- 看到"矩阵中被围绕的区域" → 反向思维：从边界出发标记不被围绕的，最后统一更新
- 正向思维（先全变再恢复）虽然能过，但代码复杂、时间差
- 和 200/695/463 题对比：都是网格 DFS，但 130 的核心是反向标记 + 统一更新