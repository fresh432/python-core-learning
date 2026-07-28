# LeetCode 78 子集

## 我的思路（18分钟）
1. 前8分钟：想到用倒序遍历的方式——从后往前，每个元素选或不选
2. 后10分钟：写出来调试通过，莫名其妙就写对了

## 代码
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        
        def func(ans, path, start):
            if start == -1:             # 遍历完所有元素
                ans.append(path[:])
                return
            
            # 不选当前元素
            func(ans, path, start-1)
            
            # 选当前元素
            path.append(nums[start])
            func(ans, path, start-1)
            path.pop()
        
        start = len(nums) - 1
        func(ans, path, start)
        return ans
```

## 关键
- 每个元素选或不选：倒序遍历，对每个元素做两个分支（选/不选）
- 终止条件：start == -1，所有元素处理完毕
- 子集问题 = 所有可能的组合，包括空集

## 更标准的写法（正序，和 77 题一致）
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        
        def func(start):
            ans.append(path[:])         # 每个节点都是一组解
            for i in range(start, len(nums)):
                path.append(nums[i])
                func(i + 1)
                path.pop()
        
        func(0)
        return ans
```

## 教训
- 子集问题的两种回溯思路：

| 思路         | 特点    | 代码风格                  |
| ---------- | ----- | --------------------- |
| 选/不选（我的写法） | 二叉树递归 | 倒序，两个分支               |
| 枚举起点（标准写法） | 组合扩展  | 正序，`ans.append` 在每个节点 |

- 标准写法更通用，和 77 题（组合）完全一致，只是不限制 len(path) == k
- 看到"求所有子集" → 回溯，每个节点都收集答案（不只是叶子节点）
