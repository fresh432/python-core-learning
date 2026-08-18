# LeetCode 684 冗余连接

## 我的思路（60分钟）
- 前15分钟：构造并查集类，复用 547 题的模板
- 中间30分钟：思路错误——想的是添加边时直接把 pre 作为 cur 的根节点，如果 cur 已在字典里就把当前边作为答案。但这样没考虑其他独立的树，导致逻辑不完整
- 后10分钟：查资料发现正确做法——pre 和 cur 都单独添加到并查集中，然后尝试合并，如果两者根相同说明已形成环，当前边就是冗余边
- 最后5分钟：修改代码，通过

## 代码
```python
class UnionFind:
    def __init__(self):
        self.father = {}
        self.ans = []
    
    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]
        while root != x:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
    
    def add(self, pre, cur):
        if pre not in self.father:
            self.father[pre] = None
        if cur not in self.father:
            self.father[cur] = None
        root_pre, root_cur = self.find(pre), self.find(cur)
        if root_pre == root_cur:
            self.ans = [pre, cur]  # 形成环，记录冗余边
        else:
            self.merge(pre, cur)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for pre, cur in edges:
            uf.add(pre, cur)
        return uf.ans
```

## 关键
- 并查集判环：遍历每条边 (u, v)，如果 u 和 v 已经在同一个集合中，加入这条边就会形成环，该边即为冗余边
- add 方法的核心：
  1. 将两个节点都加入并查集（若不存在）
  2. 查找两者的根
  3. 根相同 → 记录为答案（冗余边）
  4. 根不同 → 合并两个集合
- 为什么题目保证有唯一答案：树有 n-1 条边，现在给了 n 条，多余的一条就是冗余边

## 教训
- 看到"无向图找冗余边/成环边" → 并查集，遍历边时判环
- 并查集 add 时两个节点都要独立加入，不能只处理一个，否则独立子树无法正确合并
- 和 547 题对比：547 是统计连通分量个数，684 是找形成环的那条边——并查集的两种典型应用

## 图论算法对比（更新）
|       题目       | 图类型     | 目标       | 方法              | 核心                   |
| :------------: | :------ | :------- | :-------------- | :------------------- |
|    547 省份数量    | 无向图     | 连通分量个数   | 并查集 / DFS       | `num_of_sets`        |
|     207 课程表    | 有向图     | 是否存在环    | DFS 三色标记        | `flags` 状态           |
| **210 课程表 II** | **有向图** | **拓扑排序** | **BFS Kahn 算法** | **`indegrees` + 队列** |
|  **684 冗余连接**  | **无向图** | **找冗余边** | **并查集判环**       | **`find` 根相同 = 环**   |
