# LeetCode 503 下一个更大元素 II

## 我的思路（45分钟）
1. 前15分钟：大致写出代码，思路是循环数组 → 遍历两遍
2. 后30分钟调试：回文数组测试用例超时，排查发现 while 循环内的 if 条件里 ans 下标选错了——应该是栈顶元素的下标而非当前元素下标

## 代码
```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        s = []
        
        for j in range(2):
            for i in range(n):
                while s and nums[s[-1]] < nums[i]:
                    if ans[s[-1]] == -1:  # ← 关键：栈顶元素还没找到答案
                        ans[s[-1]] = nums[i]
                    s.pop()
                if ans[i] == -1:  # ← 只有还没找到答案的下标才入栈
                    s.append(i)
        
        return ans
```

## 关键
- 循环数组处理：遍历 range(2) 模拟走两圈
- 栈中只存"还没找到答案"的下标：if ans[i] == -1 才 append
- 更新时机：nums[s[-1]] < nums[i] 时，栈顶找到了下一个更大元素
- ans[s[-1]] 而非 ans[i]——给栈顶元素填答案

## 教训
- 变量下标搞混是高频 bug：s[-1]（栈顶下标）vs i（当前下标），写的时候必须 mentally check
- 循环数组 = 遍历两遍，但第二遍时已找到答案的元素不再入栈（ans[i] == -1 判断），避免重复处理
- 和 496 题对比：

| 题目  | 数组特性   | 处理方式             |
| --- | ------ | ---------------- |
| 496 | 两个独立数组 | 预处理 `nums2` 建哈希表 |
| 503 | 单个循环数组 | 遍历两遍 + 栈中只存未解元素  |
