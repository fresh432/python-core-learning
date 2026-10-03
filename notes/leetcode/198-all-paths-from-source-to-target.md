# LeetCode 797 所有可能的路径

## 我的思路（15分钟）
- DFS + 回溯：从 0 节点开始遍历
- path 保存当前路径，ans 收集所有完整路径
- 终止条件：index == n - 1，将 path[:] 加入 ans
- 回溯：DFS 返回前 path.pop()，恢复状态

## 代码
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        path = []
        n = len(graph)
        
        def dfs(index, move):
            path.append(index)
            if index == n - 1:
                ans.append(path[:])
            for i in move:
                dfs(i, graph[i])
            path.pop()
        
        dfs(0, graph[0])
        return ans
```

## 关键
- DFS + 回溯：path.append → 递归 → path.pop
- 终止条件：到达 n-1 节点
- path[:]：深拷贝，避免引用问题

## 教训
- 看到"图中找所有路径" → DFS + 回溯
- 和 200 题对比：200 是连通块计数（标记访问），797 是找所有路径（回溯收集）
