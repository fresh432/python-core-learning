# LeetCode 105 从前序与中序遍历序列构造二叉树

## 我的思路（35分钟）
- 前10分钟：想到前序的第一个元素是根节点，中序中根节点左边是左子树、右边是右子树
- 中间10分钟：卡在如何获取根节点在中序中的索引，以为必须遍历列表，感觉太复杂
- 后15分钟：看答案发现 list.index(val) 直接获取索引，豁然开朗，写出递归

## 代码
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]          # 前序首元素 = 根节点
        root = TreeNode(root_val)
        
        root_idx = inorder.index(root_val)  # 根节点在中序中的位置
        
        # 左子树：前序[1:root_idx+1]，中序[:root_idx]
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        # 右子树：前序[root_idx+1:]，中序[root_idx+1:]
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        
        return root
```

## 关键
- 前序特性：[根, 左子树, 右子树] → 第一个元素是根
- 中序特性：[左子树, 根, 右子树] → 根节点分割左右子树
- 递归构建：找到根 → 中序分割左右 → 前序对应切片递归
- inorder.index() 是 O(n)，可用哈希表优化到 O(1)

## 教训
- 不知道 list.index() 导致卡了10分钟——Python 基础列表方法要熟
- 看到"遍历序列构造二叉树" → 先找根节点位置，再分割左右子树区间
- 前序 + 中序、后序 + 中序可以唯一确定二叉树，但前序 + 后序不行（无法区分左右）