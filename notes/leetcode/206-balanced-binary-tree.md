# LeetCode 110 平衡二叉树

## 我的思路（19分钟）
- 前8分钟：误解题意，以为平衡二叉树只要求根节点左右子树高度差不超过1，写错了
- 中间6分钟：发现要求每个节点的左右子树高度差都不能超过1。想同时返回两种值（是否平衡的bool + 高度的int），没想出来，先用暴力解法——对每个节点调用求高度的DFS，再遍历所有节点判断，能通过但时间复杂度高
- 后5分钟：看提示，核心洞察——用返回-1表示不平衡，一个返回值同时传递两种语义（高度或-1），然后按这个方法重写，通过

## 代码（暴力版，非最优）
```python
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        
        def dfs(root, length):
            if not root:
                return length
            length = max(dfs(root.left, length), dfs(root.right, length)) + 1
            return length
        
        stack = [root]
        while stack:
            root = stack.pop()
            if abs(dfs(root.left, 0) - dfs(root.right, 0)) > 1:
                return False
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return True
```

## 代码（标准解法）
```python
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(root, length):
            if not root:
                return length
            left = dfs(root.left, length + 1)
            if left == -1: return -1
            right = dfs(root.right, length + 1)
            if right == -1: return -1
            return max(left, right) if abs(left - right) <= 1 else -1
        
        return dfs(root, 0) != -1
```

## 关键
- 后序遍历：先递归左右子树，再判断当前节点
- 返回值语义：
  - 正常高度：返回 max(left, right)
  - 不平衡：返回 -1
- 剪枝：一旦某个子树不平衡（返回-1），上层直接传递-1，无需继续计算

## 教训
- 看到"判断平衡二叉树" → 后序DFS，返回-1表示不平衡
- 题意理解：平衡二叉树要求每个节点的左右子树高度差 <= 1，不只是根节点
