# LeetCode 102 二叉树的层序遍历

## 我的思路（30分钟）
1. 前15分钟：惯性思维想递归，但层序遍历是"按层输出"，递归的深度优先不适合
2. 后15分钟：看答案理解——队列 BFS：把同一层节点全部出队处理，同时把它们的子节点入队，准备下一层遍历

## 代码
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        
        while queue:
            tmp = []
            # 关键：固定当前层的节点数，只遍历这一层
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        
        return res
```

## 关键
- BFS 核心：队列，先进先出，保证按层遍历
- 分层技巧：for _ in range(len(queue)) 固定当前层节点数，避免和新入队的子节点混在一起
- collections.deque() 的 popleft() 是 O(1)，比列表 pop(0) 高效
- 空树直接返回 []

## 教训
- 看到"按层遍历/层序" → BFS + 队列，不是递归
- 递归是 DFS（深度优先），队列是 BFS（广度优先），两者是二叉树的两大遍历体系
- 和 104 题（最大深度）对比：104 用递归求深度，102 用队列按层输出——同一棵树，不同需求用不同遍历
