# LeetCode 46 全排列

## 我的思路（30分钟）
1. 前15分钟：想到用交换，但想的是列表两边交换再截断，太复杂
2. 后15分钟：看答案理解——固定位置交换：x 是当前要填的位置，i 从 x 到末尾选一个数交换到 x 位置，然后递归填下一个位置

## 代码
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def func(x):
            if x == n - 1:          # 填到最后一个位置，得到一个排列
                ans.append(nums[:])
                return
            
            for i in range(x, n):
                nums[i], nums[x] = nums[x], nums[i]  # 把 nums[i] 换到位置 x
                func(x + 1)                           # 填下一个位置
                nums[i], nums[x] = nums[x], nums[i]  # 回溯，恢复原状
        
        func(0)
        return ans
```

## 关键
- 固定位置法：x 是当前要确定的位置，i 从 x 到 n-1 选一个数放过来
- 交换而非选择：直接在原数组上交换，不需要额外的 path 或 used 数组
- 回溯恢复：交换后递归，递归完再交换回来
- 终止条件：x == n - 1，最后一个位置已经确定

## 教训
- 排列问题有两种回溯思路：

| 方法          | 特点         | 代码                                    |
| ----------- | ---------- | ------------------------------------- |
| **交换法（本题）** | 原地交换，无额外空间 | `nums[i], nums[x] = nums[x], nums[i]` |
| used 数组法    | 标记已用元素     | `used[i] = True/False`                |

- 交换法更简洁，但 used 数组法在有重复元素时更容易处理去重
- 看到"全排列" → 先想交换法，有重复元素再考虑 used 数组 + 去重




