# LeetCode 55 跳跃游戏

## 我的思路（35分钟）
- 前10分钟：理解题意，从评论获取灵感——把数组值看作行动点，每走一步消耗1点，若当前格子的数值比剩余行动点多，就补充到当前数值
- 中间10分钟：确定用一个变量 act 维护剩余行动力即可，不需要 DP，空间复杂度 O(1)
- 后10分钟：调试写出通过
- 最后5分钟：看了维护最远到达距离的写法，更简洁，自己写了一遍

## 代码（行动力模拟法）
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        act = 0
        for i, num in enumerate(nums):
            if act < num:
                act = num
            act -= 1
            if act < 0:
                break
        return True if i == len(nums) - 1 else False
```

## 代码（维护最远距离法）
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True
```

## 关键
- 行动力法：act 维护当前剩余可跳跃步数，每步减1，遇到更大的值就补充
- 最远距离法：reach 维护当前能到达的最远下标，若遍历下标 i > reach 说明 unreachable
- 两者都是贪心，时间 O(n)，空间 O(1)

## 教训
- 看到"能否跳到末尾" → 贪心维护最远距离，若 i > reach 则返回 False
- 最远距离法比行动力模拟更直观，代码也更短
- 不要一上来就想 DP，贪心能解决的优先贪心

