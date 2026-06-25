
### 59 笔记

```markdown
# LeetCode 59 螺旋矩阵 II

## 我的思路
10分钟没思路，看答案后才理解

## 核心洞察
矩阵填充 = 四个边界逐层收缩
不是下标计算，是边界收敛问题

## 标准写法
```python
def generateMatrix(n):
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while num <= n * n:
        # 上边界：从左到右
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # 右边界：从上到下
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # 下边界：从右到左
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
        # 左边界：从下到上
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    
    return matrix
```
## 关键教训
- 矩阵问题先想"边界"而不是"下标"
- 四个边界：上、右、下、左
- 每填完一条边，对应边界收缩
- 循环条件：num <= n*n