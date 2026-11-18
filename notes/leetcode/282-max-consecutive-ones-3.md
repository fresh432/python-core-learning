# LeetCode 1004 最大连续 1 的个数 III

## 我的思路（55分钟）
- 看一眼题目就想到滑动窗口，花25分钟尝试：右边界统计 0 的 cnt 大于 k 时收缩左边界。卡在 k == 0 的情况，花了10分钟想是不是边界有问题，实在没找出来，花5分钟重写了个"遍历统计最多连续 1"处理特殊情况
- 通过后突然发现用双向队列更容易：队列存每个 0 的下标，队列中 0 的数量大于 k 时弹出左端 0 的下标，用当前下标减该下标得到窗口大小并更新 ans。花5分钟试了下，真的通过了
- 再回头看，双指针也能按队列思路优化：遇 0 计数，cnt 超过 k 后左指针向前移动直到越过一个 0，cnt 减一，更新 ans。又花10分钟重写，通过

## 代码（双指针优化版）
```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = ans = 0
        cnt = 0
        for right, num in enumerate(nums):
            if num == 0:
                cnt += 1
            if cnt > k:                       # 0 超额度，左边界越过最左的 0
                while nums[left] == 1:
                    left += 1
                left += 1
                cnt -= 1
            ans = max(ans, right - left + 1)
        return ans
```

## 代码（队列法）
```python
from collections import deque

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        queue = deque()      # 存窗口内 0 的下标
        left = ans = 0
        for right, num in enumerate(nums):
            if num == 0:
                queue.append(right)
                if len(queue) > k:
                    left = queue.popleft() + 1
            ans = max(ans, right - left + 1)
        return ans
```

## 关键
- 窗口约束：窗口内 0 的个数 ≤ k；两种维护方式等价——
  - 队列：存 0 的下标，超额度时 left = popleft() + 1 直接定位新左边界
  - 双指针：cnt 计数，超额度时左指针越过最左 0（跳过所有 1，再跳一个 0）
- 窗口大小即"翻转后全 1 的长度"，每个 right 处更新 ans

## 教训
- 看到"最多翻转 k 个 0 的最长连续 1" → 滑动窗口（cnt 记 0 个数）或队列存 0 下标
- 初版卡在 k==0 说明框架本身脆：通用框架应天然覆盖 k=0。需要特判的写法往往意味着状态定义不干净
- 队列法与双指针同义：popleft() + 1 就是"左指针越过最左 0 后一位"，一个模型两种写法，选顺手的