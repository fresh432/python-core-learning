# LeetCode 881 救生艇（复习）

## 我的思路（2分钟）
- 先将数组排序，双指针指向数组头尾
- 遍历：最重的 + 最轻的 ≤ limit 则将轻指针前进，否则只前进重指针，然后计数 +1，最重的肯定要占用一艘船，只需判断能否安插一个最轻的
- 之所以不选"最合适的"：最合适的和最轻的人选哪个都不影响，最合适的可以配最重及其以下的所有人，最重已匹配出去后剩下都能正常匹配，所以选最轻的既不影响后续组合数量，代码又简单

## 代码
```python
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        ans = 0
        i, j = 0, len(people) - 1
        people.sort()
        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            j -= 1
            ans += 1
        return ans
```

## 教训
- 复习： 2 分钟一遍过（37 → 2 分钟）
- 首次做时的弯路（没读到"最多两人"）这次已避免