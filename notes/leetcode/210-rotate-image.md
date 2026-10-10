# LeetCode 48 旋转图像

## 我的思路（35分钟）
- 前25分钟：想用类似螺旋矩阵的思路，一圈一圈交换四条边。用临时数组保存要交换的边，然后统一交换。但交换逻辑复杂，调试许久始终不过
- 后10分钟：转换思路——先转置矩阵（沿对角线交换），再反转每一行，即可达到顺时针旋转90度的效果
- 改完后成功通过

## 代码
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # 转置：沿主对角线交换
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 反转每一行
        for i in range(n):
            matrix[i] = matrix[i][::-1]
```

## 关键
- 转置：matrix[i][j] 和 matrix[j][i] 交换，注意 j 从 i+1 开始避免重复交换
- 反转每行：matrix[i][::-1]，Python 切片简洁实现
- 等价操作：转置 + 行反转 = 顺时针旋转90度

## 教训
- 看到"矩阵顺时针旋转90度" → 先转置再反转每行，不要试图一圈一圈交换
- 时间复杂度：O(n²)，空间复杂度：O(1)（原地修改）