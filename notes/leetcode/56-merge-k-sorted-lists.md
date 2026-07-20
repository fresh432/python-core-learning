# LeetCode 23 合并 K 个升序链表

## 我的思路（80分钟）
1. 前20分钟：没有思路，K 个链表如何同时合并想不清楚
2. 中间30分钟：看答案理解堆排序解法——维护一个包含所有链表头节点的小顶堆，每次取出最小值节点，同时将该节点所在链表的下一个节点入堆
3. 后30分钟：理解分而治之解法——两两合并，合并过程中排序，类似归并排序的合并阶段

## 解法一：堆排序（优先队列）
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        # 堆中存 (节点值, 链表索引, 节点)，索引用于避免值相同时比较节点对象
        h = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapify(h)
        
        while h:
            _, i, node = heappop(h)
            if node.next:
                heappush(h, (node.next.val, i, node.next))
            cur.next = node
            cur = cur.next
        
        return dummy.next
```

## 解法二：分而治之（两两合并）
```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                l1 = lists[i]
                l2 = lists[i + interval]
                # 合并两个有序链表
                dummy = ListNode(0)
                cur = dummy
                while l1 and l2:
                    if l1.val <= l2.val:
                        cur.next = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                    cur = cur.next
                cur.next = l1 if l1 else l2
                lists[i] = dummy.next
            interval *= 2
        return lists[0]
```

## 关键
- 堆排序：时间 O(n log k)，空间 O(k)。k 个链表头节点入堆，每次取最小值并补充新节点
- 分治：时间 O(n log k)，空间 O(1)。interval 每次翻倍，类似归并排序的 bottom-up 合并
- 堆中存 (val, index, node)，index 避免值相同时 Python 比较 ListNode 对象报错

## 教训
- K 个有序序列合并 → 先想堆（优先队列），经典多路归并
- 分治的核心是"两两合并"，和归并排序的合并逻辑完全一致
- 和 21 题（合并两个有序链表）的关系：分治就是多次调用 21 题的合并逻辑
- 堆排序 vs 分治：

| 方法  | 时间         | 空间   | 特点            |
| --- | ---------- | ---- | ------------- |
| 堆排序 | O(n log k) | O(k) | 代码简洁，实时处理流数据  |
| 分治  | O(n log k) | O(1) | 空间优，适合链表（可原地） |

