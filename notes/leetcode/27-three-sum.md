# LeetCode 15 三数之和

## 思路（30分钟卡住，看答案）
排序 + 固定i + 双指针j,k向中间收敛。

## 代码
```python
def threeSum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        if nums[i] &gt; 0: break  # 剪枝
        if i &gt; 0 and nums[i] == nums[i-1]: continue  # 去重
        
        j, k = i + 1, len(nums) - 1
        while j &lt; k:
            total = nums[i] + nums[j] + nums[k]
            if total &lt; 0: j += 1
            elif total &gt; 0: k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1; k -= 1
                while j &lt; k and nums[j] == nums[j-1]: j += 1
                while j &lt; k and nums[k] == nums[k+1]: k -= 1
    return ans
```

## 关键
- 排序是前提，否则无法去重和剪枝
- 剪枝：nums[i] > 0 时break
- 去重：i、j、k都要跳过重复

## 教训
- 30分钟没想到排序，惯性思维
- 看答案后理解，下次先想排序
