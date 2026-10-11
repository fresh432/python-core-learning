# LeetCode 73 矩阵置零

## 我的思路（41分钟）
- 前11分钟：用 set_i 和 set_j 保存0的位置，然后遍历集合把对应行列置0。最坏情况空间 O(m+n)
- 中间15分钟：尝试用哈希表优化，但空间仍是 O(m+n)，时间反而更高
- 后15分钟：想到用矩阵第一行和第一列代替集合来标记，但会混淆第一行/列原本自带的0。看了答案，用两个额外变量 i_has_zero 和 j_has_zero 记录第一行/列是否原本有0，解决冲突后通过，空间 O(1)

## 代码（集合法）
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        set_i, set_j = set(), set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_i.add(i)
                    set_j.add(j)
        
        for i in set_i:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in set_j:
            for i in range(m):
                matrix[i][j] = 0
```

## 代码（最优解法，O(1)空间）
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        i_has_zero, j_has_zero = False, False
        
        # 检查第一列是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                j_has_zero = True
                break
        
        # 检查第一行是否有0
        for j in range(n):
            if matrix[0][j] == 0:
                i_has_zero = True
                break
        
        # 用第一行和第一列标记0的位置
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # 根据标记置0（除第一行第一列）
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        # 处理第一行和第一列
        if i_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if j_has_zero:
            for i in range(m):
                matrix[i][0] = 0
```

## 关键
- 第一行/列作为标记位：matrix[0][j] 标记第 j 列是否需要置0，matrix[i][0] 标记第 i 行是否需要置0
- 额外变量：记录第一行/列本身是否有0，避免标记和原始数据混淆
- 顺序：先标记（除第一行第一列）→ 再置0（除第一行第一列）→ 最后处理第一行第一列

## 教训
- 看到"矩阵中0所在的行列置0，要求原地" → 用第一行第一列做标记 + 两个额外变量记录