# LeetCode 166 分数到小数（复习）

## 我的思路（37分钟）
- 前20分钟：基本写完，长除法 + 哈希表存余数和商的位置。
  - 先单独求整数部分加入字符串
  - 再循环处理小数部分，当余数出现在哈希表中时退出循环并标记
  - 有循环时按退出时余数对应的下标切分数组，把后面的循环部分加括号拼接
  - 最后根据符号决定是否带负号
- 后17分钟：求整数部分和小数部分的代码写得太混乱、先后顺序不顺畅，调试完才通过

## 代码
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = 0
        if numerator // denominator < 0:
            numerator, denominator = abs(numerator), abs(denominator)
            sign = 1
        hash_map = {}
        ans = []
        n = 1
        big = numerator // denominator
        small = numerator % denominator
        if small == 0:
            return "-" + str(big) if sign else str(big)
        ans.append(str(big) + ".")
        hash_map[small] = n
        n += 1
        small *= 10
        flag = 0
        while small:
            if small in hash_map:
                flag = 1
                break
            hash_map[small] = n
            n += 1
            num = small // denominator
            small %= denominator
            ans.append(str(num))
            small *= 10
        if flag:
            ans = "".join(ans[:hash_map[small] - 1]) + "(" + "".join(ans[hash_map[small] - 1:]) + ")"
        else:
            ans = "".join(ans)

        return "-" + ans if sign else ans
```

## 教训
- 复习： 20 分钟就写出了核心（长除法 + 哈希存余数），说明思路已记住；但代码组织卡了 17 分钟，整数部分、小数部分、符号处理要分块写，先后顺序画清楚再动手
- 踩坑：先存当前余数再算商、商的追加与余数更新顺序要一致，否则下标对不上