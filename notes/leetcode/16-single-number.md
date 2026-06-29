# LeetCode 136 只出现一次的数字

## 我的思路（3分钟）
第一反应：哈希表，存一个删一个，最后剩的就是答案。

## 代码（哈希表）
```python
def singleNumber(self, nums: List[int]) -> int:
    h = set()
    for i in nums:
        if i not in h :
            h.add(i)
        else:
            h.remove(i)
    ans = h.pop()
    return ans
```

## 更优解：异或位运算
```python
def singleNumber(nums):
    ans = 0
    for i in nums:
        ans ^= i
    return ans
```

## 异或性质
- a ^ a = 0（相同为0）
- a ^ 0 = a（与0不变）
- 交换律、结合律

## 关键教训
- 看到"出现两次/一次"，先想异或，再想哈希表
- 位运算空间 O(1)，是面试更优解
- 库函数要熟：set、位运算的基本操作