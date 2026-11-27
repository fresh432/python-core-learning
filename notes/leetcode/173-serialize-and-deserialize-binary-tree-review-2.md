# LeetCode 297 二叉树的序列化与反序列化（复习）

## 我的思路（16分钟）
- 序列化：先用列表存节点的值，层序遍历将值存入列表，空节点用占位符代替，随后用逗号拼接列表中的字符
- 反序列化：用 split(",") 按逗号分割传入的字符串，保证负数不会被破坏；接下来也是层序遍历，遇到的子节点是非有效值就跳过，有效值则创建节点并加入队列，最后返回根节点
- 字符串按逗号切分后每个位置是独立的子树值，赋值更方便；直接遍历字符处理负数符号会非常麻烦

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
                data.append("#")          # 空节点占位符
                continue
            data.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(data)

    def deserialize(self, data):
        data = data.split(",")
        if data[0] == "#":
            return None
        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if data[i] != "#":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if data[i] != "#":
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return root
```

## 教训
- 复习： 16 分钟（50 → 16），"列表 + 逗号 join + split"的完整链路已掌握
- 和上次的失误闭环：上次负数 bug 是因为裸字符串拼接，这次从第一行就是列表存值 + join