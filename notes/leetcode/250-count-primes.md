# LeetCode 204 计数质数

## 我的思路（40分钟）
- 前25分钟：想不出精确筛选质数的方法
- 看答案10分钟——埃氏筛：数组先全标记为 1，逐步筛除非质数，最后返回剩余 1 的个数。筛选只需在 2 到 √n 内进行，因为大于 √n 的非质数已被更小的质数筛过；每次从当前质数的平方开始筛（该质数到其平方之间的合数已被更小质数筛除），筛除当前质数的所有倍数即可
- 后5分钟：按这个方法写了一遍

## 代码
```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = 0
        return sum(isPrime)
```

## 关键
- 埃氏筛：isPrime 数组标记，合数全部置 0，返回 sum
- 外层只需到 √n：大于 √n 的合数必有 ≤ √n 的质因子，已被筛过
- 内层从 i * i 开始、步长 i：i 到 i² 之间的合数已被更小的质数筛过，无需重复

## 教训
- 看到"统计质数个数/筛选质数" → 埃氏筛模板
- 两个核心优化：筛到 √n 为止、从 i² 开始筛倍数——都是"合数必有小质因子"的推论