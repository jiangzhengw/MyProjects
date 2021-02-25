# Time: 2021/2/25 14:08
# Author: jiangzhw
# FileName: 7_Reverse_Integer.py

# 7. 整数反转
# 给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。

# 思路：
# 主要注意区间为[−2^31,  2^31 − 1]
# 其次考虑特殊情况：为负数的情况，考虑以零结尾的情况
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        str_x = str(x)
        # print(str_x)
        x = ''
        if str_x[0] == '-':
            # print(x)
            x += '-'
        # print(str_x[::-1])
        # lstrip()方法用于截掉字符串左边的空格或指定字符。
        # rstrip()删除string字符串末尾的指定字符（默认为空格）.
        x += str_x[::-1].strip("0").strip("-")  # 如果有0去掉反转后的首个0和去掉尾部的负号
        # x += str_x[::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        return 0


i1 = -2 ** 32
i2 = 123000
i3 = -123000
print(Solution().reverse(i1))
print(Solution().reverse(i2))
print(Solution().reverse(i3))
