# LeetCode 406 根据身高重建队列

## 我的思路（40分钟）
- 前15分钟：完全没有头绪
- 中间15分钟：看提示，想到先排序再根据第二个元素（前面有几个更高的人）作为下标插入。但排序规则没设好，调试不过
- 后5分钟：看答案，发现排序规则是按身高降序，同身高按 k 升序。原因是先排高的不会影响后面矮的人的相对计数
- 后5分钟：修改通过

## 代码
```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 按身高降序，同身高按 k 升序
        people.sort(key=lambda x: (-x[0], x[1]))
        
        for i in range(len(people)):
            if people[i][1] < i:
                # 插入到 k 指定的位置
                people.insert(people[i][1], people[i])
                people.pop(i + 1)
        
        return people
```

## 关键
- 排序规则：(-h, k)，身高高的在前，同身高 k 小的在前
- 插入逻辑：排序后第 i 个人的 k 值就是其应该插入的位置
- 为什么先排高的：高的人先定位，后面矮的人插入时不会影响高的人的相对位置

## 教训
- 看到"根据身高和前面人数重建队列" → 按身高降序排序，然后按 k 插入
- 排序规则是关键：-x[0] 降序，x[1] 升序