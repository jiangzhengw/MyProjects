# Time: 2021/2/26 16:22
# Author: jiangzhw
# FileName: usual_fun.py

# 参考链接：https://mp.weixin.qq.com/s/LJLPPSUEWZGKlgEqyfqnkA
# 其他内置函数了解：https://docs.python.org/3.8/library/functions.html#zip

# 1、dir()
# 不提供参数时，返回当前本地范围内的名称列表
# 提供一个参数时，返回该对象包含的全部属性

# 2、divmod(a,b)
# a -- 代表被除数，整数或浮点数；
# b -- 代表除数，整数或浮点数；
# 根据 除法运算 计算 a,b 之间的商和余数，函数返回一个元组(p,q) ，p 代表商 a//b ，q 代表余数 a%b

# 3、enumerate(iterable,start=0)
# iterable -- 一个可迭代对象，列表、元组序列等
# start -- 计数索引值，默认初始为0
# 该函数返回枚举对象是个迭代器，利用 next() 方法依次返回元素值，每个元素以元组形式存在，
# 包含一个计数元素(起始为 start )和 iterable 中对应的元素值；

# 4、eval(expression,globals,locals)
# expression -- 字符串表达式
# globals -- 变量作用，全局命名空间，如果提供必须为字典形式；可选参数
# locals -- 变量作用域，局部命名空间，如果提须可为任何可映射对象；可选参数
# 将字符串表达式解析，返回执行结果

# 5、filter(function,iterable)
# function -- 提供筛选函数名，返回 true 或 false
# iterable -- 列表、元组等可迭代对象
# 函数返回 iterable 中满足 function 为 True 的元素；假设有一个列表，
# 我们只需要其中的一部分元素，这时就可以提前写一个函数再借助 filter 来进行过滤

# 6、isinstance(object,classinfo)
# object --表示一个类型的对象，若不是此类型， 函数恒返回 False；
# calssinfo -- 为一个类型元组或单个类型；
# 判断对象 object 的类型是否为 classinfo 或 classinfo 中其中一个类型，返回 True 或 False；

# 7、map(function,iterable,...)
# function -- 执行函数；
# iterable -- 可迭代对象；
# 将 iterable 中的每一个元素放入函数 function 中依次执行，得到与 iteable 元素数量相同的迭代器；
# map() 中可迭代对象可以为多个，其中函数 function 中的参数为所有可迭代对象中并行元素，最终得到的迭
# 代器的数量是以提供元素数量最少可迭代对象为基准，当数量最少的可迭代对象所有元素输入完毕后即执行停止

# 8、input()
# 函数用于人机交互，读取从输入端输入的一行内容，转化为字符串

# 9、zip(*iteables)
# *iterables -- 两个或两个以上可迭代对象
# 将所有 iterable 对象中元素按参数顺序以元素并行方式聚合在一起，得到一个迭代器，迭代器中每个元素
# 是个n元素元组，n 表示函数中输入 iterable 参数数量
