# LeetCode 127 单词接龙

## 我的思路（80分钟）
- 前30分钟：完全没思路，不知道如何从一个单词变换到另一个单词
- 中间20分钟：看答案，核心洞察——BFS + 逐位替换字母：对当前单词的每个位置，尝试替换为 'a'~'z'，生成新单词，如果在字典中就加入队列
- 后20分钟：自己写出 BFS 版本
- 最后20分钟：看了双向 BFS 的优化方法，但有点看不懂，先掌握单向 BFS

## 代码
```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, step = queue.popleft()
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word == endWord:
                        return step + 1
                    if new_word in wordSet:
                        queue.append((new_word, step + 1))
                        wordSet.remove(new_word)  # 标记已访问
        
        return 0
```

## 关键
- BFS 求最短路径：每次变换一个字母，相当于在图中走一条边，BFS 天然保证最短
- 逐位替换：对 word 的每个位置 i，替换为 26 个字母之一，生成 new_word
- wordSet.remove(new_word)：标记已访问，防止重复入队和死循环
- 前置剪枝：endWord 不在字典中直接返回 0

## 教训
- 看到"单词变换 / 最小变换步数" → BFS + 逐位替换字母
- 字符串切片 word[:i] + c + word[i+1:] 是生成替换单词的简洁写法
- 双向 BFS 是优化方向（从起点和终点同时 BFS，减少搜索空间），但实现更复杂，先掌握单向
- 和 329 题对比：329 是 DFS 记忆化搜索（矩阵最长递增路径），127 是 BFS（最短变换路径）——两种图搜索的经典场景

## 图搜索算法对比
|      题目      | 场景           | 方法        | 核心特征          |
| :----------: | :----------- | :-------- | :------------ |
|   200 岛屿数量   | 网格连通块        | DFS       | 标记访问，计数       |
|  329 最长递增路径  | 矩阵递增路径       | DFS + 记忆化 | 缓存子问题结果       |
| **127 单词接龙** | **单词变换最短路径** | **BFS**   | **逐位替换，最短步数** |
|  210 课程表 II  | 有向图拓扑序       | BFS Kahn  | 入度为0入队        |


