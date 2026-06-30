# LeetCode 203 移除链表元素

## 我的思路（35分钟）
1. 第一版：嵌套while + 头节点特殊处理 → 逻辑混乱
2. 看答案：虚拟头节点 → 统一逻辑

## 代码
```python
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    ans = cur = ListNode(next = head)
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return ans.next
```

## 关键教训
- 虚拟头节点是链表问题的通用技巧
- 不用特殊处理头节点，代码更简洁
- 删除时cur不动（因为下一个可能也要删）
