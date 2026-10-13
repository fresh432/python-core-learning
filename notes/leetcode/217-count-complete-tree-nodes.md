# LeetCode 222 完全二叉树的节点个数

## 我的思路（40分钟）
- 前15分钟：想用 BFS 层序遍历，知道可以用编号定位但不知道怎么用。写了 O(n) 的代码，但题目要求优于 O(n)
- 中间15分钟：看答案，核心洞察——利用完全二叉树的性质递归：
  - 完全二叉树：除了最后一层，其他层都是满的，最后一层节点从左到右连续
  - 递归判断左右子树是否为满二叉树：分别遍历左子树的最左路径和右子树的最右路径，获取深度
  - 若 leftDepth == rightDepth：说明是满二叉树，节点数 = 2^depth - 1
  - 否则：递归计算左子树 + 右子树 + 1（根节点）
- 后10分钟：按方法写出，通过

## 代码
```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = root.left
        right = root.right
        leftDepth = 0
        rightDepth = 0
        
        while left:
            left = left.left
            leftDepth += 1
        
        while right:
            right = right.right
            rightDepth += 1
        
        if leftDepth == rightDepth:
            return 2 ** (leftDepth + 1) - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
```

## 关键
- 完全二叉树性质：左右深度相等 → 满二叉树，直接公式计算
- 只遍历"金字塔的塔边"（最左和最右路径），获取深度
- 时间复杂度：O((log n)^2)，因为每次递归只走一边，深度 log n，每层判断深度也是 log n

## 教训
- 看到"完全二叉树节点个数" → 递归 + 判断是否为满二叉树，不要直接遍历
