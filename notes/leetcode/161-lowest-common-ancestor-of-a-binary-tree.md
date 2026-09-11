# LeetCode 236 二叉树的最近公共祖先

## 我的思路（50分钟）
- 前10分钟：想到 DFS 和 BFS 两种思路，确定用 DFS
- 中间25分钟：按自己的思路写——从根节点向下 DFS，找到目标节点返回 True，当左右子树返回值都为真时保存当前节点作为答案；如果一个目标是另一个的子节点，需要额外分支处理和标记。但维护 ans 的逻辑有问题：ans 在找到最近节点时无法被修改，且无法进入标记的分支处理，调试许久无果
- 后10分钟：看答案，发现可以直接以返回值返回被认为是最近公共祖先的节点，不需要额外维护全局变量
- 后5分钟：按返回值思路重写，通过

## 代码
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left
        
        return root
```

## 关键
- 递归终止条件：root is None 或 root == p 或 root == q，直接返回 root
- 后序遍历：先递归左右子树，再根据返回值判断当前节点角色
- 四种返回情况：
  - left 和 right 都为空：当前子树不含 p 或 q，返回 None
  - 只有 left 为空：p/q 全在右子树，返回 right
  - 只有 right 为空：p/q 全在左子树，返回 left
  - left 和 right 都不为空：p 和 q 分别在左右子树，当前 root 就是 LCA

## 教训
- 看到"二叉树最近公共祖先" → 后序 DFS，返回值即答案，不要试图用全局变量维护
- 核心洞察：如果 p 和 q 分别在当前节点的左右子树中，当前节点就是 LCA；如果都在一侧，那一侧的返回值就是 LCA
- 一个节点是另一个的祖先时：递归会先遇到该祖先节点并返回，不会继续向下，天然处理这种情况
- 和 235 题对比：235 是 BST 的 LCA（利用大小关系 O(h)），236 是普通二叉树的 LCA（后序遍历 O(n)）