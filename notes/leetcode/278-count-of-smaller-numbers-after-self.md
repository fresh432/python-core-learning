# LeetCode 315 计算右侧小于当前元素的个数

## 我的思路（60分钟）
- 前10分钟：以为是单调栈写法，发现处理不了，因为不能保证单调
- 想到之前用过的树状数组倒序遍历存值取值，但这里有负数，想开两个数组分别存正数和负数的前缀和
- 花40分钟尝试：正负分开处理实在太麻烦，下标经常打架，写得太复杂
- 看答案10分钟：震惊瘫坐，原来可以先将数组离散化：把所有数字排序、去重、打排名，后续更新和查找只用排名进行。这样既处理了负数问题，又处理了数字差距过大导致的空间浪费；而且中间操作只关心大小关系，转排名不影响结果
- 整体思路：排序去重后用字典存排名；倒序遍历，先 query(rank - 1) 得右侧小于当前数的个数，再将该排名 add 进树状数组；ans 反转后返回

## 代码
```python
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def add(i):
            while i < len(tree):
                tree[i] += 1
                i += i & -i

        def query(i):
            cnt = 0
            while i > 0:
                cnt += tree[i]
                i -= i & -i
            return cnt

        n = len(nums)
        uniques = sorted(set(nums))                    # 离散化
        rank_map = {v: i + 1 for i, v in enumerate(uniques)}

        tree = [0] * (len(rank_map) + 1)
        ans = []
        for i in range(n - 1, -1, -1):                 # 倒序遍历
            rank = rank_map[nums[i]]
            ans.append(query(rank - 1))                # 右侧比它小的个数
            add(rank)
        return ans[::-1]
```

## 关键
- 离散化（坐标压缩）：排序去重 → 打排名，一举解决负数、大值域两个障碍
- 倒序遍历 + 树状数组：query(rank-1) 统计"已入树（即在右侧）且值域小于当前"的元素个数，add(rank) 记录当前元素
- 与 307 的 BIT 板子完全复用，只加一层离散化

## 教训
- 看到"统计右侧小于/大于当前元素的个数" → 离散化 + 树状数组（或归并排序）；单调栈处理不了不单调的序列
- 离散化是处理"负数 + 值域过大"的标准前置步骤，不要想"开两个数组分开存"这种土办法