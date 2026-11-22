# LeetCode 403 青蛙过河

## 我的思路（40分钟）
- 前25分钟：想 DP，感觉和走楼梯类似，但不知道怎么维护"跳到每块石头上的跨度状态"，想不出转移方程
- 看答案15分钟：dp 存的不是通常的最小步数，而是"跳到每块石头上的所有可行跳跃跨度"的集合
  - 初始化 dp[0] = {0}（起点跨度视为 0，第一次跳 1）
  - 三层循环：第一层遍历每块石头 s，第二层遍历到达 s 的所有可行跨度 step，第三层对 step 做 [-1, 0, 1] 偏移，若新跨度 > 0 且落点有石头，就把新跨度加入落点石头的集合
  - 最后判断最后一块石头的集合是否非空

## 代码
```python
from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        set_stones = set(stones)
        dp = defaultdict(set)
        dp[0] = {0}                            # 起点
        for s in stones:
            for step in dp[s]:                 # 到达 s 的所有可行跨度
                for d in [-1, 0, 1]:
                    nxt = step + d
                    if nxt > 0 and s + nxt in set_stones:
                        dp[s + nxt].add(nxt)   # 落点记下新跨度
        return len(dp[stones[-1]]) > 0
```

## 关键
- 状态设计：dp[x] = 跳到石头 x 时的可行跨度集合，"跨度"才是本题真正的状态维度
- 转移：step + d（d ∈ {-1, 0, 1}）扩展新跨度，落点必须有石头
- dp[0] = {0} 的妙处：从 0 出发第一步必须跳 1（step=0 + d ∈ {-1,0,1} 过滤后只剩 1）

## 教训
- 看到"跳跃跨度可变、问能否到达" → 状态加一维"跨度"，用集合存可行值（去重自动完成）
- 自己卡死的原因：还在套"最小步数/最值"的 DP 惯性，当转移依赖"上一步的具体决策值"（这里是跨度本身）时，状态里就必须带上这个值
