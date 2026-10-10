# LeetCode 173 二叉搜索树迭代器

## 我的思路（24分钟）
- 前17分钟：初始化时用迭代中序遍历把所有节点值存到数组 ans，维护一个下标。next() 返回下标处值并后移，hasNext() 判断下标是否越界。通过了但感觉不是考察点——题目叫"迭代器"，应该逐个吐节点才对
- 后7分钟：看提示，把压栈逻辑分离——初始化时只压左链一次，next() 弹出节点后若该节点有右子树，再对右子树压左链。这样是惰性加载，空间更优

## 代码
```python
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_left(root)
    
    def push_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        root = self.stack.pop()
        if root.right:
            self.push_left(root.right)
        return root.val
    
    def hasNext(self) -> bool:
        return bool(self.stack)
```

## 关键
- 惰性中序遍历：不一次性遍历完整棵树，而是按需压栈
- push_left：将某节点的所有左子节点一路入栈
- next：弹出栈顶（当前最小），若其有右子树，对右子树执行 push_left
- 空间复杂度：O(h)，h 为树高，而非 O(n)

## 教训
- 看到"BST 迭代器" → 栈 + 惰性中序遍历，不要一次性遍历完存数组