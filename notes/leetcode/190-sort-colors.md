# LeetCode 75 颜色分类

## 我的思路（20分钟）
- 前5分钟：因为之前做过 86 题（分隔链表），想是否可以用三个数组拆分，但题目要求原地修改
- 中间10分钟：写出荷兰国旗问题解法——维护左右两个指针 left 和 right，i 遍历数组：
  - nums[i] == 0：与 left 交换，left += 1
  - nums[i] == 2：与 right 交换，right -= 1
  - nums[i] == 1：i 继续走
  - 交换后需要循环判断新换过来的元素，直到 nums[i] == 1 或边界追上
- 后5分钟：写了单循环版本——用 while i <= right，遇到 0 交换后 i += 1，遇到 2 交换后 i 不动（因为换过来的元素未知），遇到 1 直接 i += 1

## 代码（双指针 + 循环判断）
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0, n - 1
        for i in range(n):
            if i > right:
                break
            while nums[i] != 1 and i >= left and i <= right:
                if nums[i] == 0:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
                elif nums[i] == 2:
                    nums[right], nums[i] = nums[i], nums[right]
                    right -= 1
```

## 代码（单循环版）
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0, n - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                # i 不动，因为换过来的元素需要重新判断
            else:
                i += 1
```

## 关键
- 荷兰国旗问题：三个区域（0在左，1在中，2在右）
- left：0 区域的右边界，right：2 区域的左边界
- 遇到 2 与 right 交换后 i 不动：因为换过来的元素可能是 0 或 1，需要重新判断
- 遇到 0 与 left 交换后 i += 1：因为 left 位置及之前都是 0，换过来的只可能是 1

## 教训
- 看到"原地排序三种颜色/三个类别" → 荷兰国旗问题，双指针 + 单遍历
- 和 86 题对比：86 是链表按值分区（拆成两个链表），75 是数组原地三色分类（双指针交换）
- 单循环版比 for + while 嵌套更简洁
