# LeetCode 128 最长连续序列

## 我的思路（60分钟）
- 前20分钟：想用并查集来写，但想不出如何维护最大长度的思路，卡住
- 中间15分钟：看提示，改用哈希表 + 剪枝——先将数组转 set，遍历每个数字时，只从"连续序列起点"（即 num-1 不在 set 中）开始向右扩展，这样每个数字最多被访问一次，O(n)
- 中间10分钟：看了动态规划法——哈希表存每个数字所在连续序列的长度，遍历数字时获取其左边界和右边界的连续长度，更新当前序列长度，并同步更新边界节点的长度值。时间比纯哈希慢（111ms vs 44ms）
- 后5分钟：实现 DP 版本
- 最后10分钟：想尝试并查集写法，看了20分钟答案还是没看懂思路

## 代码（哈希表 + 剪枝）
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        ans = 0
        
        for num in hash_map:
            if num - 1 not in hash_map:
                count = 1
                current_num = num
                while current_num + 1 in hash_map:
                    count += 1
                    current_num += 1
                ans = max(ans, count)
                if ans >= len(hash_map) / 2:
                    return ans
        
        return ans
```

## 代码（动态规划法）
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        ans = 0
        
        for num in nums:
            if num not in hash_map:
                left = hash_map.get(num - 1, 0)
                right = hash_map.get(num + 1, 0)
                current_len = left + right + 1
                ans = max(ans, current_len)
                hash_map[num] = current_len
                hash_map[num - left] = current_len
                hash_map[num + right] = current_len
        
        return ans
```

## 关键
- 哈希表 + 剪枝：只从连续序列的起点开始扩展（num-1 not in set），避免重复计算
- 剪枝优化：ans >= len(hash_map) / 2 时提前返回（最长序列不可能超过一半以上）
- DP 法：hash_map[num] 存以 num 为边界的连续序列长度，更新时同步更新两端边界
- 并查集：理论上可行，但维护最大长度较复杂，暂时未掌握

## 教训
- 看到"最长连续序列，要求 O(n)" → 哈希表 + 只从起点扩展，不要排序（O(n log n)）
- 剪枝技巧：当前最优解已经超过剩余元素一半时，可以直接返回
- DP 法虽然也是 O(n)，但常数较大（111ms vs 44ms）