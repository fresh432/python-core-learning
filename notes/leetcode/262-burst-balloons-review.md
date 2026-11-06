# LeetCode 312 戳气球（复习）

## 我的思路（29分钟）
- 前10分钟：想出大致思路,先给数组添加头尾元素 1，用新数组长度初始化 dp；从小到大循环遍历区间，每个区间的值由该区间内最后一个戳破的气球 k 分界：dp[l][r] = max(dp[l][k] + dp[k][r] + nums[l]·nums[k]·nums[r], dp[l][r])。第一层循环遍历区间大小，第二层循环遍历该大小区间的左边界，右边界由左边界加区间大小得出
- 卡住19分钟：觉得枚举区间内最后戳破的气球要套三层循环，感觉不对会超时，又想不到别的做法；还是看了眼之前提交的代码，发现确实是三层循环枚举 k，加上后通过

## 代码
```python
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(3, n + 1):          # 第一层：区间长度
            for l in range(0, n - i + 1):  # 第二层：左边界
                r = l + i - 1
                for k in range(l + 1, r):  # 第三层：最后戳破的 k
                    dp[l][r] = max(dp[l][r],
                                   dp[l][k] + dp[k][r] + nums[l] * nums[k] * nums[r])
        return dp[0][n - 1]
```

## 教训
- 复习时状态定义、遍历顺序都记得，卡在"三层循环会不会超时"的自我怀疑上，区间 DP 的标准形态就是三层循环（区间长度 × 左端点 × 分界点），O(n³) 对 n ≤ 500 完全可行
- 对复杂度的直觉要校准：看到三层循环先算量级再决定是否否决，不要凭感觉砍正确解法