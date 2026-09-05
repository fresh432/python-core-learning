# LeetCode 268 丢失的数字

## 我的思路（7分钟）
- 先排序，然后遍历数组
- 若 i != nums[i]，则 i 就是丢失的数字
- 若遍历完都匹配，则丢失的数字是 n（数组长度）

## 代码
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != nums[i]:
                return i
        return n
```

## 关键
- 排序后下标与值一一对应：nums[0]=0, nums[1]=1...
- 第一个 i != nums[i] 的位置就是缺失数字
- 若全部匹配，缺失的是最后一个数 n

## 教训
- 看到"0~n中缺失一个数" → 排序比对是最直观的，但时间 O(n log n)
- 更优解法：
  - 数学法：缺失数 = n*(n+1)//2 - sum(nums)，O(n) 时间 O(1) 空间
  - 位运算法：全员异或再异或 0~n，出现两次的抵消，剩下的是缺失数
- 和 136/137 题对比：都是"找缺失/唯一"问题，136用异或（出现2次），268也可用异或（找缺失）