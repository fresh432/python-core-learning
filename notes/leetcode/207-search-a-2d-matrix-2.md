# LeetCode 240 搜索二维矩阵 II

## 我的思路（36分钟）
- 前10分钟：想嵌套二分查找，先对行二分，再根据结果对列缩减边界。但发现某些情况会因为列的缩减而错过正确答案
- 中间13分钟：排查问题，改为循环每一列，对列中元素二分查找，通过但时间复杂度不够优
- 后10分钟：想从左上角开始，但发现每次移动两边都大于当前元素，无法确定方向
- 后3分钟：看提示，核心洞察——从右上角（或左下角）开始：
  - 右上角：当前元素左边都小，下边都大，可以明确排除一行或一列
  - 左上角不行：右边和下边都大，无法确定方向
- 按右上角思路重写，通过

## 代码（列二分版）
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            up, down = 0, m
            while up < down:
                mid_i = (up + down) // 2
                if matrix[mid_i][j] > target:
                    down = mid_i
                elif matrix[mid_i][j] < target:
                    up = mid_i + 1
                else:
                    return True
        return False
```

## 代码（更优解法）
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        
        while i < m and j > -1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
        
        return False
```

## 关键
- 右上角开始：matrix[i][j] 左边都小，下边都大
  - _< target_：往下走（i += 1）
  - _> target_：往左走（j -= 1）
- 每次排除一行或一列，时间 O(m+n)
- 左上角不行：右边和下边都大，无法确定搜索方向

## 教训
- 看到"行列都有序的矩阵中查找" → 从右上角或左下角开始，利用单调性排除行列
- 不要试图嵌套二分或从左上角开始，方向不确定
