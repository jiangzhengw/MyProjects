# Time: 2021/2/26 10:56
# Author: jiangzhw
# FileName: 13_罗马数字转整数.py

# 13. 罗马数字转整数
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，
# 例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，
# 数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

# 提示：

# 1 <= s.length <= 15
# s 仅含字符 ('I', 'V', 'X', 'L', 'C', 'D', 'M')
# 题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
# 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
# IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
# 关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。

class Solution:
    def romanToInt(self, s: str) -> int:
        # 创建相关哈希表
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
             'CM': 900, 'M': 1000}
        result = 0
        i = 0
        # 去掉首尾空格
        s = s.strip()
        while i < len(s):
            # 查看当前位和下一位的字符
            # 切片i到i+2位，左闭右开
            str1 = s[i:i + 2]
            # 如果当前位置是特殊情况，那么返回其在字典中对应值，并且下一次从特殊字符之后一位开始索引
            if str1 in d:
                # 字典(Dictionary)get()函数返回指定键的值，如果键不在字典中返回默认值。
                result += d.get(str1)
                i += 2
            # 如果当前位不是特殊情况，那么只返回当前位的数值
            else:
                result += d[s[i]]
                i += 1
        return result

    # 简化版，但可读性极差，引以为戒·
    def romanToInt2(self, s: str) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        # sum()方法对序列进行求和计算。
        # sum(iterable[, start])
        # iterable - - 可迭代对象，如：列表、元组、集合。
        # start - - 指定相加的参数，如果没有设置这个值，默认为0。
        return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))

    # 等同版
    def romanToInt3(self, s: str) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        result = 0
        for i, n in enumerate(s):
            # print(i)
            str1 = s[i:i + 2]
            # str1 = s[max(i - 1, 0):i + 1]  # 作者解析中的2就是用这行代码实现的
            if str1 in d:
                result += d.get(str1)
            else:
                result += d[n]
            print(result)
        return result


class Solution2:
    def romanToInt(self, s: str) -> int:
        Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        Int = 0
        n = len(s)
        # 只有在遇到特殊情况时，两个字符中左边的字符小于右边的字符，
        # 且等于右边的字符代表的数减左边字符代表的数。
        for index in range(n - 1):
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]]
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]


s1 = "III"  # 输出: 3
s2 = "IV"  # 输出: 4
s3 = "IX"  # 输出: 9
s4 = "LVIII"  # 输出: 58 解释: L = 50, V= 5, III = 3.
s5 = "MCMXCIV"  # 输出: 1994 解释: M = 1000, CM = 900, XC = 90, IV = 4.
print(Solution().romanToInt(s1))
print(Solution().romanToInt(s2))
print(Solution().romanToInt(s3))
print(Solution().romanToInt(s4))
print(Solution().romanToInt(s5))
# print(Solution().romanToInt3(s1))
# print(Solution().romanToInt3(s2))
# print(Solution().romanToInt3(s3))
# print(Solution().romanToInt3(s4))
print(Solution().romanToInt3(s5))
