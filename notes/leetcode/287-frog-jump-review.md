# LeetCode 403 青蛙过河（复习）

## 我的思路（20分钟）
- 前12分钟：DP 写法
  - dp 保存每个石头的所有可行跨度，数组本身有序直接遍历
  - 三层循环：第一层遍历所有石头，第二层遍历当前石头保存的可行跨度，第三层遍历跨度的偏移（[-1, 0, 1]）
  - 若从某石头的可行跨度偏移后到达另一块石头，就把本次跨度保存到对应石头的 dp 中
  - 判断条件：可行跨度必须为正数（不能原地不动或倒退跳）
  - 最后判断最后那块石头上有没有可行跨度
- 后8分钟：递归写法
  - 从每块石头一路向可到达的所有石头走，走到最后一块石头返回 True，否则 False
  - 石头有被重复走的可能，所以加 @cache 避免重复运算
  - 先用每个石头作为 key、下标作为 value 初始化哈希表
  - 递归先判断传入石头的下标是否是最后一块，是则直接返回 True，否则遍历跨度偏移，偏移跨度不为零且目标石头存在于哈希表，则用目标石头下标和新跨度递归
  - 所有偏移都不能到达则返回 False
- 辨析：这题石头有序且不重复，递归传下标和传石头等价，传石头不用写下标对照表、直接用 set；传下标可防止重复值，且下标更通用

## 代码
```python
from functools import cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        pos = {v: i for i, v in enumerate(stones)}

        @cache
        def dfs(i, step):
            if i == n - 1:
                return True
            for k in [-1, 0, 1]:
                tmp = stones[i] + step + k
                if step + k > 0 and tmp in pos:
                    if dfs(pos[tmp], step + k):
                        return True
            return False

        return dfs(0, 0)
```

## 教训
- 复习： 20 分钟双解法（40 → 20），"dp[x] = 可行跨度集合"与"dfs（下标， 跨度） + @cache"等价互换
