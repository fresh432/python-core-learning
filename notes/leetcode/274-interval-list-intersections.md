# LeetCode 986 区间列表的交集

## 我的思路（20分钟）
- 给两个数组分别一个下标 a 和 b，大循环用来获取两组相交部分的 start 和 end
- 小循环判定：若有下标超出对应数组长度则直接返回 ans；当前两组不相交则把靠前的那一组下标加一；相交则退出小循环
- 获取交集：start 用 max 取两组左端点，end 用 min 取右端点，将交集加入 ans
- 添加完后将右端点更小的那组下标加一。无调试一遍过

## 代码
```python
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a, b = 0, 0
        ans = []
        while True:
            # 小循环：跳过不相交区间
            while True:
                if a >= len(firstList) or b >= len(secondList):
                    return ans
                if firstList[a][1] < secondList[b][0]:    # a 整体在 b 左边
                    a += 1
                elif secondList[b][1] < firstList[a][0]:  # b 整体在 a 左边
                    b += 1
                else:
                    break
            start = max(firstList[a][0], secondList[b][0])
            end = min(firstList[a][1], secondList[b][1])
            ans.append([start, end])
            if firstList[a][1] == end:   # 右端小者前进
                a += 1
            else:
                b += 1
        return ans
```

## 关键
- 双指针各管一个列表；不相交时"靠前者"下标 +1
- 相交区间 = [max(左端), min(右端)]
- 记录交集后，右端更小的列表下标 +1（它的当前区间使命完成）

## 教训
- 看到"两个有序区间列表求所有交集" → 双指针：跳过不相交 + 端点取交 + 右端小者前进
- 和 57 题对比：57 是插入新区间（定位 + 三段扫描），986 是双列表同步扫描，区间题先判断是"单列表插入/合并"还是"双列表求交"
- 与 88（合并两个有序数组）、21（合并链表）同族：双指针各扫一个序列、按条件推进