# LeetCode 417 太平洋大西洋水流问题

## 我的思路（110分钟）
- 前10分钟：确定思路——从两个海洋的边界逆流而上（从低到高或等高），分别标记能流到太平洋和大西洋的格子，最后取两个集合的交集
- 中间90分钟：调试地狱，犯了三个致命错误：
  1. 只保留了"最高点"而不是路过的每个节点——应该用一个集合保存所有能到达的坐标
  2. 开始以为只能向对向流动，忽略了四个方向都可以逆流
  3. 忘记跳过已走过的节点（用 past 集合判重），导致 DFS 无限循环超时
- 后10分钟：逐一排查修复，终于通过

## 代码
```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()  # 能流到太平洋的坐标
        s = set()  # 能流到大西洋的坐标
        m, n = len(heights), len(heights[0])
        
        def flow(i, j, past):
            if (i, j) in past:
                return
            past.add((i, j))
            # 四个方向逆流：下一个格子高度 >= 当前
            if i + 1 < m and heights[i][j] <= heights[i + 1][j]:
                flow(i + 1, j, past)
            if j + 1 < n and heights[i][j] <= heights[i][j + 1]:
                flow(i, j + 1, past)
            if i - 1 >= 0 and heights[i][j] <= heights[i - 1][j]:
                flow(i - 1, j, past)
            if j - 1 >= 0 and heights[i][j] <= heights[i][j - 1]:
                flow(i, j - 1, past)
        
        # 太平洋边界：左边界 + 上边界
        fp = [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]
        # 大西洋边界：右边界 + 下边界
        fs = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)]
        
        for a, b in fp:
            flow(a, b, p)
        for a, b in fs:
            flow(a, b, s)
        
        return list(p & s)  # 交集
```

## 关键
- 逆向思维：不从内部往海洋流，而是从海洋边界往内部逆流（高度递增或相等）
- 两个集合 p 和 s：分别保存能到达太平洋和大西洋的所有坐标
- DFS 条件：heights[i][j] <= heights[ni][nj]（逆流，从低到高或等高）
- 判重集合 past：避免重复访问和无限循环
- 结果：两个集合的交集 p & s

## 教训
- 看到"水流/能到达两个边界" → 逆向思维：从边界逆流而上，正向从每个点往海洋流会超时
- DFS 必须加判重（set 或标记数组），否则在等高区域会死循环
- 水流是四个方向的，不要限制为对向方向
- 要保存所有路过的节点，不是只保存最高点
- 和 130 题对比：130 是从边界标记不被围绕的 O，417 是从边界标记能到达的格子——都是反向标记 + 集合交集/更新

