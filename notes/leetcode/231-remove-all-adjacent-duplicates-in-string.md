# LeetCode 1047 删除字符串中的所有相邻重复项

## 我的思路（14分钟）
- 前12分钟：遍历字符串每个元素，若当前元素等于下一个元素，则拼接字符串抛弃这两个重复字符，长度减二以便退出循环，同时下标回退继续判断。能通过，但嵌套循环加字符串反复拼接，时间复杂度高
- 后2分钟：看答案想起类似括号匹配的栈操作，用栈写了一遍，一次通过

## 代码（栈匹配）
```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
```

## 代码（嵌套循环）
```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        n = len(s)
        ans = s
        while i < n:
            while i >= 0 and i + 1 < n and ans[i] == ans[i + 1]:
                ans = ans[:i] + ans[i + 2:]
                n -= 2
                i -= 1
            i += 1
        return ans
```

## 关键
- 栈匹配：当前字符与栈顶相同则弹出（消除一对），不同则入栈
- 栈顶始终代表"当前待匹配的邻居"，与括号匹配同理
- 嵌套循环法每次字符串拼接是 O(n)，整体 O(n²)；栈是 O(n)

## 教训
- 看到"相邻重复项成对消除" → 栈（类比括号匹配），不要字符串反复拼接
- 凡是需要"回退到上一个位置重新判断"的场景，本质就是栈能做的事
