# LeetCode 179 最大数

## 我的思路（30分钟）
- 前20分钟：没有任何头绪
- 看答案：把数组中的数字分别正向拼接、反向拼接再比较——正拼 < 反拼则交换两数位置；全部比较后拼接整个数组，首元素为 0 则返回 "0"
- 花10分钟理解传递性：设 x、y、z 分别有 a、b、c 位，xy < yx 即 x·(10^b) + y < y·(10^a) + x，推出 x/(10^a - 1) < y/(10^b - 1)；同理 yz < zy 得 y/(10^b - 1) < z/(10^c - 1)，串起来得 x/(10^a - 1) < z/(10^c - 1)，反推 xz < zx——比较可传递，所以"正拼小则交换"不影响全局最大，按理解写了一遍，通过

## 代码
```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])
        # 自定义比较：x+y < y+x 则交换
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        ans = "".join(nums)
        if ans[0] == "0":
            return "0"
        return ans
```

## 关键
- 核心比较器：x + y 与 y + x 比较（字典序拼接比较）
- 传递性依据：x/(10^a - 1) 的值构成全序，xy < yx ⇔ x/(10^a-1) < y/(10^b-1)，故排序合法
- 特判：结果首字符为 "0" 说明全零，返回 "0"

## 教训
- 看到"拼接最大/最小数" → 自定义排序 x+y vs y+x

