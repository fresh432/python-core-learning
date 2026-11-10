# LeetCode 307 区域和检索 - 数组可修改（复习）

## 我的思路（30分钟）
- 前15分钟：写好框架
  - 用树状数组存前缀和，每个位置按 bit 位存储
  - 更新操作从当前下标 +1 作为起点，通过不断增加最低 bit 位来更新 tree 上的前缀和
  - 查找操作通过不断减去最低 bit 位来获取该位置的前缀和
  - 两个 bit 位操作把时间复杂度都压到 O(log n)
- 后15分钟：想不起来最低 bit 位怎么获取，查了下才修改通过
- lowbit 的含义：每个 lowbit 位只保存该 bit 对应的十进制区间的数值，tree[i] 管辖区间起点为 i 减去 lowbit(i) 再加一；而 2 的 n 次方的 bit 位直接管辖从零到该位置的所有数值

## 代码
```python
class NumArray:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = [0] * self.n
        self.tree = [0] * (self.n + 1)
        for i, num in enumerate(nums):
            self.update(i, num)

    def preSum(self, index: int) -> int:
        sum_num = 0
        while index > 0:
            sum_num += self.tree[index]
            index -= index & -index   # 减最低位，下溯
        return sum_num

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] += delta
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index   # 加最低位，上溯

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum(right + 1) - self.preSum(left)
```

## 关键
- 复习：15 分钟写出框架，但lowbit = i & -i 忘了，卡住 15 分钟
- 一句话记住：lowbit(i) = i & (-i)；update 沿 i += lowbit 上溯，query 沿 i -= lowbit 下溯