# LeetCode 124 二叉树中的最大路径和

## 我的思路（45分钟）
- 前30分钟：想用 DFS 遍历每个节点，获取左右子树的向下遍历值，然后比较返回更优值。但把向上传递的单链最优和维护全局最优混在了一起，返回的是全局最优或单链最优值，写了一堆 if 嵌套，始终不对
- 后10分钟：看答案，核心洞察——分开处理：
  - 向上传递：只返回以当前节点为端点的最大单链和（max(left, right) + root.val，负数取0）
  - 全局维护：用 ans 保存以当前节点为拐点的最大路径和（left + right + root.val）
- 后5分钟：自己写了一遍，max(0, dfs(root)) 直接覆盖负数子树，简洁通过

## 代码
```python
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = float("-inf")
        
        def dfs(root):
            if not root:
                return 0
            
            left = max(0, dfs(root.left))   # 左子树贡献，负数不要
            right = max(0, dfs(root.right)) # 右子树贡献，负数不要
            
            # 以当前节点为拐点的路径和（不向上传递，只更新全局最优）
            self.ans = max(self.ans, left + right + root.val)
            
            # 向上传递：只能选一边，形成单链
            return max(left, right) + root.val
        
        dfs(root)
        return self.ans
```

## 关键
- 后序遍历：先递归左右子树，再处理当前节点
- 向上传递值：max(left, right) + root.val，只能选一边（路径不能分叉）
- 全局最优值：left + right + root.val，可以两边都选（当前节点作为拐点）
- max(0, ...)：子树贡献为负时直接取0（不走那边）

## 教训
- 看到"二叉树最大路径和" → 后序 DFS，分开处理向上传递值和全局最优值
- 向上传递只能是单链（选左或选右），全局最优可以是"左-根-右"的拐点路径
- max(0, dfs(child)) 是处理负数子树的标准写法，避免一堆 if 嵌套
- 和 543 题对比：543 是直径（边数，只计数），124 是路径和（带权值，需要 max(0, ...) 处理负数）

## 二叉树路径系列对比
| 题目            | 目标                | 方法         | 核心                |
| :------------ | :---------------- | :--------- | :---------------- |
| 112 路径总和      | 是否存在和为 target 的路径 | DFS        | 路径和累加             |
| 437 路径总和 III  | 路径和为 target 的路径数  | 前缀和+哈希表    | `presum - target` |
| **124 最大路径和** | **最大路径和**         | **后序 DFS** | **单链传递 + 拐点全局最优** |
| 543 二叉树直径     | 最长路径（边数）          | DFS        | \`left +          |
