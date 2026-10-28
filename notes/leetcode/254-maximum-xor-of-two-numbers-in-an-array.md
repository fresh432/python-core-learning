# LeetCode 421 数组中两个数的最大异或值

## 我的思路（70分钟）
- 前10分钟：以为拿最大值逐个异或就行，随即想到应尽量让高位 0 和 1 匹配，换成哈希表存值的思路
- 中间30分钟：想用哈希表存每个位为 0 和 1 时的值，从高位往下用当前位为 1 和 0 的值都异或一遍——还是超时；意识到应该匹配完当前位再向下一位推进，但思路已乱
- 后20分钟：看答案，两种方法：
  - 哈希前缀法：从高位向低位逐位确定答案。每轮用哈希表存所有数"最高位到当前位"的前缀值；假定目标当前位为 1，将假定值与所有前缀异或，结果在哈希表中出现则确认该位为 1，否则为 0
  - 字典树法：01 字典树存每个数字的 bit 路径（0 走左、1 走右）；匹配时优先走与当前 bit 相反的方向（异或得 1，结果更大），无路可走才正着走
- 后10分钟：两个方法各写一遍

## 代码（哈希前缀法）
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            for num in nums:
                seen.add(num >> k)  # 最高位到第k位的前缀

            x_next = x * 2 + 1  # 先假定当前位为 1
            found = False

            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                x = x_next - 1  # 退回当前位为 0

        return x
```

## 代码（字典树法）
```python
class Trie:
    def __init__(self):
        self.left = None   # 0
        self.right = None  # 1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        HIGH_BIT = 30

        def add(num):
            cur = root
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right

        def check(num):
            cur = root
            x = 0
            for k in range(HIGH_BIT, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if cur.right:          # 反着走：异或得 1
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
                else:
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
            return x

        n = len(nums)
        x = 0
        for i in range(1, n):
            add(nums[i - 1])
            x = max(x, check(nums[i]))
        return x
```

## 关键
- 哈希前缀法：逐位贪心确定答案位。x_next = x * 2 + 1 假定当前位为 1；x_next ^ 前缀 ∈ seen 说明存在另一个数与该数当前前缀异或后得到假定值，确认该位为 1，否则退为 0
- 字典树法：check 时优先走相反位（0 走 right、1 走 left），走一步 x = x * 2 + 1；无相反路才正走，x = x * 2
- 两者本质相同：按位贪心，高位优先确认

## 教训
- 看到"数组中最大异或值" → 高位贪心 + 哈希前缀 / 01 字典树，不要逐个异或
- 踩坑：自己两版哈希法超时的原因是"想一次匹配所有位"——正确姿势是每轮只确认一位，确认后才进下一位
