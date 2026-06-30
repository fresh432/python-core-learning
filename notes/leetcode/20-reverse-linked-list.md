# LeetCode 206 反转链表

## 我的思路（20分钟）
- 想到双指针，但卡住临时节点
- 以为三指针实现不了，差点放弃
- 最后写出标准解法

## 代码
```python
def reverseList(head):
    cur, pre = head, None
    while cur:
        temp = cur.next   # 暂存
        cur.next = pre    # 反转
        pre = cur         # 前移
        cur = temp        # 前移
    return pre
```

## 关键
- 三指针：cur, pre, temp
- temp必须先存，否则cur.next反转后丢失
- 最后pre是新头节点

## 教训
- 链表问题要画图，指针移动要清晰
- 临时节点是必须的，不要省