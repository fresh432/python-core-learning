# LeetCode 448 找到所有数组中消失的数字

## 我的思路（20分钟）
- 前15分钟：想一遍遍历同时找缺失数字——遍历数组时交换元素到对应位置，若交换的两个数相同则退出并加入 ans。但有 bug：若需要的数字在数组末端但前面交换没映射到，会误添加。改为两遍遍历：第一遍归位，第二遍找 nums[i]-1 != i 的位置加入 ans，通过
- 后5分钟：看答案，发现标记法——遍历数组，将 nums[abs(num)-1] 标记为负数（表示该位置对应的数字出现过）。最后再遍历一遍，仍是正数的位置说明没有数字指向这里，即为缺失数字

## 代码（原地交换法）
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            while nums[i] - 1 != i:
                if nums[nums[i] - 1] == nums[i]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] - 1 != i:
                ans.append(i + 1)
        return ans
```

## 代码（标记法）
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
```

## 关键
- 原地交换：把数字 x 放到下标 x-1 处，第二遍找不匹配的
- 标记法：用负数标记"该位置对应的数字已出现"，正数表示缺失
- 注意取绝对值：abs(num)，因为可能已经被标记为负数

## 教训
- 看到"1~n中缺失的数字，要求原地" → 标记法（负数标记）或原地交换
- 和 268/41 题对比：268 是缺失一个数字（数学法/异或），41 是缺失第一个正数（原地哈希），448 是缺失多个数字（标记法）
