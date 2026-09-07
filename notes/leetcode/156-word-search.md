# LeetCode 79 单词搜索

## 我的思路（60分钟）
- 前20分钟：想到 DFS，但先尝试 BFS，越写越乱，放弃
- 中间20分钟：改用 DFS，但细节处理不到位
- 中间10分钟看答案，发现两个关键问题：
  - 变量作用域问题：试图用一个变量维护是否找到最后一个字母，但忽略了该变量不是全局变量，DFS 递归返回的结果需要用 or 连接
  - 路径标记后没有复原：访问过的格子标记为空后，在递归返回时没有恢复，导致后续搜索路径被错误阻断
- 后10分钟：重写代码，修复上述问题后通过

## 代码
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i, j, k):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            board[i][j] = ''  # 标记已访问
            res = (dfs(i + 1, j, k + 1) or 
                   dfs(i - 1, j, k + 1) or 
                   dfs(i, j + 1, k + 1) or 
                   dfs(i, j - 1, k + 1))
            board[i][j] = word[k]  # 恢复标记（回溯）
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
```

## 关键
- DFS + 回溯：从每个格子出发，向上下左右四个方向递归搜索
- 剪枝：边界检查 + 字符不匹配直接返回 False
- 标记与恢复：board[i][j] = '' 标记已访问，递归返回后 board[i][j] = word[k] 恢复，避免影响其他路径
- 终止条件：k == len(word) - 1 且字符匹配，返回 True

## 教训
- 看到"矩阵中搜索单词/路径" → DFS + 回溯，不要想 BFS（BFS 适合最短路径，不适合路径存在性）
- 回溯三要素：标记当前节点 → 递归搜索邻居 → 恢复当前节点标记
- 忘记恢复标记会导致后续搜索无法经过已访问的格子，即使该格子是另一条合法路径的一部分

## 搜索算法选择对比
| 题目          | 场景              | 方法           | 核心特征                |
| :---------- | :-------------- | :----------- | :------------------ |
| 200 岛屿数量    | 连通块计数           | DFS/BFS      | 标记访问，计数             |
| 329 最长递增路径  | 矩阵递增路径          | DFS + 记忆化    | 缓存子问题结果             |
| **79 单词搜索** | **矩阵中是否存在某条路径** | **DFS + 回溯** | **标记+恢复，四方向 or 连接** |
| 127 单词接龙    | 最短变换路径          | BFS          | 逐位替换，最短步数           |
