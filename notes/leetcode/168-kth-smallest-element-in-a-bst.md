# LeetCode 230 二叉搜索树中第K小的元素

## 我的思路（60分钟）
- 前10分钟：误以为进阶要求是用栈按顺序存答案，试了一下行不通，放弃
- 中间10分钟：不确定中序遍历顺序，复习了前/中/后序遍历
- 中间10分钟：写出递归中序遍历，但没在后面调用递归函数，导致一直返回不了正确结果。以为是逻辑问题，又花了10分钟看答案，发现和答案几乎一致，最终找到问题——没调用 dfs(root)，气笑了
- 优化：在左子树递归结束后添加 if self.k == 0: return 剪枝，通过
- 后15分钟：看迭代法（进阶）——用栈保存待遍历节点，模拟中序遍历
- 后5分钟：自己写出迭代版本

## 代码（递归法）
```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = 0
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.k == 0:       # 剪枝：已经找到，直接返回
                return
            self.k -= 1
            if self.k == 0:
                self.ans = root
            dfs(root.right)
        
        dfs(root)                 # 别忘了调用！
        return self.ans.val
```

## 代码（迭代法）
```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        count = 0
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            cur = cur.right
        
        return -1
```

## 关键
- BST 中序遍历是有序的（升序），第 k 个访问的节点就是第 k 小
- 递归法：左-根-右顺序，维护 k 计数器，减到 0 时记录答案
- 迭代法：栈模拟中序遍历，一路向左入栈，弹出时计数，到 k 返回
- 剪枝：左子树递归后判断 k == 0，提前终止

## 教训
- 看到"BST 第 K 小/大" → 中序遍历，递归或迭代均可
- 低级错误：写完递归函数别忘了调用！
- 和 215 题对比：215 是数组找第 K 大（快排/堆），230 是 BST 找第 K 小（中序遍历 O(h+k)）
