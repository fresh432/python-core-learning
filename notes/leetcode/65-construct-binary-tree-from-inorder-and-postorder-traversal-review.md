# LeetCode 106 从中序与后序遍历序列构造二叉树（复习）

## 我的思路（40分钟）
- 后序遍历序列的最后一个值代表这棵子树的根节点
- 用这个根节点去中序遍历序列中划分出左子树和右子树
- 再用中序遍历得到的根节点下标，把后序遍历序列也划分成左子树和右子树
- 递归构造左右子树序列，返回当前递归的节点

## 代码
```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode | None:
        if not inorder:
            return None
        cur = TreeNode(postorder[-1])     # 后序末位 = 根
        postorder.pop()
        for i in range(len(inorder)):     # 根在中序中的位置
            if inorder[i] == cur.val:
                break
        left = inorder[:i]
        right = inorder[i + 1:]
        cur.left = self.buildTree(left, postorder[:i])
        cur.right = self.buildTree(right, postorder[i:])
        return cur
```

## 教训
- 7 月份写过一遍，大致思路还记得，但具体实现花了点时间，复习暴露实现退化：思路记得，但切片边界的下标对应关系（postorder[:i] 对应左子树、postorder[i:] 对应右子树）花了大量时间确认
- 和 105 题对比：105 前序+中序（根在前序首位），106 后序+中序（根在后序末位）——前取头、后取尾，中序划分两侧，递归切片

