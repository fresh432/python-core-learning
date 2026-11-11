# LeetCode 421 数组中两个数的最大异或值（复习）

## 我的思路（18分钟）
- 用字典树方法：构建树节点，每次先将当前数字添加到字典树中，再用下一个数字进行匹配
  - add 函数只负责开辟新节点，把数字的所有 bit 位加入树中
  - check 函数只负责走已有节点，尽量匹配与当前数字所有 bit 位相反的路径来获得异或最大值
  - 最后保留所有匹配结果中的最大值。无调试一次过
- 哈希前缀字典查询法不太记得了，花5分钟补了一下：类似"匹配两数之和为目标数"，每次遍历时先将所有数字当层 bit 位以上的前缀加入字典，然后构造一个可能的最大值，再匹配这个可能最大值与当前层所有数字异或后是否在字典中出现，最后决定这一层的最大值为多少

## 代码
```python
class Trie:
    def __init__(self):
        self.left = None
        self.right = None

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        HIGH_BIT = 31

        def add(num):
            cur = root
            for i in range(HIGH_BIT - 1, -1, -1):
                b = (num >> i) & 1
                if b:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left

        def check(num):
            cur = root
            x = 0
            for i in range(HIGH_BIT - 1, -1, -1):
                b = (num >> i) & 1
                if b:
                    if not cur.left:      # 优先走相反的 0
                        cur = cur.left
                        x = x * 2 + 1
                    else:
                        cur = cur.right
                        x = x * 2
                else:
                    if not cur.right:     # 优先走相反的 1
                        cur = cur.right
                        x = x * 2 + 1
                    else:
                        cur = cur.left
                        x = x * 2
            return x

        ans = 0
        for i in range(1, len(nums)):
            add(nums[i - 1])
            ans = max(ans, check(nums[i]))
        return ans
```

## 教训
- 第三次复习：70 分钟（首次）→ 18 分钟，字典树法已一次通过，add/check 拆分完全掌握
- 哈希前缀法仍是弱项（花 5 分钟补），核心动作：每轮 seen 存 num >> k 前缀、构造 x_next 假定当前位为 1、验证 x_next ^ 前缀 已在 seen 中，要与字典树法一起保持熟练
