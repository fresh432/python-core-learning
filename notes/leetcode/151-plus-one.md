# LeetCode 66 加一

## 我的思路（5分钟）
- 把数组数字拼接成字符串，转成整型加一后再转回字符串，逐位转成整型放入新列表

## 代码
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        ans = []
        for num in digits:
            number += str(num)
        number = str(int(number) + 1)
        for num in number:
            ans.append(int(num))
        return ans
```

## 关键
- 字符串转换法：数组 → 字符串 → 整数 → 加一 → 字符串 → 数组
- 利用 Python 大整数特性，无需手动处理进位

## 教训
- 看到"数组表示的数字加一" → 字符串转换法最直观，但空间复杂度较高
- 更优做法：从后往前遍历，处理进位（9→0 并继续进位，非9直接加1返回），最后判断首位是否需要插入1
- 