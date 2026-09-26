# LeetCode 138 随机链表的复制

## 我的思路（60分钟）
- 前30分钟：想用哈希表存每个节点值对应的节点，遍历两遍——第一遍构造新节点存列表，第二遍连接并处理 random。但调试始终不过
- 中间10分钟：看答案，发现思路差不多，但答案哈希表的 key 是原节点，value 是对应的新节点。第二遍遍历时直接用哈希表中原节点对应的新节点进行 next 和 random 连接，非常简洁
- 后5分钟：用哈希表法写了一遍
- 后10分钟：看了拼接拆分法（空间 O(1)）——先在原链表每个节点后插入复制节点，第二遍处理 random（cur.next.random = cur.random.next），最后将两个链表拆分
- 后5分钟：用拼接拆分法写了一遍

## 代码（哈希表法）
```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        dic = {}
        cur = head
        
        # 第一遍：创建新节点
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        
        # 第二遍：连接 next 和 random
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        
        return dic[head]
```

## 代码（拼接拆分法，空间 O(1)）
```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        cur = head
        
        # Step 1: 在每个原节点后插入复制节点
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        
        cur = head
        
        # Step 2: 处理 random 指针
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # Step 3: 拆分两个链表
        res = head.next
        pre = head
        cur = res
        
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        
        pre.next = None
        return res
```

## 关键
- 哈希表法：两次遍历，空间 O(n)，代码最直观
- 拼接拆分法：三次遍历，空间 O(1)
  - 第一步：A → B → C 变成 A → A' → B → B' → C → C'
  - 第二步：cur.next.random = cur.random.next，利用相邻关系直接赋值
  - 第三步：奇偶位置拆分两个链表
- dic.get(cur.next) 处理空指针，比 dic[cur.next] 更安全

## 教训
- 看到"复杂链表复制（含 random 指针）" → 哈希表法（直观）或拼接拆分法（空间 O(1)）
- 哈希表的 key 必须是原节点对象而不是节点值，因为值可能重复
- 拼接拆分法的核心：复制节点紧跟在原节点后面，random 的映射关系天然成立
- 和 146/460 题对比：146/460 是缓存设计（哈希表+链表），138 是链表复制（哈希表映射或原地拼接）
