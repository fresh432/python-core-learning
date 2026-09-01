# LeetCode 88 合并两个有序数组

## 我的思路（30分钟）
- 前15分钟：想从前往后一次遍历合并，感觉需要3个指针但始终想不出具体实现——从前往后填充会覆盖 nums1 中原有还未比较的元素
- 中间5分钟：看答案，核心洞察——从后往前遍历，nums1 末尾有足够的零空间，从后往前填充大的元素，天然避免覆盖问题
- 后10分钟：根据思路写出代码

## 代码
```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        len1 = m - 1
        len2 = n - 1
        len3 = m + n - 1
        
        while len1 >= 0 and len2 >= 0:
            if nums1[len1] >= nums2[len2]:
                nums1[len3] = nums1[len1]
                len1 -= 1
            else:
                nums1[len3] = nums2[len2]
                len2 -= 1
            len3 -= 1
        
        # nums2 还有剩余，直接拷贝到 nums1 前面
        if len1 == -1:
            while len2 >= 0:
                nums1[len2] = nums2[len2]
                len2 -= 1
```

## 关键
- 从后往前填充：三个指针分别指向 nums1 有效末尾、nums2 末尾、nums1 总末尾
- 每次比较两个数组末尾元素，大的放到 nums1[len3] 位置
- 最后处理 nums2 剩余元素：若 nums1 先遍历完，把 nums2 剩余元素拷贝到 nums1 前面

## 教训
- 看到"合并到第一个数组且要求原地" → 立刻想从后往前，避免覆盖
- 从前往后需要额外空间暂存被覆盖的元素，从后往前则不需要
- 和 21 题对比：21 是链表合并（新建链表），88 是数组合并（原地从后往前）