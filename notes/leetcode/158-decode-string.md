# LeetCode 394 字符串解码

## 我的思路（50分钟）
- 前10分钟：想到用递归，但细节处理不到位（括号嵌套、数字解析、字符串拼接顺序）
- 中间10分钟：调试没通过
- 中间15分钟：看答案，理解了辅助栈法和递归法两种实现
- 后15分钟：把两个方法都写了一遍

## 代码（栈方法）
```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        
        return res
```

## 代码（递归法）
```python
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        
        return dfs(0)
```

## 关键
- 栈方法：
  - 遇到 '['：把当前 [multi, res] 入栈，重置 res 和 multi
  - 遇到 ']'：弹出栈顶，拼接 last_res + multi * current_res
  - 数字：累积解析多位数 multi = multi * 10 + int(c)
- 递归法：
  - 遇到 '['：递归处理子串，返回处理后的 (新索引, 子串结果)
  - 遇到 ']'：返回当前结果给上层
  - 数字和字母的处理与栈方法类似

## 教训
- 看到"字符串解码 / 嵌套括号展开" → 栈或递归，核心都是遇到 '[' 保存上下文，遇到 ']' 恢复并计算
- 数字可能是多位数（如 100[abc]），需要 multi * 10 + int(c) 累积解析
- 递归法需要返回索引，因为处理完子串后要从 ']' 之后的位置继续
- 和 71 题对比：71 是简化路径（栈处理路径段），394 是嵌套解码（栈保存 multi 和 res 上下文）

## 字符串处理栈系列对比
| 题目            | 场景       | 栈中保存               | 触发条件                |
| :------------ | :------- | :----------------- | :------------------ |
| 20 有效的括号      | 括号匹配     | 左括号                | 遇到右括号弹出比对           |
| 71 简化路径       | 路径规范化    | 路径段                | 遇到 `..` 弹出，`/` 分割   |
| **394 字符串解码** | **嵌套展开** | **`[multi, res]`** | **`[` 入栈，`]` 弹出计算** |
