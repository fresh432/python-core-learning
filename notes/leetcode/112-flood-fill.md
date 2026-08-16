# LeetCode 733 图像渲染

## 我的思路（7分钟）
- 简单题，标准 DFS flood fill
- 从起点 (sr, sc) 出发，把与起点颜色相同且连通的区域全部染成 color

## 代码
```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        tar = image[sr][sc]  # 原始颜色
        m, n = len(image), len(image[0])
        
        def col(i, j, tar):
            image[i][j] = color
            if i > 0 and image[i - 1][j] == tar:
                col(i - 1, j, tar)
            if j > 0 and image[i][j - 1] == tar:
                col(i, j - 1, tar)
            if i < m - 1 and image[i + 1][j] == tar:
                col(i + 1, j, tar)
            if j < n - 1 and image[i][j + 1] == tar:
                col(i, j + 1, tar)
        
        if tar == color:  # 颜色相同，直接返回
            return image
        col(sr, sc, tar)
        return image
```

## 关键
- 标准 flood fill：从起点向四个方向蔓延，把颜色等于 tar 的连通区域染成 color
- 边界条件：tar == color 时直接返回，避免无限递归
- 修改原数组，不需要额外空间

## 教训
- 看到"图像填充/颜色替换" → 最基础的 DFS flood fill
- 注意 tar == color 的特判，否则已染色的格子会被反复访问
- 和 200/695/463/130/417 题对比：733 是最基础的 flood fill，其他题在此基础上增加了统计、条件判断、反向标记等变体


