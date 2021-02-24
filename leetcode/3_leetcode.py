# Time: 2021/2/22 11:45
# Author: jiangzhw
# FileName: 3_leetcode.py

# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 示例 4:
# 输入: s = ""
# 输出: 0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        # n = len(s)
        n = s.__len__()
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        # 结束位置为rk
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


class Solution2:
    # 最优解？
    def lengthOfLongestSubstring(self, s: str) -> int:
        # k为上一次元素出现的下标，i为当前下标。
        left, res, c_dict = -1, 0, {}
        for right, c in enumerate(s):
            if c in c_dict and c_dict[c] > left:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                left = c_dict[c]
                c_dict[c] = right
            else:
                c_dict[c] = right
                res = max(res, right - left)
        print(c_dict)
        return res


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 最长子串的长度
        max_len = 0
        # 存放字符的字典
        char_dict = {}
        index = 0
        while s[index:].__len__() >= max_len:
            # 当前最长子串长度
            current_len = 0
            for item in s[index:]:
                old_index = char_dict.get(item)
                if old_index is not None:
                    index = old_index + 1
                    char_dict.clear()
                    break
                char_dict[item] = index
                index += 1
                current_len += 1
            if current_len > max_len:
                max_len = current_len
        return max_len


class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        start, end, max_len = -1, 0, 0
        str_len = s.__len__()
        while end < str_len:
            char = s[end]
            if char in char_dict:
                old_index = char_dict[char]
                if old_index > start:
                    start = old_index
            diff = end - start
            if diff > max_len:
                max_len = diff
            char_dict[char] = end
            end += 1
        return max_len


if __name__ == "__main__":
    strs1 = "abcabcbb"
    strs2 = "bbbbb"
    strs3 = "pwwkew"
    strs4 = ""
    s1 = Solution()
    # print(s1.lengthOfLongestSubstring(strs1))
    # print(s1.lengthOfLongestSubstring(strs2))
    # print(s1.lengthOfLongestSubstring(strs3))
    # print(s1.lengthOfLongestSubstring(strs4))
    s2 = Solution2()
    print(s2.lengthOfLongestSubstring(strs1))
    # print(s2.lengthOfLongestSubstring(strs2))
    # print(s2.lengthOfLongestSubstring(strs3))
    # print(s2.lengthOfLongestSubstring(strs4))
