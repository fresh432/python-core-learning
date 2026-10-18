# LeetCode 380 O(1) 时间插入、删除和获取随机元素

## 我的思路（23分钟）
- 用数组 + 字典 + 下标维护集合
- 插入：数字添加到数组和字典，字典存 {值: 数组下标}，index += 1
- 删除：最初想直接删除，但数组删除是 O(n)。后改为交换被删元素与数组最后一个元素，更新字典中最后一个元素的新下标，然后 pop()，实现 O(1)
- 获取随机：最初想随机交换再返回第一个，但时间复杂度高。改为直接用 random.randint 随机取下标返回数组对应值，O(1)

## 代码
```python
import random

class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.nums = []
        self.index = 0
    
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = self.index
        self.nums.append(val)
        self.index += 1
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # 交换被删元素与最后一个元素
        self.dict[self.nums[-1]] = self.dict[val]
        self.nums[self.dict[val]], self.nums[-1] = self.nums[-1], self.nums[self.dict[val]]
        self.nums.pop()
        del self.dict[val]
        self.index -= 1
        return True
    
    def getRandom(self) -> int:
        return self.nums[random.randint(0, self.index - 1)]
```

## 关键
- 数组 + 哈希表：数组支持 O(1) 随机访问，哈希表支持 O(1) 查找
- 删除技巧：交换被删元素与末尾元素 + pop()，避免数组中间删除的 O(n) 开销
- 随机访问：random.randint(0, index-1) 直接取下标

## 教训
- 看到"O(1) 插入删除随机获取" → 数组 + 哈希表，删除时交换到末尾再 pop