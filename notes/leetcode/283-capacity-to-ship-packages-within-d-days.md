# LeetCode 1011 在 D 天内送达包裹的能力

## 我的思路（30分钟）
- 前15分钟：感觉这题莫名熟悉，直觉是二分查找；后想起来因为"最低载重"答案是单调的，所以就是二分猜最小载重，根据候选载重算运输天数：天数小于要求说明载重还能减小（收缩右边界），反之收缩左边界
- 初始左边界 = 数组中最重的单个包裹，右边界 = 重量总和
- 判定：维护临时载重 s 装货，超过当前候选载重就将天数加一并清零，最后按天数与 D 的比较收缩边界

## 代码
```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            s = 0
            cnt = 1                  # 第一天
            for w in weights:
                if s + w > mid:      # 当天装不下，开新的一天
                    cnt += 1
                    s = 0
                s += w
            if cnt > days:           # 天数超了，载重太小
                left = mid + 1
            else:
                right = mid
        return left
```

## 关键
- 单调性：载重 capacity 越高 ⇒ 所需天数越少，满足二分答案条件
- 边界：left = max(weights)（最重包裹必须能装下），right = sum(weights)（一天全装）
- 判定函数：贪心按天累加，超 capacity 就开新的一天

## 教训
- 看到"D 天内运完的最小载重" → 二分答案 + 贪心算天数，与 410（最小化最大段和）、875（最小化速度）是同一个模板
- 三个题归一类：最小化最大值 / 最大化最小值 + 判定单调 → 二分答案；判定函数的写法都是"贪心扫描 + 计数 + 与限制比较"
- 首次做时"莫名熟悉"的直觉来自 410，这类题的识别信号是"至少/至多 D 个单位完成，求最值"