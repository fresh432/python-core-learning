# LeetCode 297 二叉树的序列化与反序列化（复习）

## 我的思路（50分钟）
- 前25分钟：想到用队列层序遍历、空节点用占位符代替；但写的时候总是出错，一度怀疑思路错了，看了之前的提交代码和答案，确认思路就是占位符
- 后25分钟：重构加调试，结果疏忽了负数的情况，因为直接用字符串传递、中间每个数字直接拼到一起，符号被分离，导致负数用例通过不了。虽然知道只要在序列化时改成数组、拼接时用逗号给每个数做分隔就好，但还是参照以前提交的代码改了

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
                data.append(" ")          # 空节点占位符
                continue
            data.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(data)             # 逗号分隔，负数符号不会丢

    def deserialize(self, data):
        data = data.split(",")
        if data[0] == " ":
            return None
        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if data[i] != " ":            # 左孩子
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if data[i] != " ":            # 右孩子
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return root
```

## 教训
- 序列化必须用"数组 + 分隔符"，不要用裸字符串拼接，否则负数、多位数的符号和位数信息会在裸拼接中丢失
