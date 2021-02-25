# Time: 2021/2/20 14:48
# Author: jiangzhw
# FileName: 1_twosum.py


from typing import List


# 时间线：黎晟 2021年2月20日
# Todo : 时间复杂度和空间复杂度理解及计算

# 697. 数组的度
# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。


def find_shortest_sub_array(numbers: List[int]) -> int:
    mp = dict()
    # enumerate()函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    # 同时列出数据和数据下标，一般用在 for 循环当中。
    for i, num in enumerate(numbers, start=0):
        # print(f"{i}---{num}")
        if num in mp:
            mp[num][0] += 1
            mp[num][2] = i
        else:
            # 记录每个值出现的次数，开始下标和最终下标
            mp[num] = [1, i, i]
    # print(mp.values())
    # 定义出现次数最多和最短连续子数组的长度变量
    maxNum = minLen = 0
    # 取出计算的三个数值进行处理：次数、左下标、右下标
    for count, left, right in mp.values():
        if maxNum < count:
            maxNum = count
            minLen = right - left + 1
        elif maxNum == count:
            span = right - left + 1
            # python3.8 赋值表达式
            # if minLen > (span := right - left + 1):
            if minLen > span:
                minLen = span

    return minLen


nums = [1, 2, 2, 3, 1, 4, 2]
print(find_shortest_sub_array(nums))


# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 你可以按任意顺序返回答案。

# 方法1：
def two_sum(numbers: List[int], target: int) -> List[int]:
    l = len(numbers)
    for i in range(l):
        for j in range(i + 1, l):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return []


# 方法二：
class Solution2:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            # print(num)
            # 如果target的目标值和当前值的差，刚好存在表内，则返回当前num的下标，
            # 和之前target-num对应的value下标
            # 否则将当前数值和下标键值对形式存入字典哈希表内
            if target - num in hashtable:
                # print(hashtable)
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i

        return []


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
print(Solution2().two_sum(nums, target))
nums = [4, 3, 2]
target = 6
print(two_sum(nums, target))
print(Solution2().two_sum(nums, target))
nums = [3, 3]
target = 6
print(two_sum(nums, target))
print(Solution2().two_sum(nums, target))
