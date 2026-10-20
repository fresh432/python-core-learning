# LeetCode 415 字符串相加

## 我的思路（13分钟）
- 因为之前做过 43 题乘法模拟，思路很快出来：先判 0 剪枝，再让长串在前
- 长串长度 +1 作为 ans 数组长度，短串前面补 0 对齐
- 倒序逐位相加，按个位、十位位置赋值进位，最后删掉可能多出的前导 0

## 代码
```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1

        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num_1 = [int(ch) for ch in num1]
        num_2 = [0] * (len(num1) - len(num2)) + [int(ch) for ch in num2]

        ans = [0] * (len(num1) + 1)
        for i in range(len(num1) - 1, -1, -1):
            tmp = num_1[i] + num_2[i]
            index_1 = i + 1
            index_10 = i
            res = tmp + ans[index_1]
            ans[index_1] = res % 10
            ans[index_10] += res // 10

        if ans[0] == 0:
            ans = ans[1:]
        ans = [str(num) for num in ans]
        return ''.join(ans)
```

## 关键
- 短串补 0 对齐，两个数组一样长后倒序逐位相加
- 和的位置：i+1 存个位，i 存进位（ans 长度 = 长串长度 +1）
- res 先加上 ans[index_1] 已有的进位值，再拆分

## 教训
- 看到"字符串数字相加/相乘，禁止转 int" → 竖式模拟统一套路：补 0 对齐 + 倒序 + 进位
- 和 43 题对比：43 乘法每个乘积落 i+j / i+j+1 两个位置，415 加法进位只落到 i
