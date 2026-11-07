# LeetCode 229 多数元素 II

## 我的思路（45分钟）
- 前13分钟：想不出线性时间 O(1) 空间的解法，先用哈希计数写了一遍：边计数边判断是否超过 n//3 次，超过则加入 ans 并把哈希值改为 -1，遇到 -1 直接跳过，调试通过
- 补了6分钟摩尔投票法思路后，花16分钟尝试：由"满足次数 > n//3 的数最多 2 个"，想做两次摩尔投票、第二次排除第一次投出的值，每次投完再扫圈计数验证——但这样最多的两个数可能在前段相互抵消，让后面次数不足的数捡漏，此路不通
- 花10分钟看答案：一次性选两个候选人——遍历元素与某候选人相同则其票加一；与两个都不匹配则两候选人票都减一；某候选人票数为 0 时换为当前数字、票重置为 1。最后再遍历计数，两个候选人都满足 > n//3 才加入 ans。计数时匹配用 if-elif（而非两个 if）防止两候选人相同时重复计数，按这个方法写了一遍

## 代码（哈希版）
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = n // 3
        ans = []
        count = defaultdict(int)
        for num in nums:
            if count[num] == -1:   # 已入选，跳过
                continue
            count[num] += 1
            if count[num] > k:
                ans.append(num)
                count[num] = -1
        return ans
```

## 代码（摩尔投票版）
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        a, b = -1, -1
        v_1, v_2 = 0, 0
        for num in nums:
            if num == a:
                v_1 += 1
            elif num == b:
                v_2 += 1
            elif v_1 == 0:      # a 出缺，换人
                a = num
                v_1 += 1
            elif v_2 == 0:      # b 出缺，换人
                b = num
                v_2 += 1
            else:               # 与两个候选人都不同，同归于尽
                v_1 -= 1
                v_2 -= 1

        c_1, c_2 = 0, 0
        for num in nums:        # 二次验证（候选人未必达标）
            if num == a:
                c_1 += 1
            elif num == b:
                c_2 += 1

        if c_1 > (n // 3):
            ans.append(a)
        if c_2 > (n // 3):
            ans.append(b)
        return ans
```

## 关键
- 核心定理：出现次数 > n/k 的数最多 k-1 个 → 本题维护 2 个候选人
- 双候选人投票规则：匹配谁谁的票加一；都不匹配则双双减一；谁票数为 0 谁让位给当前数字
- 最后必须二次计数验证——候选人是"幸存者"不是"达标者"
- 计数匹配用 if-elif：防止 a、b 相同时对同一数字计两次

## 教训
- 看到"求出现次数 > n/k 的元素" → 摩尔投票维护 k-1 个候选人 + 二次验证
- 和 169 题对比：169 是 > n/2（1 个候选人，数学保证存在无需验证），229 是 > n//3（2 个候选人，必须验证）
- 自己"两次投票排除第一次结果"的想法有致命缺陷：两个真众数在相互抵消阶段会同归于尽——正确做法是同一轮里两个候选人同步增减，任何第三方数字都同时抵消两者，真众数合力撑到最后
