# LeetCode 85 最大矩形

## 我的思路（120分钟）
- 前20分钟：完全没思路，不知道如何同时维护高度和宽度
- 中间100分钟：看答案，先理解了单调栈 + DP 的解法，但想尝试纯 DP 解法；看了纯 DP 解法后，对维护左右边界数组（lefts/rights）的部分还是云里雾里，cur_left/cur_right 的滑动逻辑没完全吃透，但时间花得太多，先抄下答案通过

## 代码
```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        heights = [0] * n   # 每列当前连续1的高度
        lefts = [0] * n     # 每列当前矩形的左边界
        rights = [n - 1] * n  # 每列当前矩形的右边界
        
        for i in range(m):
            cur_left = 0
            cur_right = n - 1
            
            # 正序更新高度和左边界
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                    lefts[j] = max(cur_left, lefts[j])
                else:
                    heights[j] = 0
                    lefts[j] = 0
                    cur_left = j + 1
            
            # 倒序更新右边界并计算面积
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    rights[j] = min(cur_right, rights[j])
                    max_area = max(max_area, heights[j] * (rights[j] - lefts[j] + 1))
                else:
                    rights[j] = n - 1
                    cur_right = j - 1
        
        return max_area
```

## 关键
- 核心思想：逐行将问题转化为"柱状图中最大的矩形"（LeetCode 84）
- 三个数组：
  - heights[j]：第 j 列当前连续 '1' 的高度（当前为 '1' 则 +1，否则重置为 0）
  - lefts[j]：第 j 列当前矩形的左边界（受上一行和当前行连续 '1' 的共同限制）
  - rights[j]：第 j 列当前矩形的右边界
- 左边界更新（正序遍历）：
  - 当前为 '1'：lefts[j] = max(cur_left, lefts[j]) —— 不能比当前行连续 '1' 的左起点更左
  - 当前为 '0'：lefts[j] = 0，cur_left = j + 1（重置，下一列的左起点至少从 j+1 开始）
- 右边界更新（倒序遍历）：
  - 当前为 '1'：rights[j] = min(cur_right, rights[j]) —— 不能比当前行连续 '1' 的右终点更右
  - 当前为 '0'：rights[j] = n - 1，cur_right = j - 1（重置）
- 面积计算：heights[j] * (rights[j] - lefts[j] + 1)

## 教训
- 看到"矩阵中最大矩形" → 先想能否转化为柱状图最大矩形（84 题），用单调栈；或纯 DP 维护高度 + 左右边界
- 纯 DP 解法的难点：左右边界需要逐行继承 + 当前行限制，正序更新左边界、倒序更新右边界
- 当前为 '0' 时，heights、lefts、rights 都要重置，这是容易遗漏的点
- lefts 和 rights 的更新逻辑是对称的：左边界取 max（不能更左），右边界取 min（不能更右）
- 和 221 题对比：

|      题目     | 形状     | 维护信息          | 核心方法                 |    复杂度    |
| :---------: | :----- | :------------ | :------------------- | :-------: |
|  221 最大正方形  | 正方形    | 边长            | `min(左上,上,左) + 1`    |   O(mn)   |
| **85 最大矩形** | **矩形** | **高度 + 左右边界** | **逐行转化柱状图 / 三数组 DP** | **O(mn)** |
