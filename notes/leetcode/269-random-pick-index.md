# LeetCode 398 随机数索引

## 我的思路（5分钟）
- 初始化时把每个数字对应的所有下标存入哈希表（值为列表）
- pick 时在目标数字的下标列表长度范围内取随机数，返回该随机位置对应的下标

## 代码
```python
from collections import defaultdict
import random

class Solution:
    def __init__(self, nums: list[int]):
        self.dict = defaultdict(list)
        for index, num in enumerate(nums):
            self.dict[num].append(index)

    def pick(self, target: int) -> int:
        n = len(self.dict[target])
        i = random.randint(0, n - 1)
        return self.dict[target][i]
```

## 关键
- 哈希表：数字 → 下标列表；初始化 O(n)
- pick：列表内等概率随机，O(1)

## 教训
- 看到"等概率随机返回某值的下标" → 哈希表存下标列表
