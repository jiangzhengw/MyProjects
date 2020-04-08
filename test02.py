# 函数创建
def num():
    """
    num :return:
    """
    print(2+2)
# num()

# 函数参数学习，a关键词参数，b默认参数，c可变参数拆箱参数，d词典参数
# a:卡位，需要传参，
# b:不需要传参有默认值的参数
# *表示任意长度参数
# c:元组  任意多的参数一般放到参数最后
# **词典参数
# d:词典  需要传入词典类型的参数

def fun(a,b=1,*c,**d):
    # print(a)
    print(f"a={a}\nb={b}\nc={c}\nd={d}")

# fun(1,2)
# fun(1,2,3)
# fun(1,2,3,4)
fun(1,2,3,4,5,6,x=1,y=2,apple=2)

# *可以打散参数，参数的拆箱理解
def fun1(*x):
    print(x)

def fun2(x):
    print(x)

# m = (1,2,3)
m = 1,2,3
fun1(1,2,3)
fun1(m)
fun1(*m)
fun2(m)

# 设置返回值类型
def fun3(x) ->str:
    print(x)



# 类定义
class Student:
    # 类变量
    name=""
    # 初始化方法

    # 实例方法
    def study(self,*c):
        # 实例变量

        self.name = c
        print(c)
        return c
class Teacher:
    # 类方法
    @classmethod
    def shar(cls,*c):
        print(c)