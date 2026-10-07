# LeetCode 100 相同的树

## 我的思路（18分钟）
- 递归法（6分钟）：每次递归传入两棵树的对应节点，判断：
  - 同时为 None → True
  - 一个为 None 一个非 None → False
  - 都存在但值不同 → False
  - 都存在且值相同 → 递归比较左右子树，左右都为 True 才返回 True
- 迭代法（7分钟）：用两个栈分别维护两棵树的节点，入栈时比较值。每次循环结束后比较两节点状态是否一致，不一致返回 False。外层循环后再比较节点和栈状态
- 单栈优化（5分钟）：尝试单栈写法，优化部分判断逻辑

## 代码（递归法）
```python
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        return dfs(p, q)
```

## 代码（迭代法）
```python
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        stack = []
        while (p and q) or stack:
            while p and q:
                stack.append((p, q))
                if p.val != q.val:
                    return False
                p, q = p.left, q.left
            if p or q:
                return False
            p, q = stack.pop()
            p, q = p.right, q.right
        if p or q:
            return False
        return True
```

## 关键
- 递归：同步遍历两棵树，结构和值都要相同
- 迭代：双节点按pair同步入栈出栈，任何一步不匹配立即返回 False
- 边界：空节点处理要覆盖所有组合情况

## 教训
看到"判断两棵树是否相同" → 递归同步遍历最直观，迭代用可以用单栈实现
和 572 题对比：572 是判断子树（一棵是否是另一棵的子树），100 是判断完全相同

