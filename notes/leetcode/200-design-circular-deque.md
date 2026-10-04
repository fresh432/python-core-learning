# LeetCode 641 设计循环双端队列

## 我的思路（50分钟）
- 前20分钟：用 Python 列表的 pop 和 append 写了一个能通过但感觉不正规的版本
- 中间20分钟：看答案，了解环形数组实现：
  - 用固定大小数组 + front/rear 双指针
  - front 指向队头元素，rear 指向队尾元素的下一个位置
  - 头插：front = (front - 1 + capacity) % capacity，然后赋值
  - 尾插：先赋值，rear = (rear + 1) % capacity
  - 删除：仅移动指针（逻辑删除），size -= 1
  - 判满判空：用 size 维护
- 后10分钟：按环形数组思路重写，通过

## 代码
```python
class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity = k
        self.mydeque = [0] * k
        self.size = 0
        self.front = 0
        self.rear = 0
    
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.mydeque[self.front] = value
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.mydeque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True
    
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.mydeque[self.front]
    
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.mydeque[self.rear - 1]
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.capacity
```

## 关键
- 环形数组：固定大小，front 和 rear 指针循环移动（取模）
- front 左移（-1）时加 capacity 再取模，防止负数
- rear 指向队尾元素的下一个位置，所以 getRear 返回 mydeque[rear - 1]
- 逻辑删除：只移动指针，不清理数据

## 教训
- 看到"设计循环队列/双端队列" → 环形数组 + 双指针 + size
