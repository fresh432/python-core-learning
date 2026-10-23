# LeetCode 29 两数相除

## 我的思路（26分钟）
- 先判断被除数与除数的正负关系，保存结果正负标记 flag，两数取绝对值
- 初始化栈存（除数，对应的原始倍率），count 表示当前除数倍率
- 第一重循环：被除数 >= 除数时，ans 加上当前倍率，被除数减去当前除数，（除数，倍率）入栈，然后除数与倍率同时翻倍
- 第二重循环：栈不为空时，弹出一组（除数，倍率），重复减法操作（不再入栈、不再翻倍），减不动了就弹出下一组，直到栈空
- 返回时按 flag 取正负
- 溢出特判：被除数为 -2³¹ 且除数为 -1 时结果溢出，由于输入都在 int 范围内，溢出只有这一种情况，直接特判返回 2³¹-1

## 代码
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            flag = 1
        else: flag = -1
        dividend, divisor = abs(dividend), abs(divisor)
        stack = []
        count = 1
        ans = 0
        while dividend >= divisor:
            dividend -= divisor
            ans += count
            stack.append([divisor, count])
            divisor += divisor
            count += count
        while stack:
            tmp = stack.pop()
            while dividend >= tmp[0]:
                dividend -= tmp[0]
                ans += tmp[1]
        return ans if flag == 1 else -ans
```

## 关键
- 翻倍逼近：除数与倍率同时翻倍，快速逼近商；减不动了就把每轮的（除数，倍率）入栈
- 第二阶段从栈弹出回退细减：相当于把商按二进制位逐位确定
- 时间复杂度 O((log n)²)：外层最多 log n 轮翻倍，内层回退同样 log n 轮
- 溢出只有 -2³¹ / -1 一种，特判返回 2³¹-1

## 教训
- 看到"不用乘除取模实现除法" → 翻倍逼近 + 栈回退（或位运算版本）
- 和 50 题快速幂对比：都是"倍增"思想——快速幂是平方减半幂，这里是翻倍逼近商
