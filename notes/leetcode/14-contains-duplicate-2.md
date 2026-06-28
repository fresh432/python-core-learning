# LeetCode 219 存在重复元素 II

## 思路
哈希表存最近索引，检查距离是否 <= k。

## 代码
```python
 def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for index, i in enumerate(nums):
            if i in h:
                if index - h[i] <= k:
                    return True
            h[i] = index
        return False  
```

## 注意
- 滑动窗口 O(n*k) 不如哈希表 O(n)
- 只存最近位置，自然满足距离限制