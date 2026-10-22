# LeetCode 264 丑数 II

## 我的思路（40分钟）
- 前35分钟：想到三指针 DP——给 2、3、5 三个因子各配一个指针，每次选出三者的最小值放入 dp[i]，选中的指针加一；去重靠判断两个指针乘因子后是否相等。但报指针越界，调试无果，一度以为思路错了
- 看提示就是三指针 DP，与我的思路一致，问题出在去重部分
- 后5分钟：重写并优化条件判断——只判断各因子乘指针值是否等于当前最小数，等于则指针前进，用三个并列 if 简化后通过

## 代码
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        index_2 = 0
        index_3 = 0
        index_5 = 0
        for i in range(1, n):
            num1 = dp[index_2] * 2
            num2 = dp[index_3] * 3
            num3 = dp[index_5] * 5
            num = min(num1, num2, num3)
            if num == num1:
                index_2 += 1
            if num == num2:
                index_3 += 1
            if num == num3:
                index_5 += 1
            dp[i] = num
        return dp[-1]
```

## 关键
- 三指针 DP：dp[i] = min(2·dp[i_2], 3·dp[i_3], 5·dp[i_5])
- 去重：三个并列 if（不是 if-elif）——当最小值同时等于多个候选时，所有相等因子对应的指针都要前进
- dp[0] = 1，丑数序列从 1 开始

## 教训
- 看到"第 n 个丑数/只含因子 2、3、5 的数" → 三指针 DP
- 踩坑：去重部分没处理好导致指针越界；核心技巧是"谁等于最小值谁就前进"，并列 if 一次解决重复值问题
