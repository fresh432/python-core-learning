# LeetCode 114 二叉树展开为链表

## 我的思路（35分钟）
- 前30分钟：递归，每次递归先拿到左右子树，再按左右子树存在情况拼接。但设计太绕：拿左子树头去拼接右子树头的错误没发现、每个子树单独做左子树置空冗余易错，调试拼接逻辑花了时间。设计为左子树存在时循环拿左子树尾接右子树头，通过了，但最坏 O(n²)（每个节点都要循环找左子树尾）
- 看答案5分钟：有"传尾部"的方法，每次递归返回尾部，就不用循环找左子树尾。返回优先级：左子树尾 → 右子树尾 → 当前节点；左子树尾存在才做拼接。改完 O(n)

## 代码（递归法）
```python
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        if not root:
            return None
        left_tail = self.flatten(root.left)    # 递归展开左右子树，返回各自尾
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right       # 左尾接右头
            root.right = root.left             # 左提为右
            root.left = None
        return right_tail or left_tail or root  # 返回整棵树的尾
```

## 关键
- 递归函数返回值 = "展开后链表的尾节点"，父层直接拿尾做拼接，免循环
- 拼接三步：左尾接右头 → 左子树提为右子树 → 左指针置空
- 返回尾优先级：右尾 > 左尾 > 自身（右存在则右尾是最后，否则左尾，都无则自己是尾）

## 教训
- 看到"原地展开二叉树为链表" → 递归返回尾节点的写法（O(n)），不要每次循环找尾（O(n²)）
- 设计教训：拼接类递归要想清楚"每层向父层提供什么信息"，提供尾节点比提供头节点更省事，因为父层要的是"接哪里"