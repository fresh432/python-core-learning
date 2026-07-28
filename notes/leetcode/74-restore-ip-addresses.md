# LeetCode 93 复原 IP 地址

## 我的思路（30分钟）
- 前10分钟：写出回溯框架——切割字符串，每段判断是否为合法 IP 段
- 中间10分钟：调试——判断子串首字符是否为 '0' 时写成了数字 0，导致逻辑错误,修改后通过
- 后10分钟：优化代码，时间降到3ms

## 代码
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        path = []
        n = len(s)
        
        def func(ans, path, start, count):
            if start == n and count == 4:       # 切割完且正好4段
                ans.append(".".join(path))
                return
            if count > 4:                       # 段数超了，剪枝
                return
            
            for i in range(start, n):
                substr = s[start:i+1]
                # 前导零不合法（"0" 可以，"01" 不行）
                if substr[0] == '0' and i > start:
                    break
                if int(substr) > 255:           # 超过 255 不合法
                    break
                path.append(substr)
                func(ans, path, i+1, count+1)
                path.pop()
        
        func(ans, path, 0, 0)
        return ans
```

## 关键
- IP 段合法性：
  1. 长度 1-3
  2. 数值 0-255
  3. 不能有前导零（"0" 合法，"01" 不合法）
- 剪枝：count > 4 直接返回；int(substr) > 255 或前导零时 break
- 和 131 题（分割回文串）同属字符串切割类回溯

## 教训
- 字符 '0' 和数字 0 的区别：substr[0] == '0' 是字符串比较，写成 0 永远是 False
- 看到"字符串分割 + 合法性判断" → 回溯，注意边界条件的细节
- 和 131 题对比：

| 题目           | 切割条件       | 额外约束               |
| ------------ | ---------- | ------------------ |
| 131 分割回文串    | 回文判断       | 无                  |
| **93 复原 IP** | **IP 段合法** | **正好4段、无前导零、≤255** |
