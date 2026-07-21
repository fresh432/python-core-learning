# LeetCode 226 翻转二叉树

## 我的思路（20分钟）
- 前5分钟：想到用递归，但不知道怎么把根节点返回
- 后15分钟：看答案理解——交换动作本身就是递归：先递归翻转左右子树，再交换左右子树

## 代码
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root
```

## 关键
- 递归终止：空节点直接返回
- 递归顺序：先递归翻转右子树，赋值给 root.left；再递归翻转左子树，赋值给 root.right
- 必须用 tmp 暂存：root.left 在第一步就被覆盖了，所以先存到 tmp
- 返回 root：每个递归层都返回当前子树的根节点

## 教训
- 二叉树的"修改"类递归 → 后序遍历：先处理子树，再处理当前节点
- 和 104 题（最大深度）对比：

| 题目            | 遍历顺序   | 递归公式                   |
| ------------- | ------ | ---------------------- |
| 104 最大深度      | 后序     | `max(left, right) + 1` |
| **226 翻转二叉树** | **后序** | **交换 left 和 right**    |

- 递归返回值：返回当前子树的根节点，供上一层使用
- tmp 暂存是链表/树操作的经典技巧，和 206 题（反转链表）的 temp 同理