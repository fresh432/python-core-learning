# LeetCode 901 股票价格跨度

## 我的思路（29分钟）
- 前24分钟：维护单调递减栈 + 哈希表。
  - 栈存元素下标，哈希表存下标对应的价格。初始化先向栈加一个值，方便栈中第一个元素计算连续天数
  - 当栈顶价格 < 当前价格时出栈、哈希表删除该价格；弹出结束后当前元素入栈并记入哈希表
  - 元素下标减去栈顶下标的值即为跨度。通过
- 看答案发现可以不用哈希表：栈直接存（下标, 价格）对。花5分钟修改，只用栈维护——时空复杂度一样，代码更简洁

## 代码（哈希版）
```python
class StockSpanner:
    def __init__(self):
        self.stack = [0]
        self.prices = {0: 0}
        self.n = 1

    def next(self, price: int) -> int:
        self.prices[self.n] = price
        self.n += 1
        index = 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            tmp = self.stack.pop()
            del self.prices[tmp]
            if self.stack:
                index = self.n - 1 - self.stack[-1]
            else:
                index = self.n - 1
        self.stack.append(self.n - 1)
        return index
```

## 代码（优化版）
```python
class StockSpanner:
    def __init__(self):
        self.stack = [[-1, -1]]   # 哨兵：下标-1、价格-1，省空栈判断
        self.n = 0

    def next(self, price: int) -> int:
        # 弹出所有价格 ≤ 当前价的栈顶（它们不可能再成为后续元素的"左边界"）
        while self.stack[-1][0] != -1 and self.stack[-1][1] <= price:
            self.stack.pop()
        days = self.n - self.stack[-1][0]   # 跨度 = 当前下标 - 新栈顶下标
        self.stack.append([self.n, price])
        self.n += 1
        return days
```

## 关键
- 单调递减栈存（下标, 价格）：栈顶是左边第一个比当前价格大的元素，跨度 = 当前下标 - 栈顶下标
- 哨兵 [-1, -1]：栈空时跨度为 n - (-1) = n+1... 实际上栈空意味着之前都更小，哨兵下标 -1 让公式统一
- 每个元素最多入栈、出栈各一次，均摊 O(1)

## 教训
- 看到"连续天数/跨度，比当前小的全部出局" → 单调递减栈存（下标, 值），跨度用下标差
- 栈里能一起存的信息不要拆出去用哈希表——价格和下标本就是一对，拆成两个结构反而引入删除同步的麻烦
- 和 739 对比：739 存下标查数组得温度（找右边第一个更大），901 栈内直接存（下标, 价格）算跨度（找左边第一个更大）——一右一左，都是单调栈