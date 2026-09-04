# LeetCode 134 加油站

## 我的思路（35分钟）
- 前15分钟：纠结是否需要切环模拟——让数组首尾相连，从每个站点出发真的跑一圈来验证，但感觉时间复杂度太高
- 中间10分钟：想到核心洞察——先判断总收支平衡：若 sum(gas) < sum(cost)，直接返回 -1（总油量不够总消耗，不可能跑完）。若收入大于支出，则必然存在一个解
- 后10分钟：贪心遍历，维护当前油量 fee，若 fee < 0 说明从当前起点到 i 不可达，将起点改为 i+1，fee 重置为0

## 代码
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        fee = 0
        ans = 0
        for i in range(len(gas)):
            fee = fee + gas[i] - cost[i]
            if fee < 0:
                fee = 0
                ans = i + 1
        
        return ans
```

## 关键
- 总收支平衡：sum(gas) >= sum(cost) 是存在解的必要条件，也是充分条件
- 贪心：从 ans 出发，累计 fee += gas[i] - cost[i]
- 不可达时重置：若 fee < 0，说明从 ans 到 i 这段路中任何位置作为起点都不可达（因为到 i 时油量不足，从中间任何位置出发到 i 时油量更少），所以直接从 i+1 重新开始

## 教训
- 看到"环形数组/能否走完一圈" → 先判断总收支，再贪心重置起点
- 关键证明：若 [ans, i] 不可达，则 [ans, i] 内任何位置作为起点都不可达。因此可以安全跳过这段，直接从 i+1 开始
- 和 55 题对比：55 是判断能否跳到末尾（维护 reach），134 是找起点+判断能否环形走完（维护 fee 并重置起点）
