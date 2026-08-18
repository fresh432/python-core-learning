# LeetCode 210 课程表 II

## 我的思路（35分钟）
- 前10分钟：在 207 题的基础上复习 BFS 拓扑排序（Kahn 算法）——入度为 0 的节点入队，依次删除边
- 中间15分钟：写出 210 题的代码框架，建邻接表 + 计算入度 + 队列处理
- 后10分钟：调试，把 numCourses -= 1 写到了入度减一的循环里面，导致计数逻辑错乱，修复后通过

## 代码
```python
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegrees[cur] += 1
        
        queue = deque()
        ans = []
        
        # 入度为0的节点入队
        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
        
        while queue:
            pre = queue.popleft()
            ans.append(pre)
            numCourses -= 1  # 完成一门课程
            
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        
        return ans if numCourses == 0 else []
```

## 关键
- Kahn 算法（BFS 拓扑排序）：
  1. 建邻接表 + 计算每个节点的入度
  2. 入度为 0 的节点入队（没有先修课程，可以直接学）
  3. 出队，将其后续课程的入度 -1，若后续课程入度变为 0 则入队
  4. 重复直到队列为空
- numCourses -= 1 应该在节点出队后执行，表示完成一门课程，不要写到内层循环里
- 结果判定：若 numCourses == 0 说明所有课程都能完成，返回 ans；否则有环，返回 []

## 教训
- 看到"课程安排顺序 / 拓扑排序" → Kahn 算法 BFS，207 题是判环，210 题是输出拓扑序
- numCourses 的减一位置是易错点：在节点出队后、遍历邻接表前
- 和 207 题对比：

|       题目       | 目标       | 方法                 |       返回值       |
| :------------: | :------- | :----------------- | :-------------: |
|     207 课程表    | **能否完成** | DFS 三色标记 / BFS 拓扑  |      `bool`     |
| **210 课程表 II** | **完成顺序** | **BFS 拓扑排序（Kahn）** | **`List[int]`** |
