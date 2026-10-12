# LeetCode 680 验证回文串 II

## 我的思路（19分钟）
- 前14分钟：双指针从两端向中间匹配，遇到不匹配时初始化两个指针 delete_left 和 delete_right，分别表示删除左边或右边字符后的情况，用当前 left 和 right 分别遍历这两种情况。若至少一种通过则返回 True，都没通过返回 False。若全程无 mismatch 则返回 True。调试通过
- 后5分钟：看了辅助函数法——用 lambda 判断字符串是否等于其反转。当左右字符不匹配时，将去掉左边字符或去掉右边字符的剩余字符串传入辅助函数，两个结果取 or。代码更简洁可读性好

## 代码（双指针法）
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        flag1, flag2 = 0, 0
        
        while left < right:
            if s[left] != s[right]:
                delete_left = left + 1
                delete_right = right - 1
                
                while delete_left < right:
                    if s[delete_left] != s[right]:
                        flag1 = 1
                        break
                    delete_left += 1
                    right -= 1
                
                while left < delete_right:
                    if s[left] != s[delete_right]:
                        flag2 = 1
                        break
                    delete_right -= 1
                    left += 1
                
                if flag1 and flag2:
                    return False
                return True
            
            left += 1
            right -= 1
        
        return True
```

## 代码（辅助函数法）
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        isPalindrome = lambda x: x == x[::-1]
        
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s[left + 1: right + 1]) or isPalindrome(s[left: right])
            left += 1
            right -= 1
        
        return True
```

## 关键
- 双指针：遇到 mismatch 时分别尝试跳过左或右字符，继续匹配
- 辅助函数：用字符串反转判断是否为回文，代码极短
- 注意切片：s[left+1:right+1] 和 s[left:right]，右边界是开区间

## 教训
- 看到"删除最多一个字符后是否为回文" → 双指针 + 两种跳过情况，或辅助函数判断
