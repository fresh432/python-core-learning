# LeetCode 496 下一个更大元素 I

## 我的思路（15分钟）
看到题目立刻联想到 739 题（每日温度）的单调栈模式。思路明确：用单调递减栈遍历 nums2，为每个元素找到"下一个更大元素"并存入哈希表，最后查 nums1 即可。调试约10分钟通过。

## 代码
```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        s = []
        h = {}
        for i in range(n):
            while s and nums2[s[-1]] < nums2[i]:
                h[nums2[s[-1]]] = nums2[i]
                s.pop()
            s.append(i)
        
        ans = []
        for j in nums1:
            if j in h:
                ans.append(h[j])
            else:
                ans.append(-1)
        return ans
```

## 关键
- 单调递减栈遍历 nums2，栈中存下标
- 哈希表记录结果：h[当前元素] = 下一个更大元素
- 最后遍历 nums1 查表，无记录则 -1
- 739 题的"距离"变成本题的"值映射"，核心模式相同

## 教训
- 739 题的模式迁移成功！看到"下一个更大元素"→单调递减栈已成条件反射
- 两阶段处理：先预处理 nums2 建映射表，再查 nums1——空间换时间
- 和 739 题对比：

| 题目            | 单调栈作用           | 输出     |
| ------------- | --------------- | ------ |
| 739 每日温度      | 存下标等 warmer day | 距离差    |
| 496 下一个更大元素 I | 存下标建值映射         | 下一个更大值 |
