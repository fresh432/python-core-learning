# LeetCode 79 单词搜索（复习）

## 我的思路（20分钟）
- 前5分钟：先写剪枝
  - 统计矩阵和字符串的字母数量，字符串中某字母比矩阵多则直接返回 False
  - 比较字符串首尾字符的数量，尾部字符更少则反转字符串（起点更少，时间更优）
- 主体：DFS 遍历，匹配到字母就把该位置字符置空代替 visited 数组防止走回头路；用方向数组移动坐标；任一分支返回 True 则直接返回 True；全部失败则恢复原值回溯并返回 False；匹配下标到达字符串末尾即成功
- 中间逻辑全对，但矩阵长度和字符串长度的变量不小心写成同一个，调试了几分钟

## 代码
```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # 剪枝1：字母数量统计
        cnt_b, cnt_w = Counter(w for row in board for w in row), Counter(word)
        for k in cnt_w.keys():
            if cnt_b[k] < cnt_w[k]:
                return False 
        # 剪枝2：首尾字符出现少的放前面，减少起点数
        if cnt_w[word[0]] > cnt_w[word[-1]]:
            word = word[::-1]

        move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(board), len(board[0])
        if m * n < len(word): return False
        def dfs(i, j, index):
            if board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[i][j] = ""    # 置空代替 visited
            for mi, mj in move:
                ci, cj = i + mi, j + mj
                if 0 <= ci < m and 0 <= cj < n and dfs(ci, cj, index + 1):
                    return True
            board[i][j] = word[index]   # 回溯恢复
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
```

## 关键
- DFS 回溯三件套：置空标记走过的格、方向数组四向移动、失败恢复格子原值
- 剪枝：字母数量统计 + 首尾字符频次（少的端点做起点，减少搜索量）
- 成功判定：index 到达字符串末尾

## 教训
- 看到"矩阵中找单词" → DFS 回溯 + 置空防走回头路 + 数量剪枝
- 调试教训：矩阵行列数和字符串长度这类"不同含义的长度变量"命名要区分，写混了很难发现