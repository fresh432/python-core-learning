# LeetCode 16 最接近的三数之和

## 我的思路（60分钟）
- 前35分钟：排序后固定一个数，双指针向中间逼近，同时维护与 target 最接近的三数和
- 后20分钟：看剪枝优化——双指针逼近前，先计算当前层的最小值和最大值，若超出 target 的边界则直接跳过或提前结束，将中间 O(n²) 部分近似优化到 O(n)
- 后5分钟：写出优化版，7ms

## 代码（基础版）
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        
        for i in range(n):
            left, right = 0, n - 1
            while left < right and right != i and left != i:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                elif current_sum == target:
                    return current_sum
                ans = current_sum if abs(current_sum - target) < abs(ans - target) else ans
        
        return ans
```

## 代码（剪枝优化版）
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                # 剪枝1：当前最小和都大于target，后续只会更大
                min_sum = nums[left] + nums[left + 1] + nums[i]
                if target < min_sum:
                    if abs(min_sum - target) < abs(ans - target):
                        ans = min_sum
                    break
                
                # 剪枝2：当前最大和都小于target，后续只会更小
                max_sum = nums[right] + nums[right - 1] + nums[i]
                if target > max_sum:
                    if abs(max_sum - target) < abs(ans - target):
                        ans = max_sum
                    break
                
                c_sum = nums[i] + nums[left] + nums[right]
                if c_sum > target:
                    right -= 1
                    while nums[right] == nums[right + 1]:
                        right -= 1
                elif c_sum < target:
                    left += 1
                    while nums[left] == nums[left - 1]:
                        left += 1
                elif c_sum == target:
                    return c_sum
                
                ans = c_sum if abs(c_sum - target) < abs(ans - target) else ans
        
        return ans
```

## 关键
- 排序 + 固定一个数 + 双指针：和 15 题三数之和类似
- 剪枝优化：
  - min_sum = nums[i] + nums[left] + nums[left+1]：若 target < min_sum，说明当前层最小都大于 target，后续只会更大，直接 break
  - max_sum = nums[i] + nums[right] + nums[right-1]：若 target > max_sum，说明当前层最大都小于 target，后续只会更小，直接 break
- 去重：移动指针时跳过重复元素
- 时间：剪枝后从 443ms 优化到 7ms

## 教训
- 看到"最接近的三数之和" → 排序 + 双指针 + 剪枝
- 剪枝的核心：利用排序后的单调性，计算当前层的理论最小/最大和，与 target 比较后提前终止
- 和 15 题对比：15 是找和为0的三元组（去重+收集所有解），16 是找最接近 target 的三数和（维护最优解+剪枝）

## 双指针系列对比
| 题目              | 目标            | 方法         | 核心技巧             |
| :-------------- | :------------ | :--------- | :--------------- |
| 15 三数之和         | 和为0的三元组       | 排序+双指针     | 去重，收集所有解         |
| **16 最接近的三数之和** | **最接近target** | **排序+双指针** | **剪枝（min/max和）** |
| 11 盛最多水的容器      | 最大面积          | 双指针向中间     | 移动短板             |
