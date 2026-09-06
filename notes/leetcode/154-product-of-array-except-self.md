# LeetCode 238 除自身以外数组的乘积

## 我的思路（40分钟）
- 前10分钟：看到题目提示"前缀积和后缀积的乘积不超过32位整数"，立刻想到思路——正向遍历存前缀积，反向遍历乘后缀积
- 后30分钟：实现过程中纠结是否需要额外数组分别保存前缀积和后缀积，最后确定可以直接用输出数组 ans 存前缀积，再用一个变量 b_sum 维护后缀积，反向遍历时直接乘到 ans 对应位置

## 代码
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        f_sum = 1
        b_sum = 1
        
        # 正向：ans[i] 保存 nums[0] 到 nums[i] 的前缀积
        for i in range(n):
            f_sum *= nums[i]
            ans.append(f_sum)
        
        # 反向：用 b_sum 维护后缀积，直接乘到 ans 上
        for i in range(n - 1, -1, -1):
            if i == 0:
                ans[0] = b_sum
                return ans
            elif i == n - 1:
                ans[n - 1] = ans[n - 2]
            else:
                ans[i] = ans[i - 1] * b_sum
            b_sum *= nums[i]
        
        return ans
```

## 关键
- 前缀积：ans[i] 先保存 nums[0] * ... * nums[i]
- 后缀积：b_sum 维护 nums[i+1] * ... * nums[n-1]
- 最终结果：ans[i] = 前缀积[i-1] * 后缀积[i+1]
- 边界处理：i == 0 时没有前缀，ans[0] = b_sum；i == n-1 时没有后缀，ans[n-1] = ans[n-2]

## 教训
- 看到"除自身外所有元素的乘积" → 前缀积 + 后缀积，两次遍历
- 不需要额外数组：输出数组存前缀积，一个变量维护后缀积，空间 O(1)（不算输出数组）
- 注意边界：ans[0] 和 ans[n-1] 只有单侧乘积
- 和 560 题对比：560 是前缀和+哈希表（求子数组和为k），238 是前缀积+后缀积（求除自身外乘积）