# LeetCode 528 按权重随机选择

## 我的思路（45分钟）
- 前12分钟：把权重转换成对应数量的下标存入新数组，调用时随机取值——权重数字较大时内存溢出存不下
- 中间23分钟：尝试用计数方式模拟"随机访问到一定次数后必定出某数字"——方向有问题，每个下标该计多少次始终没弄清
- 看答案10分钟：把每个权重转换为区间（前缀和），让随机数落在总权重的大区间内，二分查找判断落在哪一段区间

## 代码
```python
class Solution:
    def __init__(self, w: list[int]):
        self.n = len(w)
        self.nums = [0] * (self.n + 1)
        self.total = sum(w)
        for i in range(1, self.n + 1):
            self.nums[i] = self.nums[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        target = random.randint(0, self.total - 1)
        left, right = 1, self.n
        while left < right:
            mid = (left + right) // 2
            if self.nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right - 1
```

## 关键
- 前缀和把权重变成连续区间：nums[i] 表示前 i 个权重的累计和，第 i 个下标占据 [nums[i], nums[i+1]) 的区间
- 随机 target ∈ [0, total)，二分找第一个 nums[mid] > target 的位置，返回 mid - 1（数组下标从 0 计）
- 初始化 O(n)，每次 pick 二分 O(log n)

## 教训
- 看到"按权重随机选择" → 前缀和 + 二分查找，一行 random 定区间
- 权重展开法会内存溢出（权重值大时数组爆炸）→ 用前缀和把"数量"压缩成"区间端点"
- 计数模拟的方向性错误要果断放弃——当"每个元素该计多少次"想不清时，说明抽象层级选错了
