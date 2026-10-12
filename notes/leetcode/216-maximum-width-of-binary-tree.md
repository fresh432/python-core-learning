# LeetCode 662 二叉树最大宽度

## 我的思路（45分钟）
- 前20分钟：完全没头绪，想过层序遍历时把空节点也入队，但处理极其麻烦且不优雅
- 中间15分钟：看答案，核心洞察——用完美二叉树的子节点编号。根节点编号为1，左子节点 code*2，右子节点 code*2+1。层序遍历时记录每层节点的最小编号 mn 和最大编号 mx，该层宽度 = mx - mn + 1
- 后10分钟：按这个方法写出，通过

## 代码
```python
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        ans = 0
        queue = deque([(1, root)])
        
        while queue:
            mn, mx = inf, 0
            for _ in range(len(queue)):
                code, node = queue.popleft()
                if node.left:
                    queue.append((code * 2, node.left))
                if node.right:
                    queue.append((code * 2 + 1, node.right))
                mn, mx = min(code, mn), max(code, mx)
            ans = max(ans, mx - mn + 1)
        
        return ans
```

## 关键
- 完美二叉树编号：根=1，左子=父2，右子=父2+1
- BFS 层序遍历：每层记录 mn（最小编号）和 mx（最大编号）
- 宽度计算：mx - mn + 1
- 不需要存空节点，只存存在的节点及其编号

## 教训
- 看到"二叉树最大宽度" → BFS + 完美二叉树编号，不要试图存空节点