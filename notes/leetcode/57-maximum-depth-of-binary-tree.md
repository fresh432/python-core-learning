# LeetCode 104 二叉树的最大深度

## 我的思路（15分钟）
1. 前5分钟：想到用数组索引的父子节点关系（完全二叉树的性质），但意识到这不是链表结构的二叉树写法
2. 后10分钟：看答案，了解到递归——二叉树的问题天然适合递归，当前节点的深度 = max(左子树深度, 右子树深度) + 1

## 代码
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

## 关键
- 递归终止条件：空节点深度为 0
- 递归公式：depth(node) = max(depth(left), depth(right)) + 1
- 后序遍历：先求左右子树深度，再算当前节点深度

## 教训
- 二叉树问题 → 先想递归，不要硬套数组索引
- 完全二叉树的数组索引法（2i+1, 2i+2）只适用于数组存储的二叉树，链表结构必须用递归/迭代
- 递归三要素：终止条件、递归公式、返回值
- 和链表的区别：链表是线性结构，二叉树是树形结构，递归是树的天然解法