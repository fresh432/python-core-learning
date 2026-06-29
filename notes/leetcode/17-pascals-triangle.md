# LeetCode 118 杨辉三角

## 我的思路（10分钟卡住）
- 没想到先建立二维数组框架
- 对"动态构建二维结构"不熟悉，看答案后才理解

## 核心规律
- 第0行: [1]
- 第1行: [1, 1]
- 第2行: [1, 2, 1]      ← 2 = 1+1
- 第3行: [1, 3, 3, 1]   ← 3 = 1+2, 3 = 2+1
- 第4行: [1, 4, 6, 4, 1]
- 每行首尾固定为1
- 中间元素 = 上一行左上方 + 正上方

## 代码
```python
def generate(self, numRows: int) -> List[List[int]]:
    ans = [[1] * (i + 1) for i in range(numRows)]
    for i in range(2, numRows):
        for j in range(1, i):
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
    return ans
```

## 关键教训
- 二维动态构建：先建框架，再填充
- 首尾固定为1，只计算中间
- 索引对应关系：ans[i][j] 依赖 ans[i-1][j-1] 和 ans[i-1][j]
