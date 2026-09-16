# LeetCode 235 二叉搜索树的最近公共祖先

## 我的思路（45分钟）
- 前25分钟：用递归法写了个"石山"版本——忽略了 BST 有序特性可以天然剪枝，虽然写了节点值都小于或大于目标值时的剪枝，但整体按普通二叉树写法实现，代码极其复杂，3409ms
- 中间：看了眼答案，核心洞察——BST 的 LCA 不需要遍历整棵树：
  - 若 root.val < p.val 且 root.val < q.val：p 和 q 都在右子树，去右边找
  - 若 root.val > p.val 且 root.val > q.val：p 和 q 都在左子树，去左边找
- 否则：root 就是 LCA（一个在左一个在右，或 root 等于其中一个）
- 后5分钟：按正确思路写出递归版，64ms
- 后15分钟：写出迭代版，同样的逻辑用 while 循环，71ms

## 代码（"石山"版，普通二叉树写法）
```bash
就是普通二叉树写法上面加了两个节点都大于或小于目标值时剪枝的操作,这里就不贴了
```

## 代码（正常递归法）
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
```

## 代码（迭代法）
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = p.val, q.val
        while root:
            if root.val < p and root.val < q:
                root = root.right
            elif root.val > p and root.val > q:
                root = root.left
            else:
                return root
```

## 关键
- BST 特性：左子树所有值 < root < 右子树所有值
- 判断逻辑：
  - 都小于 root：都在左子树，去左边
  - 都大于 root：都在右子树，去右边
  - 否则：root 就是 LCA（此时 p 和 q 分布在两侧，或 root 等于其中一个）
- 时间复杂度：O(h)，h 为树高，BST 最坏 O(n)，平衡时 O(log n)

## 教训
- 看到"BST 的最近公共祖先" → 直接利用大小比较，不要套用普通二叉树的复杂递归
- BST 的 LCA 代码极简（3行递归 / 6行迭代），和普通二叉树（236题）的复杂后序遍历形成鲜明对比
- 一定要先看题目条件：BST 和普通二叉树的解法天壤之别
- 和 236 题对比：236 是普通二叉树 LCA（后序遍历 O(n)），235 是 BST LCA（大小比较 O(h)）

## LCA 系列对比
| 题目                 | 树类型     | 方法       | 时间复杂度    | 代码复杂度  |
| :----------------- | :------ | :------- | :------- | :----- |
| 236 二叉树的最近公共祖先     | 普通二叉树   | 后序 DFS   | O(n)     | 中等     |
| **235 BST的最近公共祖先** | **BST** | **大小比较** | **O(h)** | **极简** |
