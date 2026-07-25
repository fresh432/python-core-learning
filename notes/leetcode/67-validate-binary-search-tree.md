# LeetCode 98 验证二叉搜索树

## 我的思路（45分钟）
1. 前20分钟：想到两种方法：
   - 方法一：中序遍历存入列表，检查是否递增——时间空间高，放弃
   - 方法二：前序遍历，保留前两个节点值传给子节点比较——没想出怎么实现
2. 后25分钟：看答案三种方法，后序遍历动态规划方法看了20分钟才理解一点，最终写完

## 代码（递归 + 上下界约束）
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(R, min_v, max_v):
            if not R:
                return True
            
            # 当前节点值必须在 (min_v, max_v) 范围内
            if R.val >= max_v or R.val <= min_v:
                return False
            
            # 左子树：上界变为当前节点值
            if func(R.left, min_v, R.val) == False:
                return False
            # 右子树：下界变为当前节点值
            if func(R.right, R.val, max_v) == False:
                return False
            
            return True
        
        return func(root, -2**100, 2**100)
```

## 关键
- BST 定义：左子树所有节点 < 根 < 右子树所有节点
- 上下界约束：每个节点有 min_v 和 max_v，必须满足 min_v < val < max_v
- 左子树：上界收紧为当前值；右子树：下界收紧为当前值
- 初始边界：极大/极小值（或用 float('-inf') / float('inf')）

## 三种方法对比
| 方法         | 思路            | 时间       | 空间       |
| ---------- | ------------- | -------- | -------- |
| 中序遍历+列表    | 中序应为递增        | O(n)     | O(n)     |
| **递归+上下界** | **每个节点有合法范围** | **O(n)** | **O(h)** |
| 后序DP       | 子树返回 min/max  | O(n)     | O(h)     |

## 教训
- 验证 BST 不是简单的 left < root < right，而是左子树所有节点 < 根 < 右子树所有节点
- 只比较父子和左右兄弟会漏掉"右子树的左子树必须大于根"的情况
- 上下界约束是最清晰的解法：每个节点继承一个合法区间，越往下区间越窄
- 和 108 题对比：

| 题目            | 操作     | 核心        |
| ------------- | ------ | --------- |
| 108 有序数组转 BST | 构造     | 取中点       |
| **98 验证 BST** | **验证** | **上下界约束** |

