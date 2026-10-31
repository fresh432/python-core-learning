# LeetCode 456 132 模式（复习）

## 我的思路（2分钟）
- 变量 k 初始化为 -inf，代表"2"位置的值
- 倒序遍历 nums：
  - 栈非空且当前 num < k，说明找到了比 2 小的 1，返回 True
  - 栈非空且当前 num > 栈顶，循环弹出直到栈空或栈顶 ≥ num，同时 k 维护为弹出值的最大值
  - num 入栈
- 全部遍历完没找到则返回 False

## 代码
```python
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        k = -inf
        stack = []
        for num in nums[::-1]:
            if stack and num < k:           # 1 出现，132 凑齐
                return True
            while stack and stack[-1] < num:
                k = max(stack.pop(), k)     # 弹出的次大值成为新的 2
            stack.append(num)
        return False
```

## 关键
- 复习 2 分钟一遍通过，说明倒序 + 单调递减栈 + k 维护次大值的套路已经掌握