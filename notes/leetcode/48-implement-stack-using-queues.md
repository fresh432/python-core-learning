# LeetCode 225 用队列实现栈

## 我的思路（30分钟）
理解题意花了时间：只能用队列的标准操作（append 到队尾、pop(0) 从队头取、[0] 查看队头）。之前习惯直接调库函数，现在要手动模拟。

看了答案后受点拨：每次 push 时，把新元素留在队头。具体做法：新元素入 q2，然后把 q1 所有元素依次出队入 q2，最后交换 q1 和 q2。

## 代码
```python
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
```

## 关键
- 核心技巧：push 时把新元素"顶"到队头，后续 pop(0) 自然拿到最后入的元素（栈顶）
- 操作步骤：新元素入 q2 → q1 全部倒过去 → 交换 q1/q2
- q1 始终维护"栈"的状态，q2 只是临时辅助
- top() 直接取 q1[0]，pop() 直接 pop(0)

## 教训
- 队列模拟栈的核心是每次 push 后重新排队，让新元素到队头
- 和 232 题对比：

| 题目       | 核心操作               | 辅助数据结构作用       |
| -------- | ------------------ | -------------- |
| 232 栈→队列 | 倒栈（s\_in → s\_out） | s\_out 缓存待出队元素 |
| 225 队列→栈 | 重新排队（q2 顶到队头）      | q2 临时中转，交换后清空  |
- 两题都是"用基础数据结构模拟另一种数据结构"，关键是理解操作顺序的反转/保持
- 平时太依赖库函数，手动模拟时暴露了基础操作不熟练的问题
