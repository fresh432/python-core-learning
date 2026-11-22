# LeetCode 953 验证外星语词典

## 我的思路（15分钟）
- 先用哈希表把外星字母顺序保存起来（字符 → 序号）
- 构造一个比较函数，按外星序对传入的两个单词进行比较：逐字符对比，遇到不同字符按序号大小返回；一方遍历完则短者在前
- 主函数顺序遍历相邻单词对，送去比较函数，任一不满足返回 False，全部通过返回 True

## 代码
```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_map = {v: i + 1 for i, v in enumerate(order)}

        def compare(w1, w2):
            i = 0
            while i < len(w1) and i < len(w2):
                if hash_map[w1[i]] < hash_map[w2[i]]:
                    return True
                elif hash_map[w1[i]] > hash_map[w2[i]]:
                    return False
                else:
                    i += 1
            return True if i == len(w1) else False   # 前缀：短者在前

        for j in range(1, len(words)):
            if not compare(words[j - 1], words[j]):
                return False
        return True
```

## 关键
- 字典序比较的细节：字符全同时，短单词是长单词的前缀才算合法（apple < apples），这个 i == len(w1) 的尾巴别丢

## 教训
- 看到"验证自定义字典序" → 哈希表存序号 + 相邻单词两两比较
