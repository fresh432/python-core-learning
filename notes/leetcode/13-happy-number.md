# LeetCode 202 快乐数

## 思路
set 检测循环：如果进入循环，说明不是快乐数。

## 代码
```python
    def isHappy(self, n: int) -> bool:
        h = set()
        total = 0
        while n :
            total += (n % 10) * (n % 10)
            if n < 10:
                if total in h:
                    return False
                if total == 1:
                    return True
                else:
                    h.add(total) 
                    n = total 
                    total = 0   
            else:     
                n = n // 10  
```

## 注意
- 检测循环用 set，不要死循环