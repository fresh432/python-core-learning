# LeetCode 209 长度最小的子数组

## 我的思路
第一反应：滑动窗口（双指针）
问题：边界处理混乱，变量命名 a/b 不清晰，调试30分钟

## 标准写法
```python
def minSubArrayLen(target, nums):
    left = 0
    total = 0
    result = float('inf')
    
    for right in range(len(nums)):
        total += nums[right]
        
        while total >= target:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
    
    return 0 if result == float('inf') else result
```
## 关键教训
- 变量命名：left/right 比 a/b 清晰
- 窗口扩展：right 前进，加元素
- 窗口收缩：满足条件时 left 前进，减元素
- 结果更新：在收缩时更新最小长度