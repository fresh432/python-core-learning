# LeetCode 43 字符串相乘

## 我的思路（40分钟）
- 前20分钟：想不出不违反限制（不能直接把整个字符串转 int）的写法，纠结难道要字符与数字一对一匹配
- 中间15分钟：看答案，发现可以对单个字符分别转换。初始化结果数组，两个字符串倒序逐字符相乘，结果倒序存入数组，去掉首位 0 后拼接返回
- 后5分钟：按这个方法实现一遍

## 代码
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num_1 = [int(ch) for ch in num1]
        num_2 = [int(ch) for ch in num2]
        ans = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                res = num_1[i] * num_2[j]
                index_1 = i + j + 1
                index_10 = i + j
                res += ans[index_1]
                ans[index_1] = res % 10
                ans[index_10] += res // 10

        if ans[0] == 0:
            ans = ans[1:]
        ans = [str(num) for num in ans]
        return ''.join(ans
```

## 关键
- num1[i] × num2[j] 的结果落在位置 i+j（存进位）和 i+j+1（存个位）
- res 先加上 ans[index_1] 已有的低位值，再拆成个位和进位
- 结果数组长度 len1 + len2，处理完判断首位是否为 0
- "限制不能直接转 int"针对的是整个字符串，单个字符转换没有问题

## 教训
- 看到"字符串数字相乘，禁止直接转 int" → 竖式乘法模拟，倒序遍历 + 结果数组
- 核心映射：num1[i] * num2[j] → 位置 i+j（高位）、i+j+1（低位）
