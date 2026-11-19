# LeetCode 1004 最大连续 1 的个数 III（复习）

## 我的思路（5分钟）
- 前3分钟：队列版滑动窗口，队列存 0 的下标，0 的数量超过 k 个时弹出队首，用当前下标减弹出下标更新窗口大小和答案
- 后2分钟：双指针版，遇 0 计数加一，超过 k 则收缩左边界指针（越过最左的 0），按左右指针位置更新答案

## 代码（队列版）
```python
from collections import deque

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        old_zero = -1
        ans = 0
        queue = deque()
        for i, num in enumerate(nums):
            if num == 0:
                queue.append(i)
            if len(queue) > k:
                old_zero = queue.popleft()
            ans = max(ans, i - old_zero)
        return ans
```

## 代码（双指针版）
```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        ans = 0
        cnt = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1
            if cnt > k:
                while nums[left] == 1:
                    left += 1
                left += 1      # 越过那个 0
                cnt -= 1
            ans = max(ans, right - left + 1)
        return ans
```

## 教训
- 复习： 5 分钟双解法一遍过（55 → 5），该题型暂已掌握
- 队列版有个细节：old_zero 初始 -1，k 未超额度时窗口就是"从头到当前"，统一了初始情况