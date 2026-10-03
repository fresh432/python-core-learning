# LeetCode 841 钥匙和房间

## 我的思路（15分钟）
- 思路清晰：BFS 遍历图
- 用 flags 数组标记房间是否被访问过
- 用队列保存待访问的钥匙，从 0 号房间开始
- 每次取出钥匙，若房间未访问则将其钥匙入队并标记访问
- 最后遍历 flags 检查是否全部访问

## 代码
```python
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        flags = [False] * n
        flags[0] = True
        queue = deque([rooms[0]])
        
        while queue:
            keys = queue.popleft()
            for key in keys:
                if flags[key]:
                    continue
                queue.append(rooms[key])
                flags[key] = True
        
        for flag in flags:
            if not flag:
                return False
        
        return True
```

## 关键
- BFS：队列保存钥匙，逐个房间解锁
- flags 标记：避免重复访问
- 最后检查：若有房间未访问返回 False

## 教训
- 看到"能否访问所有房间/节点" → BFS/DFS + 访问标记
- 和 547 题对比：547 是省份数量（并查集/DFS），841 是能否访问所有房间（BFS）
