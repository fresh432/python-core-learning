# LeetCode 108 将有序数组转换为二叉搜索树

## 我的思路（20分钟）
1. 前10分钟：理解题目——有序数组转高度平衡 BST，需要让树尽量"矮胖"
2. 后10分钟：想到取中间元素作为根节点，左右子数组递归构建左右子树，写出代码调试通过

## 代码
```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not nums:
            return
        
        index = n // 2              # 中间元素作为根节点
        root_val = nums[index]
        root = TreeNode(root_val)
        
        root.left = self.sortedArrayToBST(nums[:index])
        root.right = self.sortedArrayToBST(nums[index+1:])
        
        return root
```

## 关键
- BST 特性：左 < 根 < 右，有序数组的中点作为根天然满足
- 高度平衡：每次取中间元素，左右子树节点数相差不超过 1
- 递归终止：not nums 返回 None

## 教训
- 看到"有序数组转 BST" → 取中点作为根，左右子数组递归
- 和 105/106 题（遍历序列构造二叉树）对比：

| 题目      | 输入       | 找根方式           |
| ------- | -------- | -------------- |
| 105/106 | 遍历序列     | 前序首/后序尾        |
| **108** | **有序数组** | **取中点 `n//2`** |

- 本题是 BST 的构造，105/106 是普通二叉树的构造