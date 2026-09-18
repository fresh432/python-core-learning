# LeetCode 211 添加与搜索单词 - 数据结构设计

## 我的思路（80分钟）
- 前30分钟：写出 Trie 框架，插入操作和 208 题一致
- 中间30分钟：设计 . 通配匹配——遇到 . 时遍历当前节点的全部子节点，若有一条能走到底则返回最终节点，再判断 isEnd。传入参数设计为剩余 word 切片 + 当前节点，但写了30分钟始终调试不通，逻辑越写越乱
- 后10分钟：看答案，发现答案的传入参数设计不同——传入完整 word + 当前索引 + 当前节点，且匹配函数直接返回 bool 值（在函数内部判断 isEnd），而不是返回节点再外部判断
- 后10分钟：把答案的哈希表改成数组存子节点的方式重写，通过

## 代码
```python
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            id_ = ord(char) - ord('a')
            if not node.children[id_]:
                node.children[id_] = Node()
            node = node.children[id_]
        node.isEnd = True
    
    def search(self, word: str) -> bool:
        return self.__dfs(word, 0, self.root)
    
    def __dfs(self, word: str, index: int, node: Node) -> bool:
        if index == len(word):
            return node.isEnd
        
        char = word[index]
        if char == '.':
            for child in node.children:
                if child and self.__dfs(word, index + 1, child):
                    return True
            return False
        else:
            id_ = ord(char) - ord('a')
            child = node.children[id_]
            if not child:
                return False
            return self.__dfs(word, index + 1, child)
```

## 关键
- 插入：和 208 题 Trie 完全一致
- . 通配：DFS 遍历当前节点的所有非空子节点，只要有一条路径匹配成功就返回 True
- 传入参数设计：完整 word + 当前索引 + 当前节点，比"剩余切片+节点"更清晰
- 终止条件：index == len(word) 时返回 node.isEnd
- 普通字符：直接走对应分支，不存在则返回 False

## 教训
- 看到"Trie + 通配符匹配" → DFS 递归，传入 (word, index, node) 三元组
- 和 208 题对比：208 是纯 Trie（insert/search/startWith），211 增加了 . 通配符搜索（需要 DFS 回溯）
- 参数设计很重要：index 比切片更清晰，避免字符串切片的额外开销
