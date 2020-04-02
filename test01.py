# 导入队列包
from collections import deque



# numbers
# 反斜杠转移
print('C:\\some\\name')
# r表示原生
print(r'C:\some\name')
# python的自动拼接
print('Py'+'thon')

# Strings
# format()和f前缀的使用
x='adc'
print('C:\\some\\name'+x)
print('C:\\some\\name{}'.format(x))
print('C:\\some\\name{}\\{}'.format(x,123))
print('C:\\some\\name{x}\\{y}'.format(y=x,x=123))
print(f'C:\\some\\name{x}')

# Lists
squares = ['1','2','4','5']
l=len(squares)
print(squares[0])
# python切片,左闭右开
print(squares[0:3])
print(squares[-2:])
print(squares[-2:-1])

# 列表操作append,insert,remove,pop,sort
L = ['2','13','28','37','88']
# append尾部追加
L.append("99")
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
x=[x for x in range(10)]
print(x)
x=[x*10 for x in range(10)]
print(x)
