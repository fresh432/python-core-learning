# LeetCode 106 从中序与后序遍历序列构造二叉树

## 我的思路（10分钟）
和 105 题类型相同，花了5分钟把中序和后序的联系理清楚，再花5分钟调试通过。

## 代码
```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root_val = postorder[-1]        # 后序尾元素 = 根节点
        root = TreeNode(root_val)
        postorder.pop()                 # 弹出已用的根节点
        
        root_idx = inorder.index(root_val)
        
        # 左子树：中序[:root_idx]，后序[:root_idx]
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        # 右子树：中序[root_idx+1:]，后序[root_idx:]
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:])
        
        return root
```

## 关键
- 后序特性：[左子树, 右子树, 根] → 最后一个元素是根
- postorder.pop() 取出根节点，剩余部分先左后右
- 后序的左右子树切片长度和中序的左右子树长度相同（都是 root_idx 个）

## 和 105 题的对比
| 题目            | 根节点位置               | 子树切片                                            |
| ------------- | ------------------- | ----------------------------------------------- |
| 105 前序+中序     | `preorder[0]`       | 左：`preorder[1:root_idx+1]`，`inorder[:root_idx]` |
| **106 后序+中序** | **`postorder[-1]`** | 左：`inorder[:root_idx]`，`postorder[:root_idx]`   |

## 教训
- 105 题的模式直接迁移成功！两题核心逻辑完全一致，只是根节点位置和切片方式不同
- postorder.pop() 可以简化切片计算，但要注意顺序：先构建右子树再左子树时不能用 pop（会乱），本题先左后右刚好匹配
- 看到"遍历序列构造二叉树" → 先确定哪种遍历提供根节点（前序首/后序尾），再用中序分割
