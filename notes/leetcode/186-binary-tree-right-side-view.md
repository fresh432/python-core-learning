# LeetCode 199 二叉树的右视图

## 我的思路（35分钟）
- 前15分钟：想用 DFS，思考是否需要参数标记最右节点，没想出来
- 中间10分钟：改用层序遍历（BFS），发现出奇简单——每层最后一个节点就是右视图看到的节点，保存每层的最后一个即可。轻松实现
- 后10分钟：还是想写 DFS 版本。核心思路——先遍历右子树再遍历左子树，传入 layer 参数标记层数。当 len(ans) < layer 时，说明当前节点是该层第一个被访问到的（因为先右后左），即最右节点，加入答案

## 代码（BFS 法）
```python
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        
        while queue:
            layer = deque()
            while queue:
                node = queue.popleft()
                if not queue:  # 当前层最后一个
                    ans.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            queue = layer
        
        return ans
```

## 代码（DFS 法）
```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        
        def dfs(root, layer):
            if not root:
                return
            if len(self.ans) < layer:
                self.ans.append(root.val)
            dfs(root.right, layer + 1)  # 先右
            dfs(root.left, layer + 1)   # 后左
        
        dfs(root, 1)
        return self.ans
```

## 关键
- BFS：按层遍历，每层最后一个节点加入答案
- DFS：先右后左，layer 标记深度，ans 长度小于当前层数时说明是该层第一个访问的节点（最右）
- 两种方法时间都是 O(n)，BFS 空间 O(w)（最大宽度），DFS 空间 O(h)（树高）

## 教训
- 看到"二叉树右视图/每层最右节点" → BFS 最直观（取每层最后一个），DFS 先右后左也可
- DFS 的关键：先遍历右子树，这样每层第一个遇到的节点就是最右节点
- 和 102/107 题对比：102 是层序遍历返回所有层，107 是返回自底向上的层序，199 是只取每层最右
