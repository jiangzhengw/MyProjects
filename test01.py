# 导入队列包
from collections import deque

# 数字numbers
# 字符串Strings
# 列表List

# 数字numbers
# 反斜杠转移
print('C:\\some\\name')
# r表示原生
print(r'C:\some\name')
# python的自动拼接
print('Py' + 'thon')

# 字符串Strings
# format()和f前缀的使用
x = 'adc'
print('C:\\some\\name' + x)
print('C:\\some\\name{}'.format(x))
print('C:\\some\\name{}\\{}'.format(x, 123))
print('C:\\some\\name{x}\\{y}'.format(y=x, x=123))
print(f'C:\\some\\name{x}')

# 列表List
squares = ['1', '2', '4', '5']
l = len(squares)
print(squares[0])
# python切片,左闭右开
print(squares[0:3])
print(squares[-2:])
print(squares[-2:-1])

# 列表操作append,insert,remove,pop,sort
L = ['2', '13', '28', '37', '88', "99"]
# append尾部追加
print(L)

# 队列，先进先出，尾部追加头部弹出
queque = deque(L)
# 右出
queque.pop()
queque.pop()
# 左出
queque.popleft()
queque.popleft()

# list
# 表达式创建简单列表
x = [x for x in range(10)]
print(x)
x = [x * 10 for x in range(10)]
print(x)

# 列表：list []
# 元组：tuple ()
# 集合 :set {}
# 词典 :Dictionary {'':x,'',y}

# 集合set,打印的数据不重复
basket = {'apple', 'orange', 'peach', 'apple'}
basket.add("a")
basket.add("a")
basket.add("apple")
print(basket)
basket2 = {'apple', 'orange', 'peach', 'apple', 'b'}
# 找出两个集合中相同的元素
basket2.intersection(basket)
# 找出两个集合中不同的元素
basket2.difference(basket)

# 元组tuple,固定顺序的列表，不可变的，只能重新创建不可追加
t = 1, 2, 3
t = 1, 2, 3, (5, 6, 7)

# Lists

# 词典Dictionary
d = {'a': 1, 'name': "apple"}
print("--------------")
d['a']
d['age'] = 10
d['age']
d = {d: d ** 2 for d in (2, 4, 5)}
print(d)
print("--------------")
# 词典遍历
for k, v in d.items():
    print(k, v)

# enumerate返回下标和key值
for k, v in enumerate(d):
    print(k, v)

# if elif else

# for遍历 for i in List：
#           if :elif : else:
#         for i in range(10)

# while 比较灵活但是要小心出现死循环
