# Time: 2020/11/17 20:41
# Author: jiangzhw
# FileName: daily_test.py

# 字符串/整型的反转输出

# 切片：
# arr [start: end: step]
# 左闭右开区间
# start 缺省表示 从最左边 index = 0 开始
# end 缺省表示 取到最右边 index = len(arr) - 1
# step 缺省表示 步长为 +1x
strs = '1234567890'
i = 120093883
print(strs[::-1])
print(str(i)[::-1])
l = list(strs)
l2 = list(str(i))
l.reverse()
l2.reverse()
print(''.join(l))
print(''.join(l2))

print("---------------")
# 打印列表基数偶数下标


print("---------------")
# 列表去重改变原列表的顺序了
l1 = [1, 4, 4, 2, 3, 4, 5, 6, 1]
l2 = list(set(l1))
# 去重不改变顺序
new_l1 = []
for i in l1:
    if i not in new_l1:
        new_l1.append(i)
print(new_l1)

print("---------------")
# 两个列表提取作为字典
list1 = ['1', '2']
list2 = ['3', '4']
print(dict(zip(list1, list2)))

# 正则表达式替换（字符串中数字乘以2）
import re

ss = 'adafasw12314egrdf523.6qew123.111'
num = re.findall('\d+', ss)
res = re.findall('\d+\.?\d+', ss)
res = re.findall('\d+\.?\d*', ss)
print(num)
new_list = [int(i) * 2 for i in list(num)]
print(res)
print(new_list)
new_list = [float(i) * 2 for i in list(res)]
print(new_list)
print("---------------")


# 将列表中的异位词分组

def group_anagrams(l: list):
    # 思路：处理过程用map进行保存；key和value值分别对应 字母的从小到大排列值 和 strs中的真实值
    d1 = {}
    # sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作,保留原列表
    for i in range(len(l)):
        # print(strs[i])
        # print(sorted(strs[i]))
        # Python join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        tmp = ''.join(sorted(l[i], reverse=True))
        # print(tmp)
        if tmp in d1:
            # 如果已存在就追加
            d1[tmp].append(l[i])
        else:
            # print("1111")
            # 如果未存在就创建一个key value
            d1[tmp] = [l[i]]
    # print(map_)
    return [v for v in d1.values()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))


# 判断字符串是否对称
def is_symmetric1(strs):
    str1 = list(strs)
    str2 = list(strs)
    str2.reverse()
    if str1 == str2:
        return "对称！"
    else:
        return "不对称！"


def is_symmetric2(strs):
    length = len(strs)
    for i in range(int(length / 2)):
        if strs[i] == strs[length - i - 1]:
            return "对称！"
        else:
            return "不对称！"


str1 = "123333333"
str2 = "123321"
str3 = "abcba"

print(is_symmetric1(str1))
print(is_symmetric1(str2))
print(is_symmetric1(str3))

print(is_symmetric2(str1))
print(is_symmetric2(str2))
print(is_symmetric2(str3))


# 冒泡排序
def bubble_sort(arr):
    if isinstance(arr, str):
        arr2 = []
        arr = re.findall('\d+', arr)
        print(arr)
        for i in range(len(arr)):
            arr2.append(int(arr[i]))
        n = len(arr2)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr2[j] > arr2[j + 1]:
                    arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
        return arr2
    else:
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


arr = [64, 34, 25, 12, 22, 11, 90, 123]
strs = "64, 34, 25, 12, 123 , 22, 11, 90"
print(bubble_sort(arr))
print(bubble_sort(strs))


# (1~255).(0~255).(0~255).(0~255)
# 方案一为字符串处理，方案二为正则表达式处理，方案三位第三方库直接判断
# 1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9]
# 100-199之间 | 200-249之间 | 250-255 之间| 10-99之间| 1-9 之间
# 1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d
# 100-199之间 | 200-249之间 | 250-255 之间| 10-99之间| 0-9 之间
# \. 反斜杠表示转义
# 25[0-5]|2[0-4]\d|[01]?\d\d?
# 250-255 | 200-249 | 0-199
# ?	匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?。
def checkip1(ip):
    p = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    # p = re.compile(
    #     '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False


# 字符串方法
def checkip2(ipstr: str):
    # strip()方法移除头尾
    # 去掉首尾空格，然后按照“.”切片
    newip = ipstr.strip().split(".")
    if len(newip) != 4:
        return False
    # 转换为int，比较
    for i in range(len(newip)):
        newip[i] = int(newip[i])
        if i == 0:
            if newip[i] <= 255 and newip[i] > 0:
                pass
            else:
                return False
        else:
            if newip[i] <= 255 and newip[i] >= 0:
                pass
            else:
                return False
    return True


# 调用第三方库
"""
import IPy
def is_ip(address):
    try:
        IPy.IP(address)
        return True
    except Exception as  e:
        return False
"""
ip1 = "127.0.0.1"
ip2 = "0.255.0.1"
print(checkip1(ip1))
print(checkip1(ip2))
print(checkip2(ip1))
print(checkip2(ip2))
"""
想象一个场景：
    我随便想1~100中的数字，你的目标是以最少的次数猜中我所想的数字，那么你会怎么做呢？

    你可能会从1开始以此往上猜，直到猜中数字，这是一种简单查找算法，每次猜测只能排除一个数字
    你可能从50开始猜，我告诉你大了或者小了，这样每猜一次，都会将剩余的数字排除掉一半，不管我心里想的是哪个数字，你在7次之内都能够猜到，因为每次猜测都将排除很多数字！
    相比之下，第二种方法会更加省时，这种算法叫做二分算法，又称折半查找。

对于要搜索的元素越多，二分查找速度比简单查找快的更多 这是二分查找算法的优点，但二分算法也有缺点，二分算法只针对有序的列表，这样插入和删除就会很困难，因此，折半查找方法只适合不经常变动的有序列表
"""


def binary_search(my_list, num):
    """
    二分算法
    :param my_list: 有序列表
    :param num: 要查找的元素
    :return: 存在返回下标　不存在返回NONE
    """
    low = 0
    high = len(my_list)
    tem = sorted(my_list)
    while low <= high:
        mid = int((low + high) / 2)
        gress = tem[mid]
        if gress == num:
            return my_list.index(tem[mid])
        elif guess > num:
            # 说明猜大了
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [19, 29, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 15, 16, 16, 17]
guess = 29
print(binary_search(my_list, guess))


# TODO:有相同值的二分查找 python

# 题目描述
# 请实现有重复数字的有序数组的二分查找。
# 输出在数组中第一个大于等于查找值的位置，如果数组中不存在这样的数，则输出数组长度加一。

# 输出位置从1开始计算
# 解题思路：难点在于查找的值是相同的，就可以按着大于的思路往下找，直到找不到大于等于的


# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型
#
def upper_bound_(n, v, a):
    if v > a[n - 1]:
        return n + 1
    if v < a[0]:
        return 1
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if v <= a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return l + 1


print(upper_bound_(7, 2, [1, 1, 2, 2, 3, 4, 5]))
print(binary_search([1, 1, 2, 2, 3, 4, 5], 2))

# 计算字符串内各字符重复次数，并列出排名前五的字符
string = "a a a b c d c z a b x ss"
# 字典表达式
tmp = {a: string.count(a) for a in list(string.replace(' ', ''))}
res = {}
for i in range(5 - 1):
    print(list(tmp.keys())[i])
    print(list(tmp.values())[i])
    res[list(tmp.keys())[i]] = list(tmp.values())[i]
print(res)


# 快速排序:思想
# 快速排序使用分治的思想，通过一趟排序将待排序列分割成两部分，其
# 中一部分记录的关键字均比另一部分记录的关键字小。之后分别对这两
# 部分记录继续进行排序，以达到整个序列有序的目的。
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # // 双反斜杠表示向下取整
    pivot = arr[len(arr) // 2]
    # pivot = arr[int(len(arr) / 2)]
    # 列表表达式
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# 将-1移到列表左边，快排>冒泡
l = [-1, 1, -1, 1, 1, 1, -1]
print(quicksort([3, 6, 8, 19, 1, 5, 5]))  # [1，3, 5, 6, 8, 19]
print(quicksort(l))

# 切片练习
l = [3, 6, 8, 19, 1, 51, 5]
print(l[:-2])


# 比较两个版本号大小1.2.3.127，1.2.4.145，返回版本号较大的
# version1 > version2返回1，如果version1 < version2返回 - 1， 除此之外返回0。
def compare_version(version1: str, version2: str) -> int:
    if not version1 and version2:
        return -1
    if version1 and not version2:
        return 1
    if not version1 and not version2:
        return 0
    version1 = version1.split('.')
    version2 = version2.split('.')
    length1 = len(version1)
    length2 = len(version2)
    if length1 < length2:
        version1 += ['0'] * (length2 - length1)
    elif length1 > length2:
        version2 += ['0'] * (length1 - length2)
    print(version1)
    print(version2)
    index1 = 0
    while index1 < max(length1, length2):
        print(index1)
        if int(version1[index1]) > int(version2[index1]):
            return 1
        elif int(version1[index1]) < int(version2[index1]):
            return -1
        else:
            index1 += 1
    return 0


version1 = "1.2.3.127"
version2 = "1.2.4.145"
print(compare_version(version1, version2))


# 对一个整数进行翻转
# todo:多种方法考虑
def reverse(x: int) -> int:
    if x < 0:
        x *= -1
        a = str(x)[::-1]
        b = int(a) * -1

    else:
        a = str(x)[::-1]
        b = int(a)

    return b


# 字典排序
# 按 值 排序
# sorted函数按key值对字典排序
# 先来基本介绍一下sorted函数，sorted(iterable,key,reverse)，sorted一共有
# iterable,key,reverse这三个参数。其中iterable表示可以迭代的对象，例如可以
# 是dict.items()、dict.keys()等，key是一个函数，用来选取参与比较的元素，
# r everse则是用来指定排序是倒序还是顺序，reverse=true则是倒序，
# reverse=false时则是顺序，默认时reverse=false。
dic = {"a": 5, "b": 2, "c": 3, "d": 4, "e": 1}
print(dic.keys())
print(dic.values())
print(dic.items())
print(sorted(dic.keys()))
print(sorted(dic.values()))
# todo:lambda表达式学习
print(sorted(dic.items(), key=lambda item: item[1], reverse=True))
