# LeetCode 6 Z 字形变换

## 我的思路（25分钟）
- 前20分钟：基本写完。按行数建二维数组保存各行字符，类似螺旋矩阵——一来一回为一个周期：先从上到下把字符加入对应行，再从下到上来一遍，检查是否走到字符串尽头，没到就重复，最后拼接各行
- 排查5分钟：numRows = 1 时卡循环超时，以为是逻辑问题，最后干脆特判直接返回
之后看了其他答案优化：用 flag 维护方向，省去每轮越界检查

## 代码
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        i = 0
        count = 0
        n = len(s)
        while True:
            while count < numRows and i < n:
                ans[count].append(s[i])
                i += 1
                count += 1
            count -= 2
            while count >= 0 and i < n:
                ans[count].append(s[i])
                i += 1
                count -= 1
            count += 2
            if i == n:
                break
        ans = [''.join(s) for s in ans]
        return ''.join(ans)
```

## 代码（优化版）
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for ch in s:
            ans[i] += ch
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return ''.join(ans)
```

## 关键
- 模拟走 Z：行指针 i + 方向 flag，碰到第 0 行或第 numRows-1 行就翻转方向
- numRows = 1 必须特判，否则方向永不翻转、死循环
- 原始版"一来一回"周期填行，count 先减 2（跳过转折点重复行）

## 教训
- 看到"Z 字形/蛇形排列" → 方向翻转模拟（flag），或一来一回填行
- 和 54 题螺旋矩阵对比：都是"方向控制"问题，螺旋矩阵是二维下标转向，Z 字形是一维行指针往复
- 踩坑：numRows=1 的边界特判，方向类模拟题先想"什么情况下方向不生效"

