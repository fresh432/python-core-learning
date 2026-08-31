# LeetCode 92 反转链表 II

## 我的思路（50分钟）
- 前25分钟：错误思路，想先定位区间再两两交换节点值/指针，实现极其复杂，写不出来
- 后25分钟：突然想到正确做法——保存反转区间的前一个节点 pre，区间内直接反转连接方向，最后把反转后的头节点接到 pre 后面。用头插法思路，把区间内的节点逐个插到 tail 前面

## 代码
```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = fast = dummy
        
        # fast 走到第 right 个节点
        for _ in range(right):
            fast = fast.next
        
        # slow 走到第 left-1 个节点（反转区间前一个）
        for _ in range(left - 1):
            slow = slow.next
        
        tail = fast.next       # 反转区间后的第一个节点
        pre = slow             # 反转区间前一个节点
        start = slow.next      # 反转区间的第一个节点（反转后变成尾）
        
        # 头插法：把 start 逐个插到 tail 前面
        for _ in range(right - left + 1):
            tmp = start.next
            start.next = tail
            tail = start
            start = tmp
        
        pre.next = fast        # 反转后的新头（原 fast）接到 pre 后面
        return dummy.next
```

## 关键
- 虚拟头节点 dummy：处理 left = 1 的边界情况
- 先定位：fast 到 right 位置，slow 到 left-1 位置
- 保存 tail = fast.next：反转区间后的节点，反转后需要接在区间尾部
- 头插法反转：把 start 节点不断往 tail 前面插，实现区间内反转
- pre.next = fast：fast 是原区间尾节点，反转后变成头节点，接到 pre 后面

## 教训
- 看到"反转链表指定区间" → 虚拟头节点 + 定位区间 + 头插法反转 + 重接前后
- 不要试图两两交换，链表指针操作已经够复杂了，头插法是最简洁的实现
- 先保存区间前后的节点（pre 和 tail），反转完再重接，避免断链后找不到后续节点
- 和 206 题对比：206 反转整个链表（只需改 next 方向），92 反转指定区间（需要额外保存前后连接点）

## 链表反转系列对比
| 题目             | 反转范围                    | 额外操作        | 核心技巧            |
| :------------- | :---------------------- | :---------- | :-------------- |
| 206 反转链表       | 整个链表                    | 无           | 逐节点反转 next 方向   |
| **92 反转链表 II** | **指定区间 \[left, right]** | **保存前后连接点** | **头插法 + 虚拟头节点** |
| 234 回文链表       | 前半部分                    | 找中点 + 比较    | 快慢指针 + 边找边反转    |
