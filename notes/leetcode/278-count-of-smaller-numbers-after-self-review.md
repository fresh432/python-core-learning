# LeetCode 315 计算右侧小于当前元素的个数（复习）

## 我的思路（11分钟）
- 先把原数组离散化处理：把所有数字对应的排名存到哈希表中
- 倒序遍历原数组的值：先取当前元素对应的排名，再根据这个排名去树状数组里取前缀和（query(rank-1)），然后将当前元素的排名添加进树状数组
- 返回时把 ans 反转
- 离散化的作用：去重、消除正负数影响、消除值域过大和值域稀疏的影响

## 代码
```python
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        tree = [0] * (n + 1)

        def add(i):
            while i < n:
                tree[i] += 1
                i += i & -i

        def sum_pre(i):
            cnt = 0
            while i > 0:
                cnt += tree[i]
                i -= i & -i
            return cnt

        uniques = sorted(set(nums))
        rank_map = {v: i + 1 for i, v in enumerate(uniques)}

        for i in range(n - 1, -1, -1):
            rank = rank_map[nums[i]]
            ans.append(sum_pre(rank - 1))
            add(rank)
        return ans[::-1]
```

## 教训
- 复习： 11 分钟一遍过（60 → 11），离散化，树状数组基本概念已掌握
- 离散化四大作用：去重、消正负、压值域、治稀疏，下次遇到"值域大/有负数/稀疏"三个信号中的任意一个，先想离散化
