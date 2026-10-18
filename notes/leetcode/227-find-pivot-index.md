# LeetCode 724 寻找数组的中心下标

## 我的思路（10分钟）
- 先用 total 保存数组总和
- 初始化前缀和 prev 和后缀和 tail（tail = total - nums[0]）
- 遍历数组，比较 prev 和 tail 是否相等，相等则返回当前下标
- 不等则更新：prev += nums[i]，tail -= nums[i+1]
- 在数组尾部额外添加一个0元素，避免边界判断

## 代码
```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        nums = nums + [0]
        prev = 0
        tail = total - nums[0]
        for i in range(n):
            if prev == tail:
                return i
            else:
                prev += nums[i]
                tail -= nums[i + 1]
        return -1
```

## 关键
- 前缀和：prev 累加当前元素之前的所有元素
- 后缀和：tail 减去当前元素及之前的所有元素
- 边界处理：数组末尾加0，避免 i+1 越界

## 教训
- 看到"找中心下标/左右和相等" → 前缀和，或数学法 2 * prev + nums[i] == total
- 和 560 题对比：560 是前缀和+哈希表（子数组和为k），724 是找中心下标（前缀和等于后缀和）
