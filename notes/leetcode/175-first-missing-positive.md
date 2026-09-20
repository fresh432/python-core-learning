# LeetCode 41 缺失的第一个正数

## 我的思路（60分钟）
- 前15分钟：想到哈希表存值，但题目要求常数空间，排除。转而想到原地下标修改（原地哈希）——把大于0且小于数组长度的值归位到其值对应的下标处（即数字 x 放到下标 x-1），然后再遍历一遍，第一个 nums[i] != i+1 的位置就是答案
- 中间30分钟：研究原地修改实现。先想用递归传下标逐个归位，写了半天感觉有问题；改回 for 循环归位，但判断归位条件时用了 nums[i] = i 的方式，没处理重复数，导致相同数字反复交换死循环，一直调试不过
- 后10分钟：看答案，了解防重复关键——判断条件要套一层 nums[nums[i] - 1] != nums[i]，确保目标位置已经是正确数字时才停止交换
- 后5分钟：按正确思路重写，通过

## 代码
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 原地哈希：把数字 x 放到下标 x-1 处
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                targetIndex = nums[i] - 1
                nums[i], nums[targetIndex] = nums[targetIndex], nums[i]
        
        # 找第一个不满足 nums[i] == i+1 的位置
        for i in range(1, n + 1):
            if nums[i - 1] != i:
                return i
        
        return n + 1
```

## 关键
- 原地哈希：数字 x（1 <= x <= n）应该放在下标 x-1
- while 循环交换：当前数字不在正确位置时，持续交换到正确位置
- 防重复条件：nums[nums[i] - 1] != nums[i]，避免相同数字导致死循环
- 第二次遍历：nums[i-1] != i 时，i 就是缺失的第一个正数
- 边界：若 1~n 都存在，则答案是 n+1

## 教训
- 看到"缺失的第一个正数，要求 O(n) 时间 O(1) 空间" → 原地哈希 / 桶排序
- 交换条件不能是简单的 nums[i] != i+1，必须是 nums[nums[i]-1] != nums[i]，否则重复数字会死循环
- 和 268 题对比：268 是缺失数字（范围 0~n，可用数学法），41 是缺失第一个正数（范围 1~n+1，需原地哈希）