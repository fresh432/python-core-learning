# LeetCode 399 除法求值

## 我的思路（70分钟）
- 前30分钟：确认用并查集，但卡在如何维护权重——a / b = 2.0 这种带权值的边怎么在并查集中保存和传递
- 中间25分钟：看答案，理解了带权并查集的核心：weigh[x] 表示 x 到其父节点的权重比值，find 时路径压缩要同时更新权重，merge 时要根据等式计算新权重
- 后15分钟：自己写了一遍

## 代码
```python
class UnionFind:
    def __init__(self):
        self.father = {}
        self.weigh = {}  # weigh[x] = x / father[x] 的比值
    
    def find(self, x):
        root = x
        base = 1.0
        # 先找到根，同时累乘路径上的权重
        while self.father[root] is not None:
            root = self.father[root]
            base *= self.weigh[root]
        # 路径压缩：把 x 直接挂到 root 下，同时更新 weigh[x]
        while root != x:
            original_father = self.father[x]
            self.weigh[x] *= base
            base /= self.weigh[original_father]
            self.father[x] = root
            x = original_father
        return root
    
    def merge(self, x, y, val):
        # a / b = val，即 a = val * b
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            # weigh[root_x] = weigh[y] * val / weigh[x]
            self.weigh[root_x] = self.weigh[y] * val / self.weigh[x]
    
    def is_connected(self, x, y):
        return x in self.weigh and y in self.weigh and self.find(x) == self.find(y)
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.weigh[x] = 1.0

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)
        
        res = [-1.0] * len(queries)
        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                # a / b = (a / root) / (b / root) = weigh[a] / weigh[b]
                res[i] = uf.weigh[a] / uf.weigh[b]
        
        return res
```

## 关键
- 带权并查集：每个节点 x 维护 weigh[x] = x / father[x] 的比值
- find(x) 路径压缩时：同时更新 weigh[x] 为 x / root 的总比值
- merge(a, b, val)：a / b = val，合并后 weigh[root_a] = weigh[b] * val / weigh[a]
- 查询 a / b：若连通，结果为 weigh[a] / weigh[b]（两者到根节点的比值相除）

## 教训
- 看到"等式求值 / 变量间比值关系" → 带权并查集，weigh[x] 保存到父节点的比值
- 带权并查集是并查集的进阶应用，核心在于路径压缩时同步更新权重
- 和 990 题对比：990 是普通并查集（判断等式可满足），399 是带权并查集（维护比值关系并查询）