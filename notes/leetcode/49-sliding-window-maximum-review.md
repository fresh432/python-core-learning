# LeetCode 239 滑动窗口最大值（复习）

## 我的思路（28分钟）
- 单调队列存窗口内单调递减的值：新元素大于队尾则一直弹出队尾，直到队空或队尾大于当前元素
- 从头到尾遍历，每遍历完一个元素将队首加入 ans；当窗口移动后"左边界要丢失的元素"是队首元素时弹出队首
- 因为从头到尾遍历，返回 ans 时要截去窗口未成型的前 k-1 个元素（返回 ans[k-1:]）才能通过

## 代码
```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        ans = []
        for i in range(n):
            while queue and queue[-1] < nums[i]:   # 维护递减
                queue.pop()
            queue.append(nums[i])
            if i >= k and queue[0] == nums[i - k]: # 左边界元素离开
                queue.popleft()
            ans.append(queue[0])
        return ans[k - 1:]                          # 截掉窗口未成型部分
```

## 教训
- 复习： 28 分钟，"弹队尾 + 弹队首 + 截前缀"三步都记得，但组合时仍绕了一阵，说明 239 的题型还不熟练