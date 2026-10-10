# LeetCode 338 比特位计数

## 我的思路（28分钟）
- 找规律发现"对折点"——二进制每次进位变为仅有前缀一个1的数字（1, 2, 4, 8...）
- 遍历 0~n，判断是否为对折点：
  - 是：推1入 ans，对折点乘2
  - 否：ans.append(ans[i - point//2] + 1)，即当前数减去前对折点后的位置处的答案加一
- 简单调试一遍通过
- 后5分钟：看答案，发现更简洁的奇偶法——ans[i] = ans[i//2] + (i%2)。因为一个数乘以2后二进制只是在前面加了个0，所以偶数的1的位数等于其一半位置的值；奇数则在此基础上加1

## 代码（对折点法）
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        point = 1
        for i in range(1, n + 1):
            if i % point == 0:
                ans.append(1)
                point *= 2
            else:
                index = i - point // 2
                ans.append(ans[index] + 1)
        return ans
```

## 代码（奇偶法）
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i % 2)
        return ans
```

## 关键
- 对折点法：利用二进制进位规律，每过一个2的幂次，后续数字的1的位数都是前半段对应位置+1
- 奇偶法：偶数 i 的二进制是 i//2 左移一位（末尾补0），所以1的个数相同；奇数则末尾多一个1
- 时间复杂度：O(n)，空间复杂度：O(1)（不算输出数组）

## 教训
- 看到"0~n每个数的二进制1的个数" → 奇偶法 ans[i] = ans[i//2] + (i%2)，最简洁
