# LeetCode 54 螺旋矩阵

## 我的思路（35分钟）
- 之前做过 59 题（螺旋矩阵 II），对收缩边界印象深刻——大循环套四个小循环，分别遍历上、右、下、左四条边，每遍历完一条边就收缩对应的边界
- 前15分钟：写出基本框架
- 后20分钟：循环结束条件调试。想寻找比"每个小循环后判断边界"更优雅的方法，但没找到，最终选择在每个小循环结束后判断边界是否交叉（u > d 或 l > r），通过

## 代码
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        l, r, u, d = 0, n - 1, 0, m - 1
        
        while True:
            # 上边：从左到右
            for j in range(l, r + 1):
                ans.append(matrix[u][j])
            u += 1
            if u > d: break
            
            # 右边：从上到下
            for i in range(u, d + 1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r: break
            
            # 下边：从右到左
            for j in range(r, l - 1, -1):
                ans.append(matrix[d][j])
            d -= 1
            if u > d: break
            
            # 左边：从下到上
            for i in range(d, u - 1, -1):
                ans.append(matrix[i][l])
            l += 1
            if l > r: break
        
        return ans
```

## 关键
- 四个边界：l（左）、r（右）、u（上）、d（下）
- 遍历顺序：上 → 右 → 下 → 左，每遍历完一条边就收缩对应边界
- 结束条件：每次收缩后判断边界是否交叉（u > d 或 l > r）
- 和 59 题几乎 identical：59 是生成螺旋矩阵（赋值），54 是读取螺旋矩阵（取值）

## 教训
- 看到"螺旋遍历矩阵" → 收缩边界法，大循环套四个方向的小循环
- 结束判断必须在每次边界收缩后立即检查，不能等四轮都走完
- 和 59 题对比：59 是螺旋矩阵 II（n×n，生成），54 是螺旋矩阵（m×n，读取），核心逻辑完全相同
