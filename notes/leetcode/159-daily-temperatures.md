# LeetCode 739 每日温度

## 我的思路（9分钟）
- 看到题立刻想到单调栈，维护一个递减栈（存下标）
- 遍历温度数组，当前温度 > 栈顶温度时，循环弹出栈顶，计算 i - stack[-1] 作为该天的等待天数
- 最后把当前下标入栈，等待后面更高的温度来"解锁"

## 代码
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        
        return ans
```

## 关键
- 单调递减栈：栈中存的是下标，对应的温度值单调递减
- 弹出条件：temperatures[i] > temperatures[stack[-1]]，当前温度比栈顶高，说明找到了下一个更高温度
- 天数差：ans[j] = i - j
- 栈中剩余元素：后面没有更高的温度，ans 保持默认值 0

## 教训
和 496/503 题对比：496 是下一个更大元素 I（数组），503 是下一个更大元素 II（循环数组），739 是每日温度（求距离而非值），核心都是单调栈

## 单调栈系列对比
| 题目             | 目标                | 栈中存    | 计算内容    |
| :------------- | :---------------- | :----- | :------ |
| 496 下一个更大元素 I  | 右边第一个更大值          | 下标     | 值       |
| 503 下一个更大元素 II | 循环数组右边第一个更大       | 下标     | 值       |
| **739 每日温度**   | **右边第一个更高温度的天数差** | **下标** | **下标差** |
