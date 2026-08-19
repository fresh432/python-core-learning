# LeetCode 802 找到最终的安全状态

## 我的思路（45分钟）
- 前30分钟：想正向拓扑排序，保存每个节点的出度，遍历邻接节点判断是否都是终端节点，发现逻辑走不通——正向无法判断"所有路径都到达终端"
- 中间5分钟：看答案，核心洞察——反向建图 + 拓扑排序：把原图所有边反向，原图的终端节点（出度为0）在反向图中入度为0，从它们出发反向可达的节点就是安全节点
- 后10分钟：根据反向图思路写出代码

## 代码
```python
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        ans = []
        
        # 计算原图每个节点的出度（作为反向图的入度）
        indegrees = [len(graph[i]) for i in range(n)]
        # 反向建图：原图 i -> j，反向图 j -> i
        adjacency = [[] for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                adjacency[j].append(i)
        
        queue = deque()
        # 原图出度为0的节点 = 反向图入度为0 = 终端节点，入队
        for i in range(n):
            if indegrees[i] == 0:
                queue.append(i)
        
        # Kahn 算法拓扑排序
        while queue:
            safe = queue.popleft()
            ans.append(safe)
            for i in adjacency[safe]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        
        return sorted(ans)
```

## 关键
- 安全节点定义：从该节点出发的所有路径都最终到达终端节点（出度为0）
- 反向图思路：
  - 原图：判断"从节点出发能否到达终端"很难（路径可能无限）
  - 反向图：判断"终端能否反向到达该节点"很容易（拓扑排序）
- 原图出度 = 反向图入度：入度为0的节点就是终端节点，拓扑排序后所有被访问到的节点都是安全节点
- 结果需要 sorted(ans)，因为拓扑排序不保证顺序

## 教训
看到"所有路径最终到达终点 / 安全状态" → 反向图 + 拓扑排序（Kahn）
正向思维卡壳时，立刻尝试反向建图，很多问题（如 417 太平洋大西洋）都适用
和 210 题对比：210 是正向拓扑排序（找入度为0的先修课），802 是反向拓扑排序（找出度为0的终端节点）

## 图论算法对比（更新）
|       题目      | 图类型     | 目标        | 方法             | 核心技巧              |
| :-----------: | :------ | :-------- | :------------- | :---------------- |
|    207 课程表    | 有向图     | 判环        | DFS 三色标记       | `flags` 状态        |
|   210 课程表 II  | 有向图     | 拓扑序       | BFS Kahn 正向    | `indegrees`       |
|    547 省份数量   | 无向图     | 连通分量      | 并查集 / DFS      | `num_of_sets`     |
|    684 冗余连接   | 无向图     | 找冗余边      | 并查集判环          | `find` 根相同        |
| **785 判断二分图** | **无向图** | **是否二分图** | **DFS 染色法**    | **`colors` 双色标记** |
|  **802 安全状态** | **有向图** | **找安全节点** | **反向图 + Kahn** | **原图出度 = 反向图入度**  |
