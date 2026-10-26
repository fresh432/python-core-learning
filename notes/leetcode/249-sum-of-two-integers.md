# LeetCode 371 两整数之和

## 我的思路（35分钟）
- 前15分钟：想到 a ^ b 得到无进位的和，a & b 得到进位但位置不对；随后想到把 a & b 左移一位就是进位
- 花5分钟写出：以进位为循环条件，循环内取无进位和与进位和；无进位和作为答案，进位和作为下一轮循环条件，进位为 0 时返回
- 调试10分钟：传入负数时死循环，查资料发现 Python 整数位数无限，进位始终有效；花5分钟加掩码模拟 32 位截断后通过

## 代码
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        Mask = 0xffffffff
        Max = 0x7fffffff
        while b & Mask:
            a, b = (a ^ b) & Mask, ((a & b) << 1) & Mask
        return a if a <= Max else ~(a ^ Mask)
```

## 关键
- a ^ b：无进位的和； (a & b) << 1：进位
- 循环条件 b & Mask（进位不为 0 就继续），b 为 0 时 a 就是答案
- 掩码 0xffffffff 模拟 32 位截断；Max 0x7fffffff 判断符号位，负数还原用 ~(a ^ Mask)

## 教训
- 看到"不用 + - 实现加法" → 位运算迭代：异或得无进位和、与后左移得进位
- 踩坑：Python 整数无限位，负数补码会无限延伸导致死循环——位运算模拟固定位数（32 位）的题目必须加掩码截断

