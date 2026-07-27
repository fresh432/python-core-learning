# LeetCode 39 组合总和

## 我的思路（60分钟）
- 前30分钟：想用倒序遍历加回溯，但写到后面发现逻辑太绕，实现困难
- 后30分钟：看答案后重新写——排序 + 正序遍历 + 允许重复选择，start 参数控制从当前位置开始选，避免重复组合

## 代码
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        def func(path, target, choices, start, ans):
            if target == 0:         # 找到一组解
                ans.append(path[:])
                return
            
            for i in range(start, len(choices)):
                if target - choices[i] < 0:  # 剪枝：排序后，后面的数更大
                    break
                path.append(choices[i])
                func(path, target - choices[i], choices, i, ans)  # i 不是 i+1，允许重复选
                path.pop()
        
        candidates.sort()
        start = 0
        func(path, target, candidates, start, ans)
        return ans
```

## 关键
- 允许重复选择：递归传 i 而不是 i+1，同一个数可以选多次
- 排序后剪枝：target - choices[i] < 0 时 break，因为后面的数更大
- start 保证组合不重复：每次从当前位置开始，避免 [2,3] 和 [3,2] 被视为不同组合

## 教训
- 倒序遍历不是回溯的标准写法，正序 + start 参数更清晰
- 看到"无限制重复选取 + 和为目标值" → 回溯，start 传 i（不是 i+1）
- 和 216 题对比：

| 题目           | 数字范围    | 重复选取  | 个数限制  |
| ------------ | ------- | ----- | ----- |
| 216 组合总和 III | 1-9     | 否     | 选 k 个 |
| **39 组合总和**  | **无限制** | **是** | **无** |
