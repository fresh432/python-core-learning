# LeetCode 40 组合总和 II

## 我的思路（30分钟）
- 前10分钟：写出大致框架，和 39 题类似
- 中间10分钟：去重部分调试失败——以为 i > 0 and cand[i] == cand[i-1] 就能跳过，结果跳过了正确的组合
- 后10分钟：看答案理解——去重条件要加 i > start，只跳过同一层的相同元素，不跳过不同层的

## 代码
```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        def func(path, ans, cand, target, start):
            if target == 0:
                ans.append(path[:])
                return
            
            for i in range(start, len(cand)):
                if target - cand[i] < 0:
                    break
                # 去重关键：i > start，只跳过同一层的重复元素
                if i > start and cand[i] == cand[i - 1]:
                    continue
                path.append(cand[i])
                func(path, ans, cand, target - cand[i], i + 1)  # i+1，每个数只能用一次
                path.pop()
        
        candidates.sort()
        start = 0
        func(path, ans, candidates, target, start)
        return ans
```

## 关键
- 每个数只能用一次：递归传 i + 1
- 去重条件：i > start and cand[i] == cand[i-1]
  - i > start：只在同一层跳过重复，不同层（递归 deeper）允许重复
  - 如果写成 i > 0，会错误地跳过不同层的合法组合
- 先排序，让相同元素相邻，才能用相邻比较去重

## 教训
- 去重的核心：i > start vs i > 0 的区别：
  - i > 0：全局去重，会漏掉合法组合（如 [1,1,6] 中第二个 1 被跳过）
  - i > start：层内去重，只跳过同一 for 循环中的重复，递归 deeper 时允许
- 和 39 题对比：

| 题目             | 重复选取    | 去重              | start 传值    |
| -------------- | ------- | --------------- | ----------- |
| 39 组合总和        | **允许**  | 无需              | `i`         |
| **40 组合总和 II** | **不允许** | **`i > start`** | **`i + 1`** |
