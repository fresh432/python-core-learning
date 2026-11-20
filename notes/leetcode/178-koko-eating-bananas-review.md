# LeetCode 875 爱吃香蕉的珂珂（复习）

## 我的思路（11分钟）
- 二分答案：先初始化左右边界，左边界最少是"香蕉总数 ÷ 总时间"的上界，右边界最多是数量最多那堆的个数
- 二分猜速度、算总时间和给定时间比较，然后收缩窗口，最后留下来的就是最小速度

## 代码
```python
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = (sum(piles) + h - 1) // h, max(piles)

        while left < right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid   # 该堆需要的小时数（向上取整）
            if time > h:                          # 速度太慢，调快
                left = mid + 1
            else:
                right = mid
        return left
```

## 教训
- 复习： 11 分钟一遍过，"二分速度 + 算时间判定"已熟
- 本题特有的细节：每小时吃 mid 根、吃不完留到下一小时 → 单堆耗时是 ceil(pile / mid) 即 (pile + mid - 1) // mid，这个向上取整的写法是本题区别于 410/1011 判定函数的地方
