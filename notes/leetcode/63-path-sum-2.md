# LeetCode 113 路径总和 II

## 我的思路（40分钟）
- 前15分钟：想到递归保存路径和计算数值，和 112 题思路一致
- 中间15分钟调试：卡在两处：
  - 路径列表的回溯删除不知道怎么处理
  - 保存到 ans 时不知道要保存路径的副本（list(path)），直接 append(path) 会导致后续修改影响已保存的路径
- 后10分钟：看答案理解——回溯法：递归前 append，递归后 pop，保持路径列表的"现场还原"

## 代码
```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans, path = [], []
        
        def func(R, Sum):
            if not R:
                return
            path.append(R.val)      # 做选择：当前节点加入路径
            Sum -= R.val
            
            if Sum == 0 and not R.left and not R.right:
                ans.append(list(path))  # ← 保存副本！不是 path 本身
            
            func(R.left, Sum)       # 递归左子树
            func(R.right, Sum)      # 递归右子树
            path.pop()              # 撤销选择：回溯，恢复现场
        
        func(root, targetSum)
        return ans
```

## 关键
- 回溯模板：选择 → 递归 → 撤销选择（append → func → pop）
- 保存副本：ans.append(list(path)) 或 path[:]，否则 path 后续 pop() 会影响已保存的结果
- 和 112 题对比：112 只判断是否存在，113 要找出所有路径 → 回溯法

## 教训
- 看到"找出所有路径/所有组合/所有解" → 回溯法（DFS + 状态恢复）
- 回溯的核心是现场还原：递归前修改状态，递归后恢复状态，保证每条路径独立
- list(path) 保存副本是高频坑点，直接 append(path) 是引用传递，后续修改会影响所有已保存的路径
- 和 112 题的关系：

| 题目              | 需求         | 方法            |
| --------------- | ---------- | ------------- |
| 112 路径总和        | 判断是否存在     | 递归返回 bool     |
| **113 路径总和 II** | **找出所有路径** | **回溯 + 保存副本** |
