# LeetCode 79 单词搜索（复习+剪枝优化）

## 我的思路（53分钟）
- 前20分钟：写出基础 DFS + 回溯，维护 visited 数组，传坐标和 word 下标。匹配到最后一个字符返回 True，否则四方向递归，用 flag 标记是否有解，返回前恢复 visited
- 中间18分钟：调试地狱，始终不返回 True。查到最后发现 flag 拼写成了 falg，改完后通过
- 后10分钟：看剪枝优化：
  1. 字母计数剪枝：用 Counter 统计 board 和 word 的字母数量，若 board 中某字母少于 word 中所需，直接返回 False
  2. 反向搜索剪枝：比较 word 首尾字母在 board 中的数量，较少的那个打头阵（反向搜索），减少 DFS 分支
- 后5分钟：添加剪枝优化并优化部分判断逻辑，从 3654ms → 347ms

## 代码（基础版）
```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j, index):
            if visited[i][j] == 1:
                return False
            if word[index] == board[i][j]:
                visited[i][j] = 1
                if index == len(word) - 1:
                    return True
            else: return False
            flag = 0
            for mi, mj in move:
                ci, cj = i + mi, j + mj
                if 0 <= ci < m and 0 <= cj < n and dfs(ci, cj, index + 1):
                    flag = 1
            visited[i][j] = 0
            return True if flag == 1 else False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False
```

## 代码（剪枝优化版）
```python
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = Counter(c for row in board for c in row)
        if cnt < Counter(word):
            return False
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]
        
        m, n = len(board), len(board[0])
        if m * n < len(word):
            return False
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j, index):
            if word[index] != board[i][j]:
                return False
            if index == len(word) - 1:
                return True
            board[i][j] = ""
            for mi, mj in move:
                ci, cj = i + mi, j + mj
                if 0 <= ci < m and 0 <= cj < n and dfs(ci, cj, index + 1):
                    return True
            board[i][j] = word[index]
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
```

## 关键
- 剪枝1：cnt < Counter(word)，board 中字母不够直接返回 False
- 剪枝2：cnt[word[-1]] < cnt[word[0]] 时反转 word，从出现次数少的字母端开始搜索，减少分支
- 剪枝3：m * n < len(word)，board 格子数不够直接返回 False
- 原地标记：board[i][j] = "" 代替 visited 数组，节省空间

## 教训
- 看到"矩阵中搜索单词" → DFS + 回溯 + 剪枝（字母计数 + 反向搜索）
- 拼写检查：flag 不要写成 falg，调试18分钟的血泪教训
- 和第一次做 79 题对比：第一次只写了基础 DFS，这次加了剪枝优化，时间从 3654ms → 347ms
