# LeetCode 71 简化路径

## 我的思路（30分钟）
第一反应想到栈结构：遇到目录名入栈，遇到..出栈.
卡住：以为需要手写一个方法把 path 中的文件名单独提取出来，觉得太复杂.
看答案后：原来 path.split('/') 直接搞定，空字符串和.自动过滤，..时出栈

## 代码
```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for i in path.split('/'):
            if i == "" or i == ".":
                continue
            if i != "..":
                ans.append(i)
            elif ans:
                ans.pop()
        return '/' + '/'.join(ans)
```

## 关键
- path.split('/') 直接分割，空字符串（连续斜杠）和 .（当前目录）跳过
- ..（父目录）：栈非空时出栈
- 最后 '/' + '/'.join(ans) 拼接结果，保证以 / 开头
- 栈为空时 .. 不做处理（已在根目录）

## 教训
- 字符串分割不要想复杂，先试试 split() 能不能直接用
- 连续斜杠 // 分割后产生空字符串，自然被过滤
- 和 20 题（有效的括号）、150 题（逆波兰）同属栈的应用，但这里是"目录栈"
- 看到路径简化、表达式求值、括号匹配 → 先想栈