# LeetCode 207 课程表

## 我的思路（50分钟）
- 前20分钟：想通过访问每个节点比对"最开始进入的节点"来判断是否有环，逻辑没理清楚，没实现出来
- 中间20分钟：看答案，核心思路是三色标记法 DFS 判环——用 flags 数组维护每个节点的状态：
  - 0：未访问
  - 1：正在访问（在当前 DFS 路径上）
  - -1：已访问且安全（无环）
- 后10分钟：自己写了一遍

## 代码
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1:  # 已访问且安全
                return True
            if flags[i] == 1:   # 在当前路径上又遇到，有环
                return False
            flags[i] = 1        # 标记为正在访问
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1       # 标记为安全
            return True
        
        # 建邻接表：pre -> cur（先修指向后续课程）
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        
        flags = [0] * numCourses
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        
        return True
```

## 关键
- 有向图判环：DFS + 三色标记是经典做法
- flags[i] == 1 时遇到 i：说明形成了回溯边，存在环，返回 False
- flags[i] == -1：该节点已确认安全，直接返回 True 剪枝
- 邻接表方向：pre -> cur（先修课程指向后续课程）

## 教训
- 看到"课程先修关系 / 能否完成所有课程" → 有向图判环，DFS 三色标记或拓扑排序（Kahn 算法）
- 三色标记的核心：1（正在访问）遇到回溯 = 有环，-1（已安全）用于剪枝避免重复搜索
- 和 547 题对比：547 是无向图连通分量，207 是有向图判环——图论问题的两个经典方向
- 拓扑排序的 BFS 版（Kahn 算法：入度为 0 的节点入队，依次删除边）也值得掌握

## 图论算法对比
|      题目     | 图类型     | 目标        | 方法           | 核心数据结构                     |
| :---------: | :------ | :-------- | :----------- | :------------------------- |
|   547 省份数量  | **无向图** | 连通分量个数    | 并查集 / DFS    | `father` 字典 / `visited` 数组 |
| **207 课程表** | **有向图** | **是否存在环** | **DFS 三色标记** | **`flags` 状态数组**           |
