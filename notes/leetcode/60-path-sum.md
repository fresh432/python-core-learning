# LeetCode 112 路径总和

## 我的思路（40分钟）
1. 前10分钟：想到内部定义递归函数处理根节点，和 101 题模式一致
2. 中间15分钟：卡在叶子节点判断——调试了很久才确认"叶子 = 左右都为空"
3. 后15分钟：自己写出嵌套函数版本通过，再看答案发现可以直接用原函数递归，不用嵌套

## 我的写法（嵌套函数）
```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def func(R, Sum):
            if not R:
                return False
            Sum -= R.val
            if not R.left and not R.right and Sum == 0:
                return True
            return func(R.left, Sum) or func(R.right, Sum)
        
        if not root:
            return False
        return func(root, targetSum)
```

## 更优写法（直接用原函数递归）
```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)
```

## 关键
- 递归思路：每到一个节点，targetSum 减去当前节点值，到叶子时看是否为 0
- 叶子节点判断：not left and not right，缺一不可
- 返回值：left or right，只要有一条路径满足即可

## 教训
- 嵌套函数不是必须的，原函数直接递归更简洁——但嵌套函数在处理"需要额外参数"时有用
- 和 104 题对比：

| 题目           | 递归返回值    | 核心                           |
| ------------ | -------- | ---------------------------- |
| 104 最大深度     | int      | `max(left, right) + 1`       |
| **112 路径总和** | **bool** | **`left or right`，减 target** |

- 看到"路径和" → 递归时做减法，到叶子判断是否为 0，比累加更直观