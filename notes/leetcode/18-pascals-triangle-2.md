# LeetCode 119 杨辉三角 II

## 我的思路
- 先按118思路写出完整二维版本（7分钟）
- 边界处理耽误了一会
- 尝试空间优化，花了15分钟没成功

## 完整二维版本（和118一样）
```python
def getRow(self, rowIndex: int) -> List[int]:
    c = [[1] * (i + 1) for i in range(rowIndex + 1)]
    for i in range(2, rowIndex + 1):
        for j in range(1, i):
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
    return c[rowIndex]
```

## 空间优化尝试
```python
# 错误代码
ans = [1] * (rowIndex + 1)
for i in range(rowIndex - 1):
    for j in range(1, i):
        # 正序更新，ans[j-1] 已被覆盖，结果错误
        ans[j] = ans[j-1] + ans[j]
```

## 正确优化：滚动数组 + 倒序更新
```python
def getRow(rowIndex):
    ans = [1] * (rowIndex + 1)
    
    for i in range(2, rowIndex + 1):
        # 必须倒序！从后往前更新，避免覆盖
        for j in range(i - 1, 0, -1):
            ans[j] = ans[j-1] + ans[j]
    
    return ans
```

## 关键教训
- 空间优化：滚动数组，只保留一行
- 必须倒序更新，正序会覆盖未使用的值
- 倒序是"依赖上一行"问题的通用技巧
- 我的错误：试图用额外数组c中转，逻辑混乱
