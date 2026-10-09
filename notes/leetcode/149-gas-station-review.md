# LeetCode 134 加油站（复习）

## 我的思路（35分钟）
- 前15分钟：写出核心逻辑——初始化 ans 和 fee，遍历所有站点，fee += gas[i] - cost[i]，若 fee < 0 则从失败点的下一个位置重新出发（ans = i + 1, fee = 0）
- 后20分钟：忘了总油量小于总消耗的剪枝，导致处理"答案不存在"的情况时调试了很久。最后看了之前提交过的代码才发现少了 if sum(gas) < sum(cost): return -1
- 加上剪枝后通过

## 代码
```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        ans, fee = 0, 0
        
        for i in range(n):
            fee = fee + gas[i] - cost[i]
            if fee < 0:
                ans, fee = i + 1, 0
        
        return ans
```

## 关键
- 总收支平衡：sum(gas) >= sum(cost) 是存在解的充要条件
- 贪心重置：从 ans 出发，累计 fee，若 fee < 0 说明 [ans, i] 内任何位置作为起点都不可达，直接从 i+1 重新开始
- 剪枝：sum(gas) < sum(cost) 时直接返回 -1

## 教训
- 看到"环形数组能否走完一圈" → 先判断总收支，再贪心重置起点
- 剪枝不要忘：sum(gas) < sum(cost) 是快速排除无解情况的关键
- 复习价值：经典贪心题，剪枝条件和重置逻辑是易错点
