# LeetCode 217 存在重复元素

## 思路（1分钟）
第一反应：set 去重，比较长度。

## 代码
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    h = {}
    for i in nums:
        if i in h:
            return True
        h[i] = 0
    return False
```

## 关键
- set 天然去重，比较长度是最简洁写法
- 遍历写法可以提前返回，某些输入更快
- 已形成条件反射：看到"重复"想到 set