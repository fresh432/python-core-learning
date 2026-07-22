# LeetCode 543 二叉树的直径

## 我的思路（40分钟）
1. 前30分钟：写出大致框架——内部函数 MaxLen(R) 递归求最深长度，但：
   - bug 1：函数内部节点不小心写成外层节点（变量名混淆）
   - bug 2：保存最大值的思路有问题，直径 = 左深度 + 右深度，不是单纯的 max
2. 后10分钟：看答案发现问题，修改通过

## 代码
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def MaxLen(R):
            if not R:
                return 0
            n_left = MaxLen(R.left)
            n_right = MaxLen(R.right)
            # 经过当前节点的直径 = 左深度 + 右深度
            self.ans = max(self.ans, n_left + n_right)
            # 返回当前子树的最大深度（供父节点使用）
            return max(n_left, n_right) + 1
        
        MaxLen(root)
        return self.ans
```

## 关键
- 直径定义：任意两个节点之间的最长路径，等于某个节点的左子树深度 + 右子树深度
- 递归返回值：返回当前子树的最大深度（供父节点计算直径）
- 全局变量 self.ans：记录遍历过程中遇到的最大直径
- 后序遍历：先递归左右子树，再计算当前节点的直径

## 教训
- 变量名混淆是大坑：内部递归函数的参数名要和外层严格区分
- 和 104 题（最大深度）的关系：
  - 104 题：返回 max(left_depth, right_depth) + 1
  - 543 题：返回 max(left_depth, right_depth) + 1，但额外记录 left_depth + right_depth 作为直径候选
- 看到"二叉树最长路径/直径" → 后序遍历，每个节点计算 left + right，全局维护最大值
- 这类"递归过程中需要额外记录信息"的题，用 self.ans 或闭包变量
