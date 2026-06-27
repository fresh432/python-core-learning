# LeetCode 1 两数之和

## 思路
哈希表：遍历数组，找 target - num 是否在表中。

## 代码
```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index, num in enumerate(nums):
            n = target - num
            if n in h:
                return [h[n], index]
            h[num] = index
        return []
```

## 关键
- 哈希表把时间从 O(n²) 降到 O(n)
- 空间换时间
- 一次遍历，边查边存