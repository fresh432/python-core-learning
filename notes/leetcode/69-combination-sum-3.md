# LeetCode 216 组合总和 III

## 我的思路（50分钟）
1. 前10分钟：想到用 77 题的回溯 + 剪枝方法
2. 后40分钟：卡在剪枝条件处理——需要同时考虑个数限制（k 个）和和的限制（n），调试了很久

## 代码
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        
        def func(i, n):
            d = k - len(path)       # 还需选 d 个
            # 最大可能和：从 i 往下选 d 个最大的数
            max_sum = d * (2 * i - d + 1) // 2
            
            # 剪枝：剩余和不够或为负，或最大可能和不够
            if n < 0 or n > max_sum:
                return
            
            if d == 0 and n == 0:   # 选够 k 个且和正好为 n
                ans.append(path[:])
                return
            
            if i > d:
                func(i - 1, n)      # 不选 i
            
            path.append(i)
            func(i - 1, n - i)      # 选 i，目标和减去 i
            path.pop()
        
        func(9, n)
        return ans
```

## 关键
- 双重约束：既要选够 k 个数，又要和为 n
- 剪枝条件：
  - n < 0：当前和已经超过目标
  - n > max_sum：即使选最大的 d 个数，和也不够
  - max_sum = d*(2*i-d+1)//2：等差数列求和，从 i 往下连续 d 个数的和
- 数字范围固定 1-9，从 9 开始倒序选

## 教训
- 组合问题的剪枝要同时考虑个数和和两个维度
- max_sum 的计算是等差数列求和：从 i 开始连续 d 个数 i + (i-1) + ... + (i-d+1)
- 和 77 题对比：

| 题目               | 约束条件             | 剪枝维度       |
| ---------------- | ---------------- | ---------- |
| 77 组合            | 选 k 个            | 个数         |
| **216 组合总和 III** | **选 k 个 + 和为 n** | **个数 + 和** |

- 回溯 + 剪枝是组合问题的标准解法，剪枝条件越严格效率越高