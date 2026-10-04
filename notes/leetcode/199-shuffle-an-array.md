# LeetCode 384 打乱数组

## 我的思路（25分钟）
- 前15分钟：写出基本框架——reset 返回原数组拷贝，shuffle 用随机交换打乱
- 思路：遍历每个位置，用 random.randint 获取随机下标与当前元素交换
- 后10分钟：看答案，发现两个关键修正：
  1. 随机范围：不是 0 ~ n-1，而是 i ~ n-1。0 ~ n-1 会产生 n^n 种可能（不均匀），i ~ n-1 产生 n! 种可能（全排列，最公平的随机）——这就是 Fisher-Yates 洗牌算法
  2. 深拷贝：初始化保存原数组和 reset 返回时都要用 [:] 深拷贝，防止外部修改

## 代码
```python
import random

class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]
    
    def reset(self) -> List[int]:
        return self.original[:]
    
    def shuffle(self) -> List[int]:
        arr = self.original[:]
        n = len(arr)
        for i in range(n):
            factor = random.randint(i, n - 1)
            arr[factor], arr[i] = arr[i], arr[factor]
        return arr
```

## 关键
- Fisher-Yates 洗牌算法：从后往前（或从前往后），每个位置与 [i, n-1] 范围内的随机位置交换
- random.randint(i, n-1)：保证每个排列出现的概率相等（1/n!）
- 深拷贝：nums[:] 防止引用共享导致原数组被修改

## 教训
- 看到"数组随机打乱" → Fisher-Yates 算法，randint(i, n-1) 不是 randint(0, n-1)
