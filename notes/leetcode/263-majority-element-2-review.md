# LeetCode 229 多数元素 II（复习）

## 我的思路（8分钟）
- 每次候选两个数字。遍历每个数字时：先判断是否与候选数相同（相同则对应选票 +1）；再判断是否需要补新候选（某候选票数为 0 则换为当前数字、票重置为 1）；都不符合则两个候选的选票都减一
- 候选完后还要验证：候选只是"幸存者"，需再遍历一次数组判断两个候选的出现次数是否大于 n/3，符合的加入 ans 返回

## 代码
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a, b = 0, 0
        v_a, v_b = 0, 0
        n = len(nums)
        for num in nums:
            if num == a:
                v_a += 1
            elif num == b:
                v_b += 1
            elif v_a == 0:
                a = num
                v_a += 1
            elif v_b == 0:
                b = num
                v_b += 1
            else:              # 与两候选都不同，同归于尽
                v_a -= 1
                v_b -= 1
        c_a, c_b = 0, 0
        for num in nums:       # 二次验证
            if num == a:
                c_a += 1
            elif num == b:
                c_b += 1
        ans = []
        if c_a > n // 3:
            ans.append(a)
        if c_b > n // 3:
            ans.append(b)
        return ans
```

## 教训
- 复习： 8 分钟一遍通过，双候选人摩尔投票（匹配加票、出缺换人、双减、二次验证）已完全掌握