# LeetCode 421 数组中两个数的最大异或值（复习）

## 我的思路（35分钟）
- 前25分钟：想用字典树——每个数字按 bit 位从高位到低位维护，0 存左边、1 存右边；匹配时尽量走向与当前 bit 位相反的方向保证异或最大。
- 但这次写的时候几处细节没处理好：应该是先把前一个数字存入字典树、再用当前数字去匹配；把"添加"和"匹配"的代码写到一起，逻辑分不清
- 看了眼之前提交的代码才想起来：要把 add 和 check 拆成两个独立函数，遍历时先 add(nums[i-1]) 再 check(nums[i])，清晰多了
- 花10分钟改完通过

## 代码
```python
class Trie:
    def __init__(self):
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        n = len(nums)
        ans = 0
        HIGH_BIT = 30

        def add(num):      # 存入：按 bit 位建路径
            cur = root
            for i in range(HIGH_BIT, -1, -1):
                if (num >> i) & 1:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left

        def check(num):    # 匹配：优先走相反位（异或得 1）
            cur = root
            x = 0
            for i in range(HIGH_BIT, -1, -1):
                if (num >> i) & 1:
                    if cur.left:
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
                else:
                    if cur.right:
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
            return x

        for i in range(1, n):          # 先存前面的，再匹配当前的
            add(nums[i - 1])
            ans = max(ans, check(nums[i]))
        return ans
```

## 教训
- 细节模糊：add 和 check 必须拆成两个函数——建树的只管建，查询的只管查，混在一起就逻辑混乱
- 遍历节奏：i 从 1 开始，先 add(nums[i-1]) 再 check(nums[i])，保证查询时树里已有历史元素
