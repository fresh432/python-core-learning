# LeetCode 621 任务调度器

## 我的思路（30分钟）
- 前15分钟：没思路
- 后5分钟：看答案，核心洞察——出现次数最多的任务决定最短时间。因为冷却时间固定，出现最多次的任务其最短编排位置是固定的，只需在其间隔中编排其他任务
- 公式：max(任务总数, (maxFreq - 1) * (n + 1) + 出现 maxFreq 次数的任务个数)
- 后10分钟：顺着思路写出，通过

## 代码
```python
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_c = defaultdict(int)
        max_c = 0
        
        for task in tasks:
            hash_c[task] += 1
            max_c = max(hash_c[task], max_c)
        
        max_chars = 0
        for _, value in hash_c.items():
            if value == max_c:
                max_chars += 1
        
        return max(len(tasks), (n + 1) * (max_c - 1) + max_chars)
```

## 关键
- max_c：出现次数最多的任务的频率
- max_chars：出现 max_c 次的任务种类数
- 核心公式：(max_c - 1) * (n + 1) + max_chars
  - max_c - 1：最高频任务形成的间隔数
  - n + 1：每个间隔的长度（任务本身 + n 个冷却单位）
    - + max_chars：最后一行可以同时放多个最高频任务
- 特殊情况：若任务种类很多，冷却时间内可以排满其他任务，此时答案就是 len(tasks)

## 教训
- 看到"任务调度，有冷却时间" → 最高频任务决定最短时间，公式 max(len(tasks), (max_c-1)*(n+1) + max_chars)
