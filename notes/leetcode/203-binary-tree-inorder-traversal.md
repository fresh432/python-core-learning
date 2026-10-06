# LeetCode 94 二叉树的中序遍历

## 我的思路（20分钟）
- 前2分钟：递归法轻松写出，左-根-右顺序
- 中间10分钟：想迭代法，卡在如何维护遍历节点和回溯上层节点，只记得要用数组保存，但具体逻辑想不出来
- 后5分钟：看答案，回想起迭代法核心——用栈保存访问过的节点，一路向左入栈，左子树走到底后弹出栈顶节点保存值，再转向右子树，重复上述过程
- 后3分钟：自己写了一遍迭代版，通过

## 代码（递归法）
```python
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans
```

## 代码（迭代法）
```python
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans
```

## 关键
- 递归：左-根-右，天然中序
- 迭代：栈模拟递归，一路向左入栈，弹出时访问（中序），再转向右
- 与前序遍历迭代的区别：前序在入栈时就可以保存值，中序必须在弹出后保存

## 教训
- 看到"二叉树中序遍历" → 递归法秒写，迭代法记住"左入栈→弹出访问→转右"的模板
- 和 144/145 题对比：144 是前序（根左右），145 是后序（左右根），94 是中序（左根右），三种遍历的递归和迭代都要熟练掌握
