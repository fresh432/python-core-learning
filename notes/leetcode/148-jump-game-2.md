# LeetCode 45 跳跃游戏 II

## 我的思路（40分钟）
- 前15分钟：用 DP 写了一遍，dp[i] 表示跳到 i 的最少步数，但时间复杂度O(n²)，耗时3126ms太慢
- 中间15分钟：看答案，核心洞察——贪心"造桥法"：遍历数组时维护当前能到达的最远边界 next_end，当走到当前桥的终点 cur_end 时，必须再跳一次，把桥铺到 next_end，计数加一
- 后10分钟：根据思路写出贪心版本，3ms

## 代码（DP，超时边缘）
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                if i + j == n:
                    break
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]
```

## 代码（贪心造桥法，最优）
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_end = 0      # 当前这步能覆盖的最远边界（桥头）
        next_end = 0     # 下一步能覆盖的最远边界（造桥）
        
        for i in range(len(nums) - 1):  # 不用遍历最后一个元素
            next_end = max(next_end, i + nums[i])
            if i == cur_end:            # 走到桥头，必须跳一步
                cur_end = next_end
                ans += 1
        
        return ans
```

## 关键
- 核心思想：在当前步的覆盖范围内"造桥"（更新 next_end），走到边界时跳一步
- cur_end：当前这一步跳跃能到达的最远下标
- next_end：从当前覆盖范围内任意位置再跳一步能到达的最远下标
- 当 i == cur_end：已经走到当前步的极限，必须再跳一次，把 cur_end 扩展到 next_end
- 遍历到 len(nums) - 2 即可：最后一个位置不需要再跳

## 教训
- 看到"最少跳跃次数" → 贪心法，不要想 DP（O(n²) 时间复杂度高）
- 形象理解：在 cur_end 范围内你可以免费走动，但一旦走到边界就必须花一步"买票"跳到 next_end
- 和 55 题对比：55 是判断能否到达（维护 reach），45 是求最少步数（维护 cur_end + next_end）

## 跳跃游戏系列对比
| 题目             | 目标         | 方法       | 核心变量                              |
| :------------- | :--------- | :------- | :-------------------------------- |
| 55 跳跃游戏        | 能否到达终点     | 贪心       | `reach = max(reach, i + nums[i])` |
| **45 跳跃游戏 II** | **最少跳跃次数** | **贪心造桥** | **`cur_end` + `next_end`**        |
