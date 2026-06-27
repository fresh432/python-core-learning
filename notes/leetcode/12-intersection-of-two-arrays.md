# LeetCode 349 两个数组的交集

## 我的思路（15分钟）
双层哈希表：h1 存 nums1，h2 存交集，最后转列表。
问题：过度设计，两个表其实没必要。

## 大佬思路
单层 set：nums1 转 set，遍历 nums2，找到就 remove。
关键：set 天然去重，remove 同时完成"找到"和"移除"。

## 最优写法
```python
def intersection(nums1, nums2):
    st = set(nums1)
    ans = []
    for x in nums2:
        if x in st:
            st.remove(x)
            ans.append(x)
    return ans
```

## 教训
- 去重第一反应应该是 set，不是 dict
- 库函数要熟：set、list、dict 的基本操作
