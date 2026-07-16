# LeetCode 739 每日温度

## 我的思路（30分钟）
1. 前10分钟：想到用栈，但没有具体思路
2. 看答案后理解：单调递减栈——栈中存的是还没找到"下一个更大元素"的日期下标。当新温度大于栈顶温度时，栈顶元素"等到了" warmer day，计算距离差后出栈

## 代码
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        
        for i, v in enumerate(temperatures):
            while st and v > temperatures[st[-1]]:
                prevI = st.pop()
                ans[prevI] = i - prevI  # 距离 = 当前下标 - 栈顶下标
            st.append(i)
        
        return ans
```

## 关键
- 单调递减栈：栈中存下标，对应温度递减
- 触发条件：当前温度 v > temperatures[st[-1]]（栈顶温度）时，栈顶找到了下一个更大元素
- 距离计算：i - prevI，当前日期减去"等待中"的日期
- 栈中剩余元素：右边没有更暖的天，保持 ans[i] = 0

## 教训
- 看到"下一个更大/更小元素" → 先想单调栈
- 单调栈存的是下标而非值，因为需要计算距离/位置
- 和 239 题对比：

| 题目          | 数据结构 | 单调方向 | 存什么    |
| ----------- | ---- | ---- | ------ |
| 239 滑动窗口最大值 | 单调队列 | 递减   | 值（或下标） |
| 739 每日温度    | 单调栈  | 递减   | 下标     |

- 单调栈 vs 单调队列：栈是"等待匹配"，队列是"滑动窗口维护最值"
- 两题都是单调结构的经典应用，239偏"窗口"，739偏"下一个更大"
