# LeetCode 307 区域和检索 - 数组可修改

## 我的思路（40分钟）
- 前15分钟：想用字典存前缀和方便查找，但修改时又要 O(n) 超时；用遍历求和查找又是 O(n)
- 中间15分钟：没想出让查找和更新都小于 O(n) 的方法
- 看答案10分钟：用树状数组存值，二进制下标作索引，每个索引保存"从当前最高位到当前位置"的区间和。
  - 更新时只更新当前位置到数组最高位的值，中间通过加最低位 1（i & -i）找到下一个要更新的下标
  - 查找时累加当前下标的值，每次累加后减去最低位 1 得到下一个下标。查找和更新都只要 O(log n)

## 代码
```python
class NumArray:
    def __init__(self, nums: list[int]):
        n = len(nums)
        self.nums = [0] * n
        self.tree = [0] * (n + 1)
        for i, x in enumerate(nums):
            self.update(i, x)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1                 # 树状数组下标从 1 开始
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i               # 加上最低位 1，上溯

    def prefixSum(self, i):
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1                # 减去最低位 1，下溯
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right + 1) - self.prefixSum(left)
```

## 关键
- 树状数组（BIT）：tree[i] 管理一段以 i 结尾、长度为 lowbit(i) = i & -i 的区间
- update：delta 增量更新，i 从 index+1 沿 i += i&-i 上溯到 n，O(log n)
- prefixSum(i)：沿 i -= i&-i（即 i &= i-1）下溯到 0，O(log n)
- 区间和 = prefixSum(right+1) - prefixSum(left)
- update 与 query 方向相反：更新往上加、查询往下减，别记反

## 教训
- 看到"频繁单点修改 + 区间和查询" → 树状数组（或线段树）；朴素前缀和修改 O(n)、遍历查询 O(n)，都不行
