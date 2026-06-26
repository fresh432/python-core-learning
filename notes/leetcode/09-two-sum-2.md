# LeetCode 167 两数之和 II

## 我的思路（25分钟）
1. 快慢指针双层遍历 → 超时
2. 左右指针，但"遍历一圈再缩减" → 还是 O(n²)
3. 看解析：每次比较后立即缩减 → O(n)

## 核心洞察
数组有序，左右指针：
- 和 < target → 需要更大 → i += 1
- 和 > target → 需要更小 → j -= 1

## 代码
```python
def twoSum(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s == target:
            return [i + 1, j + 1]
        elif s < target:
            i += 1
        else:
            j -= 1
```
## 教训
- 有序数组 + 找两个数 → 左右指针
- "立即缩减"不是"遍历后再缩减"
