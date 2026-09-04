# LeetCode 137 只出现一次的数字 II

## 我的思路（70分钟）
- 前10分钟：知道应该用位运算，但想不出具体实现
- 中间30分钟：看答案的位运算解法——统计所有数字在每一位上的1的个数，对3取模，剩下的就是只出现一次数字在该位上的值。理解了思路但看不懂代码实现
- 后15分钟：看到快速选择（随机枢轴+partition）的解法：随机选 pivot，partition 后看左边长度对3取模，不为0则答案在左边，否则收敛到右边重复。时间复杂度期望 O(n)
- 后10分钟：跟着快速选择的思路写了一遍
- 最后5分钟：受到快速选择的启发，想到更简单的方法——先排序，再用快慢指针每次跳3步比对。若 nums[i] != nums[i+1]，则 nums[i] 就是答案。3ms 通过

## 代码（快速选择法）
```python
import random

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            k = randint(l, r)
            nums[k], nums[r] = nums[r], nums[k]
            i, j = l, r - 1
            
            while i <= j:
                while i < r and nums[i] <= nums[r]:
                    i += 1
                while j >= l and nums[j] > nums[r]:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            
            nums[i], nums[r] = nums[r], nums[i]
            
            if (i - l + 1) % 3 != 0:
                r = i
            else:
                l = i + 1
        
        return nums[l]
```

## 代码（排序+快慢指针法）
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i + 1 < len(nums):
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 3
        return nums[-1]
```

## 关键
- 位运算思路（理论最优）：统计32位中每一位的1的个数，对3取模，空间 O(1)，但代码晦涩
- 快速选择：类似快排的 partition，利用"其余数字出现3次"的性质，通过区间长度对3取模判断答案在哪一侧
- 排序+跳3步：排序后相同的3个数字必然相邻，快慢指针每次跳3步，遇到不匹配的就是答案

## 教训
- 看到"其余出现k次，只有一个出现1次" → 位运算是理论最优解
- 和 136 题对比：136 是其余出现2次（异或即可），137 是其余出现3次（需要位运算或排序跳3步）

## "只出现一次"系列对比
| 题目                  | 其余出现次数 | 方法              | 核心操作                      |
| :------------------ | :----- | :-------------- | :------------------------ |
| 136 只出现一次的数字        | 2次     | 位运算             | 全员异或                      |
| **137 只出现一次的数字 II** | **3次** | **位运算 / 排序跳3步** | **统计位1的个数对3取模 / 排序后i+=3** |
