# Time: 2021/3/2 10:14
# Author: jiangzhw
# FileName: 14_最长公共前缀.py

# des:编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 提示：
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
from typing import List


# todo: 思想理解
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 分治思想
        def lcp(start, end):
            print(start, end)
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)


strs = ["flower", "flow", "flight"]  # 输出："fl"
Solution().longestCommonPrefix(strs)

strs = ["dog", "racecar", "car"]  # 输出：""
