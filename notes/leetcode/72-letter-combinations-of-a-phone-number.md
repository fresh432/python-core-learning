# LeetCode 17 电话号码的字母组合

## 我的思路（20分钟）
1. 前10分钟：写出大致框架——字典映射数字到字母，回溯枚举所有组合
2. 后10分钟：调试通过，核心是按数字顺序，每个数字选一个字母

## 代码
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = []
        path = []
        
        def func(ans, path, start):
            if len(path) == len(digits):    # 选够 digits 长度的字母
                ans.append("".join(path))
                return
            
            for i in digits[start:start+1]:  # 当前处理的数字
                for j in dic[i]:              # 该数字对应的所有字母
                    path.append(j)
                    func(ans, path, start+1)  # 处理下一个数字
                    path.pop()
        
        if not digits:
            return []
        func(ans, path, 0)
        return ans
```

## 关键
- 字典映射：数字 → 字母字符串
- 回溯顺序：按 digits 的顺序，每个位置选一个字母
- start 控制处理到第几个数字，不是 for 循环的索引
- 空输入直接返回 []

## 教训
- 看到"多路选择组合" → 回溯，外层循环是"选择集合"，内层递归是"下一个位置"
- 和 77 题（组合）对比：77 是从一个集合选 k 个，17 是按顺序从多个集合各选一个
- 回溯的 start 含义要清晰：本题是"第几个数字"，不是"从哪个数开始选"


