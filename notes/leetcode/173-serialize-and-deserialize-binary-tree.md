# LeetCode 297 二叉树的序列化与反序列化

## 我的思路（80分钟）
- 前60分钟：序列化想用 DFS 先序遍历，反序列化想用下标索引。但忽略了这不是完全二叉树，误以为可以用 index*2+1/2 表示左右子节点位置，发现实现不了
- 序列化改为层序遍历（BFS）后，反序列化也想用层序，但误以为层序遍历就是"完全二叉树式"的固定位置映射，卡住
- 后10分钟：看答案，发现层序反序列化的正确方式——边连接左右子节点，边将非空子节点加入队列。不是固定位置映射，而是按顺序逐个分配左右子节点
- 序列化字符串用逗号分隔，空节点用空格标记，注意处理负数
- 后10分钟：按层序遍历方式重写反序列化，通过

## 代码
```python
from collections import deque

class Codec:
    def serialize(self, root):
        data = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                data.append(" ")
                continue
            data.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(data)
    
    def deserialize(self, data):
        data = data.split(',')
        if data[0] == " ":
            return None
        
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1
        
        while queue:
            cur = queue.popleft()
            if data[index] != " ":
                cur.left = TreeNode(int(data[index]))
                queue.append(cur.left)
            index += 1
            if data[index] != " ":
                cur.right = TreeNode(int(data[index]))
                queue.append(cur.right)
            index += 1
        
        return root
```

## 关键
- 序列化：BFS 层序遍历，空节点用 " " 占位，保证结构完整
- 反序列化：按顺序读取 data 数组，当前节点的左右子节点就是接下来的两个元素
- 队列维护：每创建一个非空子节点，就将其加入队列，等待后续分配它的子节点
- 分隔符：逗号分隔，负数直接用 int() 转换即可

## 教训
- 反序列化不是"找位置"，而是"按顺序分配"：data 数组按层序顺序排列，每出队一个节点，接下来的两个值就是它的左右子节点