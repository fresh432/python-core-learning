# LeetCode 547 省份数量

## 我的思路（70分钟）
- 前20分钟：试图用矩阵秩来求，感觉实现复杂，放弃
- 中间30分钟：看答案了解并查集（Union-Find），理解 find（路径压缩）+ merge（合并集合）+ num_of_sets（集合计数）的核心机制
- 后10分钟：跟着模板写出并查集解法
- 最后10分钟：又看了 DFS 感染法——遍历每个节点，未访问就启动 DFS 标记所有连通节点，ans += 1，然后自己重写了一遍 DFS 版

## 代码（并查集版）
```python
class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0
    
    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]
        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind()
        
        for i in range(n):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)
        
        return uf.num_of_sets
```

## 代码（DFS 版）
```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)
        
        ans = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1
        
        return ans
```

## 关键
- 并查集：维护连通分量的集合，每次 merge 减少一个集合数，最终 num_of_sets 就是省份数
- DFS 感染法：和 200 题（岛屿数量）几乎一样，只是邻接关系由矩阵给出而非网格坐标
- 路径压缩：find 时把沿途节点的父节点直接指向根，加速后续查询

## 教训
- 看到"无向图连通分量个数" → 并查集或 DFS/BFS 遍历，两种都要会
- 并查集模板要熟记：find（带路径压缩）+ merge + add，num_of_sets 维护集合数
- 矩阵只遍历下三角（j in range(i)）避免重复合并
- 并查集 vs DFS：并查集适合动态连通性问题，DFS 适合一次性统计连通块

