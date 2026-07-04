# LeetCode 18 四数之和

## 思路（50分钟，自己写出）
排序 + 固定i,j + 双指针a,b。

## 代码
```python
def fourSum(nums, target):
    nums.sort()
    ans = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]: continue
        
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            
            a, b = j + 1, len(nums) - 1
            while a < b:
                total = nums[i] + nums[j] + nums[a] + nums[b]
                if total == target:
                    ans.append([...])
                    a += 1; b -= 1
                    # 去重
                elif total > target: b -= 1
                else: a += 1
    return ans
```

## 关键
- 三数之和外面再套一层循环
- 去重4处：i、j、a、b
- 调试容易绕晕，注意变量名

## 教训
- 想优化成双重循环失败，回归三循环
- 不要过度优化，先写出能跑的