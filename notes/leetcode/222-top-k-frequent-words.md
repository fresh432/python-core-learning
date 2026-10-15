# LeetCode 692 前K个高频单词

## 我的思路（50分钟）
- 前10分钟：手写堆实现
- 中间15分钟：想到先用哈希表统计频率，再用桶排序保存单词。但无法对相同频率的单词按字典序排序
- 中间：改用 heapq 库，但加了错误逻辑——每次 push 后判断堆大小超过 k 就弹出。因为是大顶堆，弹出的是堆顶（频率最高的），反而把前 k 个里面的元素弹出了，导致始终不通过
- 后10分钟：看答案，发现可以直接用 sorted 对哈希表排序：key=lambda x: (-x[1], x[0])，频率倒序、单词正序，然后取前 k 个
- 后5分钟：按排序法写出，通过
- 后10分钟：修正堆解法，删除错误的弹出逻辑，用 heapq 实现大顶堆，通过

## 代码（排序法）
```python
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_count = defaultdict(int)
        for word in words:
            hash_count[word] += 1
        
        res = sorted(hash_count.items(), key=lambda x: (-x[1], x[0]))
        ans = []
        for i in range(k):
            ans.append(res[i][0])
        return ans
```

## 代码（堆解法）
```python
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_count = defaultdict(int)
        for word in words:
            hash_count[word] += 1
        
        heap = []
        for key, value in hash_count.items():
            heapq.heappush(heap, (-value, key))
        
        ans = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            ans.append(word)
        return ans
```

## 关键
- 排序法：sorted(hash_count.items(), key=lambda x: (-x[1], x[0]))，频率倒序、单词字典序正序
- 堆解法：heapq 大顶堆，元素为 (-频率, 单词)，Python 元组比较会先比较第一个元素，再比较第二个
- 错误点：不要在大顶堆中维护固定大小 k，因为弹出的是最大的，会误删前 k 个元素

## 教训
- 看到"前 K 个高频，相同频率按字典序" → sorted 最简洁，或堆（元组 (-freq, word)）
- sorted 的 key 可以传元组 (-x[1], x[0])，实现多关键字排序
