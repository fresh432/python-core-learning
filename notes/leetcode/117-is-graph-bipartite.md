# LeetCode 785 判断二分图

## 我的思路（50分钟）
- 前5分钟：读懂题意，确认用染色标记法——两种颜色交替染相邻节点，如果发生冲突则不是二分图
- 中间30分钟：卡在如何传递下一个邻接节点，试图加队列把未染色节点存起来再遍历，越写越复杂，陷入实现困境
- 后15分钟：看答案，发现根本不需要队列——直接 DFS 递归染色，当前节点染 c，邻接节点染 -c，未染色的递归下去，已染色的检查是否冲突

## 代码
```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)  # 0=未染色, 1/-1=两种颜色
        
        def dfs(i, c):
            colors[i] = c
            for j in graph[i]:
                # 邻接节点已染同色 → 冲突
                if colors[j] == c:
                    return False
                # 邻接节点未染色 → 递归染相反色
                if colors[j] == 0 and not dfs(j, -c):
                    return False
            return True
        
        for i, c in enumerate(colors):
            if c == 0 and not dfs(i, 1):
                return False
        
        return True
```

## 关键
- 二分图判定定理：一个图是二分图，当且仅当可以用两种颜色染色，使得每条边的两个端点颜色不同
- DFS 染色：当前节点染 c，邻接节点必须染 -c
- 冲突检测：colors[j] == c 时返回 False
- 外层循环：图可能不连通，需要对每个未染色的连通分量启动 DFS

## 教训
- 看到"能否分成两组/两种颜色" → 二分图判定，DFS/BFS 染色法
- 不需要队列，DFS 递归本身就是天然的遍历方式，递归参数传递颜色即可
- 和 207 题对比：207 是判环（有向图），785 是二分图判定（无向图）——都是图论 DFS，但染色法关注的是相邻节点颜色冲突
