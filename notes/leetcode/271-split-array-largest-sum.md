# LeetCode 410 分割数组的最大值

## 我的思路（35分钟）
- 前20分钟：没有丝毫头绪，只知道分完段后的最小"最大和"至少为数组中的最大值
- 看答案15分钟：遍历可能的单段上限 mx，按 mx 贪心分段
  - 发现 mx 越小分出的段数越多、mx 越大段数越少，题目转化为：找最小的 mx 使分出的段数 ≤ k。于是二分 mx，另写判定函数按 mx 分段计数
  - 段数超过 k 说明 mx 小了、收缩左边界，反之收缩右边界。二分边界：left = 数组最大值，right = 数组总和

## 代码
```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx):            # 每段和 ≤ mx 时，能否在 k 段内分完
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                    continue
                if cnt == k:      # 段数已用完还放不下
                    return False
                cnt += 1
                s = x
            return True

        left = max(nums) - 1      # 开区间左界：check(left) 必为 False
        right = sum(nums)         # 开区间右界：check(right) 必为 True
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
```

## 关键
- 单调性：mx ↑ ⇒ 所需段数 ↓，答案满足"二分答案"的条件
- check(mx)：贪心累加，超过 mx 就切段；段数 > k 返回 False
- 二分区间：[max(nums), sum(nums)]；开区间写法 left = max - 1
- 复杂度：O(n log(sum - max))

## 教训
- 看到"分割成 k 段使最大段和最小" → 二分答案 + 贪心判定，答案下界 max(nums)、上界 sum(nums)
- 判定函数的写法套路：贪心扫描 + 计数 + 与限制值比较