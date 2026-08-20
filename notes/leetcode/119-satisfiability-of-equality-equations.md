# LeetCode 990 等式方程的可满足性

## 我的思路（60分钟）
- 前20分钟：确认用并查集，把所有 "==" 的字母合并到同一集合，然后检查 "!=" 的字母是否在同一个集合中。但写类的时候感觉有问题，改用函数式写法
- 中间10分钟：看答案，发现不用类也可以——直接用字典 fa + 递归 find 实现路径压缩
- 后15分钟：写出函数式版本
- 最后15分钟：还是想用类的方式写一遍，复用之前的 UnionFind 模板，写出类式版本

## 代码（函数式 — 简洁版）
```python
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        fa = {x: x for x in ascii_lowercase}  # 26个小写字母
        
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])  # 路径压缩
            return fa[x]
        
        def merge(x, y):
            x, y = find(x), find(y)
            if x != y:
                fa[x] = y
        
        # 第一遍：处理所有 "=="，合并集合
        for x, c, _, y in equations:
            if c == "=":
                merge(x, y)
        
        # 第二遍：处理所有 "!="，检查冲突
        for x, c, _, y in equations:
            if c == "!" and find(x) == find(y):
                return False
        
        return True
```

## 代码（类式 — 复用模板）
```python
class UnionFind:
    def __init__(self):
        self.father = {}
    
    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.father[x] = y
    
    def add(self, x, y):
        if x not in self.father:
            self.father[x] = None
        if y not in self.father:
            self.father[y] = None

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for x, c, _, y in equations:
            if c == "=":
                uf.add(x, y)
                uf.merge(x, y)
        for x, c, _, y in equations:
            if c == "!":
                uf.add(x, y)
                if uf.find(x) == uf.find(y):
                    return False
        return True
```

## 关键
- 两遍扫描：先处理所有 "=="（合并），再处理 "!="（检查冲突）
- 函数式 find 用递归 + 路径压缩，类式用迭代 + 路径压缩
- 字母范围只有 26 个小写字母，可以直接用字典或数组

## 教训
- 看到"等式/不等式约束判断可行性" → 并查集，先合并相等关系，再检查不等关系
- 函数式写法更简洁（递归 find），类式写法更易复用和扩展
- 和 547/684 题对比：547 是连通分量计数，684 是找冗余边，990 是等式约束可满足性——并查集三种经典场景
