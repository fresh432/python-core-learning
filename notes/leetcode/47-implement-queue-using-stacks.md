# LeetCode 232 用栈实现队列

## 我的思路（第一版15分钟 + 第二版30分钟）

### 第一版（15分钟）：以为删除队首元素需要额外维护一个列表，忘了可以直接用 pop(0) 弹出指定位置元素，走了弯路。

### 第二版（30分钟 + 看答案10分钟）：重新用"仅标准栈操作"实现。核心困惑在于如何用栈的 LIFO 模拟队列的 FIFO。看答案后理解：两个栈配合——s_in 负责入队，s_out 负责出队，当 s_out 空时把 s_in 全部倒过去。

## 代码
```python
class MyQueue:

    def __init__(self):
        self.s_in = []
        self.s_out = []

    def push(self, x: int) -> None:
        self.s_in.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s_out.pop()

    def peek(self) -> int:
        if not self.s_out:
            while self.s_in:
                self.s_out.append(self.s_in.pop())
        return self.s_out[-1]

    def empty(self) -> bool:
        if not self.s_in and not self.s_out:
            return True
        else:
            return False
```

## 关键
- 双栈分工：s_in 只负责 push，s_out 只负责 pop/peek
- 倒栈时机：s_out 为空时，把 s_in 全部 pop() 到 s_out，顺序自然反转
- 均摊 O(1)：每个元素最多被压入/弹出两次
- empty() 检查两个栈是否都为空

## 教训
- Python 列表 pop(0) 是 O(n)，但题目限制"只能用栈操作"（pop() 是 O(1)），所以必须用双栈
- 栈模拟队列的核心是反转两次 = 恢复原序
- 先做了 225 题（队列实现栈）再回来重做 232，发现两题思路对称但细节不同：栈→队列是"倒栈"，队列→栈是"留头"