# LeetCode 304 二维区域和检索 - 矩阵不可变
- 我的思路（30分钟）
- 前10分钟：以为复制矩阵后遍历计算，超时
- 中间10分钟：改成保存每列前缀和，能通过但耗时高
- 后10分钟：想到二维前缀和（积分图），初始化时多给一行一列避免边界判断。公式：n_maxtrix[i][j] = matrix[i-1][j-1] + n_maxtrix[i-1][j] + n_maxtrix[i][j-1] - n_maxtrix[i-1][j-1]。查询时用容斥原理减去多余部分

## 代码
```python
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.n_maxtrix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.n_maxtrix[i][j] = (matrix[i - 1][j - 1] 
                                        + self.n_maxtrix[i - 1][j] 
                                        + self.n_maxtrix[i][j - 1] 
                                        - self.n_maxtrix[i - 1][j - 1])
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.n_maxtrix[row2 + 1][col2 + 1] 
                - self.n_maxtrix[row1][col2 + 1] 
                - self.n_maxtrix[row2 + 1][col1] 
                + self.n_maxtrix[row1][col1])
```

## 关键
- 二维前缀和：dp[i][j] 表示从 (0,0) 到 (i-1,j-1) 的矩形区域和
- 初始化公式：dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
- 查询公式：容斥原理，大矩形减去两个多余小矩形，加回重复减去的交集
- 多给一行一列：避免大量的 i>0 and j>0 边界判断

## 教训
- 看到"矩阵区域和查询，矩阵不变" → 二维前缀和，预处理 O(mn)，查询 O(1)
- 和 560 题对比：560 是一维前缀和+哈希表（子数组和为k），304 是二维前缀和（矩形区域和）
