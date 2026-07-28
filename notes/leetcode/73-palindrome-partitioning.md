# LeetCode 131 分割回文串

## 我的思路（40分钟）
1. 前20分钟：写出回溯框架，但传递给递归的是索引而非子串，一直调试找不到原因
2. 后20分钟：看答案发现——应该传的是切割后的子串进入递归，不是单个索引

## 代码
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        
        def func(ans, path, start):
            if start == len(s):           # 切割到末尾，找到一组解
                ans.append(path[:])
                return
            
            for i in range(start, len(s)):
                substr = s[start:i+1]     # 切割子串 [start, i]
                if substr == substr[::-1]:  # 是回文
                    path.append(substr)   # ← 传的是子串，不是索引！
                    func(ans, path, i+1)  # 从 i+1 继续切割
                    path.pop()
        
        func(ans, path, 0)
        return ans
```

## 关键
- 切割问题：start 是切割起点，i 是切割终点，substr = s[start:i+1]
- 回文判断：substr == substr[::-1]
- 递归传值：传 i+1（下一个切割起点），不是 start+1
- path 中存的是子串，不是索引或字符

## 教训
- 切割类回溯 vs 组合类回溯：

| 类型     | 代表题目     | path 存什么   | 递归参数        |
| ------ | -------- | ---------- | ----------- |
| 组合     | 77、39、40 | 选的数字       | 下一个可选位置     |
| **切割** | **131**  | **切割出的子串** | **下一个切割起点** |

- 我犯的错误：把 path.append(substr) 写成了传索引，导致 path 里存的是位置而非子串
- 看到"分割/切割字符串" → 回溯，for i in range(start, n)，substr = s[start:i+1]
