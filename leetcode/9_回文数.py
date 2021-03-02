# Time: 2021/2/25 16:57
# Author: jiangzhw
# FileName: 9_回文数.py

# 9. 回文数
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
# https://blog.csdn.net/chenhua1125/article/details/80469505
# https://blog.csdn.net/qiubingcsdn/article/details/81773168?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase

x1 = 121  # 输出：true
x2 = -121  # 输出：false
x3 = 10  # 输出：false
x4 = -101  # 输出：false


class Solution1:
    # 整数转字符串，通过下标对比确定该整数是否为回文数
    def is_palindrome(self, x: int) -> bool:
        str_x = str(x)
        # print(str_x[-1])
        for i in range(0, int(len(str_x) / 2)):
            # 因为i=0对应的是尾指针为i=-1，
            if str_x[i] != str_x[-i - 1]:
                return False
        return True


print(Solution1().is_palindrome(x1))
print(Solution1().is_palindrome(x2))
print(Solution1().is_palindrome(x3))
print(Solution1().is_palindrome(x4))


# 字符串切片操作，str[index:index:step]，中括号里面分别为：字符起点、终点和步长
class Solution2:
    def is_palindrome(self, x: int) -> bool:
        str_x = str(x)
        tmp_x = str_x[::-1]
        if tmp_x == str_x:
            return True
        return False

    # 代码简化：
    def is_palindrome2(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


print(Solution2().is_palindrome2(x1))
print(Solution2().is_palindrome2(x2))
print(Solution2().is_palindrome2(x3))
print(Solution2().is_palindrome2(x4))


# 数学计算的方法，对比反转整数的值,不太适应
class Solution3:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp_x = x
        palindromeNum = 0
        while temp_x != 0:
            palindromeNum = palindromeNum * 10 + temp_x % 10
            temp_x /= 10
            # print(f"{palindromeNum}:{temp_x}")
        return palindromeNum == x


print(Solution3().is_palindrome(x1))
print(Solution3().is_palindrome(x2))
print(Solution3().is_palindrome(x3))
print(Solution3().is_palindrome(x4))


# 整数转字符串，反转字符串，对比反转后字符串与原字符串是否相等
class Solution4:
    def is_palindrome(self, x: int) -> bool:
        str_x = str(x)
        str_y = ""
        for i in str_x:
            str_y = i + str_y
        print(str_y)
        return str_y == str_x


print(Solution4().is_palindrome(x1))
print(Solution4().is_palindrome(x2))
print(Solution4().is_palindrome(x3))
print(Solution4().is_palindrome(x4))


# reverse方法翻转列表比较
class Solution5:
    def is_palindrome(self, x: int) -> bool:
        x_list = list(str(x))
        tmp_list = list(str(x))
        tmp_list.reverse()
        # print(x_list)
        # print(tmp_list)
        return tmp_list == x_list


print(Solution5().is_palindrome(x1))
print(Solution5().is_palindrome(x2))
print(Solution5().is_palindrome(x3))
print(Solution5().is_palindrome(x4))
