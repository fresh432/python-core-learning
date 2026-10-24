# LeetCode 166 分数到小数

## 我的思路（35分钟）
- 前20分钟：想先算整数、再算小数，用哈希判断循环。但一开始想存"算出来的小数结果"，这样很难发现循环、也找不到循环入口
- 看答案5分钟：应该存"算小数时的余数 + 当前小数位的位置"，并且用长除法算每一位小数——余数一旦重复，循环的入口和结束点就确定了
- 后10分钟：按这个思路重写，判断循环 + 字符串拼接

## 代码
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        pre = numerator // denominator
        tmp = numerator % denominator

        if tmp == 0:
            return sign + str(pre)

        ans = [sign + str(pre) + "."]
        hash_tmp = {tmp: 1}
        while tmp:
            pre, tmp = tmp * 10 // denominator, tmp * 10 % denominator
            ans.append(str(pre))
            if tmp in hash_tmp:
                pos = hash_tmp[tmp]
                return f"{''.join(ans[:pos])}({''.join(ans[pos:])})"
            hash_tmp[tmp] = len(ans)
        return ''.join(ans)
```

## 关键
- 长除法逐位算小数：当前位 = tmp10 // denominator，新余数 = tmp10 % denominator
- 哈希存 余数 → 小数位位置（ans 中的下标）；余数重复即出现循环，入口就是该余数第一次出现的位置
- 拼接：非循环部分 + "(" + 循环部分 + ")"
- 处理顺序：符号 → 取绝对值 → 整数部分 → 余数为 0 直接返回

## 教训
- 看到"分数转小数，检测循环节" → 长除法 + 哈希存余数（不是存小数位！）
- 核心认知：余数决定后续所有位，余数重复 = 循环开始；小数位本身没有记忆性