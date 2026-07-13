# LeetCode 155 最小栈

## 思路（30分钟，看答案）
辅助栈：同步存储当前最小值。

## 代码
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
```

## 关键
- 辅助栈只存更小或相等的值
- pop时同步检查是否需要弹出辅助栈
- getMin()直接取辅助栈顶，O(1)

## 教训
- sorted排序是O(n log n)，不满足O(1)要求
- 栈的辅助数据结构是常见技巧
- 对栈的使用需要多练习
