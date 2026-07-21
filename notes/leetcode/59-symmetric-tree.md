# LeetCode 101 对称二叉树

## 我的思路（20分钟）
- 前10分钟：想到递归，但不知道怎么处理根节点——对称是左右子树比较，根节点没有"对称对象"
- 后10分钟：看答案理解——单独写一个递归方法 recur(L, R)，传入两个节点比较，根节点的特殊处理放在外层

## 代码
```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)
        
        return not root or recur(root.left, root.right)
```

## 关键
- 双指针递归：recur(L, R) 同时遍历左子树和右子树
- 对称条件：
  1. 都为空 → True
  2. 一个为空或值不等 → False
  3. 递归：L.left vs R.right（外侧），L.right vs R.left（内侧）
- 根节点处理：空树直接 True；非空树调用 recur(left, right)

## 教训
- 二叉树"比较"类问题 → 写双参数递归函数，外层处理根节点特殊情况
- 和 226 题对比：

| 题目            | 递归特点      | 核心操作       |
| ------------- | --------- | ---------- |
| 226 翻转二叉树     | 单参数递归     | 交换左右子树     |
| **101 对称二叉树** | **双参数递归** | **比较两个子树** |

- 双参数递归是处理"两棵树关系"的标准模式（比较、合并等）
- not root or recur(...) 简洁处理空树情况