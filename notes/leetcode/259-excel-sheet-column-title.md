# LeetCode 168 Excel 表列名称

## 我的思路（25分钟）
- 前20分钟：知道是 26 进制，但始终处理不好进位问题
- 后5分钟：看答案才知道要在取模前先减一，把 1~26 映射成 0~25，进位问题就解决了

## 代码
```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            columnNumber -= 1
            ans += chr(columnNumber % 26 + ord("A"))
            columnNumber //= 26
        return ans[::-1]
```

## 关键
- 每轮先 columnNumber -= 1：把 1~26 映射为 0~25，% 26 和 // 26 的进位才正确
- 字符转换 chr(x % 26 + ord("A"))，结果逆序返回

## 教训
- 看到"数字转 Excel 列名/26 进制" → 先减一再取模
- 进位问题的根源：这题是 1-indexed 进制，必须映射到 0-indexed 才能套标准进制转换
