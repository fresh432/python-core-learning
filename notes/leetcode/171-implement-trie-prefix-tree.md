# LeetCode 208 实现 Trie（前缀树）

## 我的思路（60分钟）
- 前30分钟：误以为和并查集类似，始终想不出实现方式
- 中间20分钟：看答案，理解 Trie 的核心结构——多叉树，每个节点包含：
  - children：长度为 26 的数组，存放下一个字符节点
  - isEnd：标记当前节点是否是一个完整单词的结尾
- 后10分钟：跟着写出 insert、search、startsWith 和公共的 __search_prefix

## 代码
```python
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            id_ = ord(char) - ord('a')
            if not node.children[id_]:
                node.children[id_] = Node()
            node = node.children[id_]
        node.isEnd = True
    
    def search(self, word: str) -> bool:
        node = self.__search_prefix(word)
        return node is not None and node.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        return self.__search_prefix(prefix) is not None
    
    def __search_prefix(self, word: str) -> Node:
        node = self.root
        for char in word:
            node = node.children[ord(char) - ord('a')]
            if not node:
                return None
        return node
```

## 关键
- Trie 是多叉树：每个节点代表一个字符路径，26 个分支对应 26 个字母
- insert：逐字符下行，没有对应子节点就创建，最后标记 isEnd = True
- __search_prefix：公共方法，按字符路径下行，返回最终节点（或 None）
- search：前缀存在 且 isEnd == True
- startsWith：前缀存在即可（不需要是完整单词）

## 教训
- 看到"前缀树 / Trie" → 多叉树结构，每个节点 children[26] + isEnd，和并查集完全不同
- children 用数组比哈希表更快（固定 26 个字母），且节省空间
- 提取公共的 search_prefix 方法，避免 search 和 startsWith 代码重复
- 和 146 LRU 缓存对比：146 是哈希表+双向链表，208 是多叉树，两种完全不同的数据结构