# LeetCode 437 路径总和 III

## 我的思路（60分钟）
- 前35分钟：想用 DFS 维护一个列表保存遍历过的元素，每到一个节点计算列表和，若比目标值大则弹出队首，相等则计数加一再弹出。但这样时间复杂度 O(n²)，且边界细节调试了很久始终不过
- 后20分钟：看答案，发现用前缀和 + 哈希表，时间复杂度 O(n)。思路：哈希表保存每个前缀和出现的次数，遍历每个节点时，若 当前前缀和 - targetSum 在哈希表中出现过，则答案加上该前缀和对应的次数
- 后5分钟：跟着写了一遍，通过

## 代码
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, presum):
            if not root:
                return 0
            
            presum += root.val
            
            # 以当前节点结尾的路径中，和为 targetSum 的路径数
            path_cnt = presum_counts.get(presum - targetSum, 0)
            
            # 当前前缀和入表
            presum_counts[presum] = presum_counts.get(presum, 0) + 1
            
            # 递归左右子树
            path_cnt += dfs(root.left, presum) + dfs(root.right, presum)
            
            # 回溯：当前前缀和出表
            presum_counts[presum] -= 1
            
            return path_cnt
        
        presum_counts = {0: 1}  # 前缀和为0出现1次（空路径）
        return dfs(root, 0)
```

## 关键
- 前缀和：presum 表示从根节点到当前节点的路径和
- 路径和为 targetSum 的数量 = presum_counts[presum - targetSum]
- 哈希表 presum_counts：记录每个前缀和出现的次数
- 回溯：离开节点时 presum_counts[presum] -= 1，因为不同分支的路径不能混用
- 初始化 {0: 1}：处理从根节点开始的路径（presum - targetSum = 0）

## 教训
- 看到"二叉树路径和为 target" → 前缀和 + 哈希表 + 回溯，O(n) 时间
- 不要维护列表然后逐个求和（O(n²)），前缀和是标准解法
- 回溯很关键：DFS 返回时要将当前前缀和计数减1，避免不同分支互相干扰
- 和 560 题对比：560 是数组前缀和（一维），437 是二叉树前缀和（DFS + 回溯）