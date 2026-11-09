# LeetCode 410 分割数组的最大值（复习）

## 我的思路（35分钟）
- 前15分钟：写好整体框架，二分查找最小最大分段值，分段值范围为数组最大数到数组总和
  - 分段值越大分的段越少，所以当分的段少于题目要求的段数时收缩右边界、反之收缩左边界
  - 判定函数遍历数组累加，累加要超过分段值时段数加一并清零，段数超过要求返回 False，否则 True
  - 最后按二分收敛返回结果
- 后20分钟：调试边界和判定函数的边界

## 代码
```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            total = 0
            cnt = 0
            for num in nums:
                if total + num > mid:
                    cnt += 1
                    total = 0
                total += num
                if cnt >= k:
                    return False
            return True

        left, right = max(nums) - 1, sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
```

## 教训
- 复习时二分答案的整体框架（单调性 + 判定函数 + 边界）已经掌握，但边界调试仍花了 20 分钟，开区间写法 left = max - 1、while left + 1 < right、return right 要形成肌肉记忆，把调试时间压到 0
