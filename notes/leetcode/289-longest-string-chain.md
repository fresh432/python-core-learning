# LeetCode 1048 最长字符串链

## 我的思路（32分钟）
- 前22分钟：用的动态规划
  - 先将单词数组按长度排序
  - 初始化哈希表存所有单词对应的最长词链长度，维护全局 ans。
  - 双层遍历：外层单词、内层每个字符，查询"缺少当前字符后的剩余子串"是否在哈希表中出现过，出现过则取该轮最长的词链长度加一、存入当前单词的哈希表值，ans 更新最大值
  - 都没出现过则当前单词存 1。全部遍历完返回 ans
- 感觉还有更优解，看答案10分钟：记忆化递归
  - 单词数组转集合（去重 + 方便查找）
  - 递归函数传入字符串，维护局部词链长度 res = 0
  - 遍历字符串每个位置做删除操作，剩余子串拿去集合查询，存在则递归该子串并更新 res 最大值
  - 返回 res + 1，递归函数加 @cache 记忆化避免重复子问题，主函数取所有单词递归结果的最大值

## 代码（排序 + 哈希 DP）
```python
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        hash_map = defaultdict(int)
        ans = 1
        for w in words:
            for i in range(len(w)):
                tmp = w[:i] + w[i + 1:]              # 删除第 i 个字符
                hash_map[w] = max(hash_map[w], hash_map[tmp] + 1)
            ans = max(ans, hash_map[w])
        return ans
```

## 代码（记忆化递归）
```python
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        ws = set(words)

        @cache
        def dfs(s):
            res = 0
            for i in range(len(s)):
                tmp = s[:i] + s[i + 1:]
                if tmp in ws:
                    res = max(res, dfs(tmp))
            return res + 1

        return max(dfs(w) for w in ws)
```

## 关键
- 链的构成关系：单词 A 是 B 的前驱 ⇔ 删掉 B 的某一个字符得到 A。所以每个单词有 len(w) 个候选前驱
- DP 版：按长度升序处理，保证前驱先算（一维哈希 DP，与 LIS 同构）
- DFS 版：逆向思维，从当前单词出发找前驱，@cache 记忆化；单词集合做 O(1) 存在性查询

## 教训
- 看到"单词链/逐步删字符" → 哈希 DP（长度排序正序处理）或记忆化 DFS（@cache + 集合查询）
- 和 241 复习形成呼应：DFS + @cache 与 DP 填表互为表里，同一问题两条路，都要会写