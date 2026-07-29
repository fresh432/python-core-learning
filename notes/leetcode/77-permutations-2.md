# LeetCode 47 全排列 II

## 我的思路（30分钟）
- 前5分钟：写出交换法框架，和 46 题一致
- 中间15分钟：去重调试失败——想用相邻重复跳过，但有问题
- 后10分钟：看答案理解——每层用一个集合记录已用过的数字，同一层相同的数字只交换一次

## 代码
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def func(x):
            if x == n - 1:
                ans.append(nums[:])
                return
            
            dic = set()                 # ← 每层一个集合，记录本层已用过的数字
            for i in range(x, n):
                if nums[i] in dic:      # 本层已用过，跳过
                    continue
                dic.add(nums[i])
                nums[i], nums[x] = nums[x], nums[i]
                func(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
        
        func(0)
        return ans
```

## 关键
- 层内去重：dic = set() 在递归函数内部创建，每层独立
- 同一层中，相同的数字只交换一次，避免产生重复排列
- nums[i] in dic 判断的是"本层是否已经用过这个数"，不是全局去重

## 和 46 题的对比
| 题目            | 元素是否重复   | 去重方法           |
| ------------- | -------- | -------------- |
| 46 全排列        | 不重复      | 无需去重           |
| **47 全排列 II** | **可能重复** | **每层用 set 去重** |

## 教训
- 排列去重 vs 组合去重：

| 类型       | 去重条件                                 | 代表题目          |
| -------- | ------------------------------------ | ------------- |
| 组合去重     | `i > start and nums[i] == nums[i-1]` | 40 组合总和 II    |
| **排列去重** | **每层用 set**                          | **47 全排列 II** |

- 组合是"选或不选"，排列是"交换位置"，去重机制不同
- 排列的交换法去重：每层维护一个 set，记录本层已经交换过的数字值
