# LeetCode 190 颠倒二进制位

## 我的思路（8分钟）
- 给定数字是 32 位整数，只需循环 32 次：每轮把 n 的最低位添加到 ans 的最低位，n 右移、ans 左移，遍历完即完成整个 bit 位颠倒

## 代码
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | n & 1
            n >>= 1
        return res
```

## 关键
- 每轮两步：res 左移一位腾位置，或上 n 的最低位（n & 1）；n 右移一位
- 固定循环 32 次（题目给定 32 位整数，高位 0 也要参与颠倒）

## 教训
- 看到"颠倒/反转二进制位" → 逐位搬运：res 左移 + n 右移，循环固定位数
