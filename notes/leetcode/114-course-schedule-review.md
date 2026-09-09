# LeetCode 207 课程表（复习）

## 我的思路（40分钟）
- 前10分钟：想用 DFS 三色标记判环，但遍历细节（邻接表构建、状态转移）想不出来
- 中间10分钟：突然想起 Kahn 算法（入度表 + BFS），顺着思路写
- 踩坑：写到"入度为0的节点入队"时，发现前面没保存邻接表，导致无法快速找到并减少后续节点的入度。花了10分钟看答案修正
- 后5分钟：回顾 DFS 判环思路，和之前想的一样
- 后5分钟：自己写出 DFS 三色标记版本

## 代码（Kahn 算法 / 入度表）
```python
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        
        # 构建入度表和邻接表
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        
        # 入度为0的节点入队
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        
        return not numCourses
```

## 代码（DFS 三色标记判环）
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == 1: return False   # 当前节点在本次 DFS 中再次遇到，有环
            if flags[i] == -1: return True   # 当前节点已被其他路径验证无环
            
            flags[i] = 1                      # 标记为"正在访问"
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1                     # 标记为"已访问且无环"
            return True
        
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        
        return True
```

## 关键
- Kahn 算法：入度为0的节点先修，修完减少后续节点入度，若最后还有节点未修完则有环
- DFS 三色标记：0 未访问，1 正在访问（当前路径上），-1 已访问且无环。遇到 1 说明有环
- 邻接表必须提前构建：adjacency[pre].append(cur)，否则无法快速找到后续课程

## 教训
- 看到"课程表 / 判断有向图是否有环" → Kahn 算法（入度表）或 DFS 三色标记
- Kahn 算法需要同时维护入度表和邻接表，缺一不可。入度表用于判断能否入队，邻接表用于找到后续节点并减少入度
- DFS 三色标记的核心：flags[i] == 1 表示在当前递归路径上再次遇到该节点，即存在环
- 复习价值：两种方法都要熟练掌握，Kahn 适合求拓扑序，DFS 适合判断环的存在性
