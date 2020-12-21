# Time: 2020/9/23 16:37
# Author: jiangzhw
# FileName: hello_world.py


# Cpython用内存地址作为id，因此不能保证整个生命周期内是唯一的，因为内存地址允许被复用
# 存活实例对象都有 "唯一" ID
import keyword

print(id(123))
print(id("asdc"))

# type()方法返回实例（instance）所属类型
print("-----分界线-----")
print(type(123))
print(type(1.12))

# isinstance()方法，判断实例是否属于特定类型
print("-----分界线-----")
print(isinstance(1, int))
print(isinstance(1.2, float))
print(isinstance("asd", str))


# 类型class和继承关系
class Animal: pass  # 动物


class Mammal(Animal): pass  # 哺乳动物


class Felidae(Mammal): pass  # 猫科动物


class Lion(Felidae): pass  # 狮子


class Trigger(Felidae): pass  # 老虎


class Ligger(Lion, Trigger): pass  # 狮虎兽


# issubclass()方法判断是否为某类的子类
print("-----分界线-----")
print(issubclass(Mammal, Animal))
print(issubclass(Felidae, Animal))
print(issubclass(Lion, Animal))
print(issubclass(Trigger, Animal))
print(issubclass(Ligger, Animal))
print(issubclass(Ligger, Felidae))
print(issubclass(Trigger, Felidae))
print(issubclass(Ligger, Lion))
print(issubclass(Ligger, Trigger))

# 子类的实例是任何祖先类型的实例
print("-----分界线-----")
wxh = Ligger()
print(isinstance(wxh, Lion))
print(isinstance(wxh, Trigger))
print(isinstance(wxh, Felidae))
print(isinstance(wxh, Mammal))
print(isinstance(wxh, Animal))

# 所有类型都有一个共同祖先类型object
print("-----分界线-----")
print(issubclass(Ligger, object))
print(issubclass(Trigger, object))
print(issubclass(Lion, object))
print(issubclass(Felidae, object))
print(issubclass(Mammal, object))
print(issubclass(Animal, object))

# 类型也是对象实例，但区别是所有类型都是有type创建的
print("-----分界线-----")
print(id(Animal))
print(type(Animal))
print(isinstance(Animal, type))

# 默认情况下，类型生命周期与进程相同，且仅有一个实例
print("-----分界线-----")
print(type(1) is type(1234) is int)

# 理解静态编译和动态解释型语言对于变量名的处理方式
# 对名字和目标对象的理解
# 最直接的关联操作：赋值   名字和目标对象值
# 名字没有类型，objects有。

# namespace是用来存储名字和目标引用关联的容器
# globals()和 locals()返回全局和本地名字空间字典
# locals()指向当前作用域环境，globals()总是指向名字空间
print("-----分界线-----")
x = 100
print(id(globals()))
print(id(locals()))


def t():
    x = "hello world !"
    print("-----分界线-----")
    print(locals())
    print(id(locals()))
    print(id(globals()))


t()

# 可以直接修改名字命名控件（namespace）来建立关联引用
# namespace是专门用来存储名字和目标引用关联的容器
print("-----分界线-----")
globals()["hello"] = "hello world !"
globals()["name"] = "jiangzhw"
print(hello)
print(name)

# 名字只是一个主键信息并无任何目标对象信息
# 赋值操作只是让名字在名字空间里重新关联，而非修改原目标对象。
# 一个名字只能引用一个目标对象
# 一个目标对象可以有多个名字，无论是否在相同和不同的命名空间内

# 必须使用 is操作符 判断两个名字是否引用同一对象
# 相等操作符并不能确定两个名字是否指向同一对象，仅用来比较值会否相等、
print("-----分界线-----")
a = 123334444444444
b = 123334444444444
print(a is b)
print(a == b)

# 命名规范见资料：如下
# https://www.jianshu.com/p/a793c0d960fe


# 检测动态生成代码是否违反保留字规则
print(keyword.kwlist)
print(keyword.iskeyword("is"))
print(keyword.iskeyword("False"))

# 模块成员已单下划线开头（_x）,属于私有成员，不会被星号导入
# 类型成员以双下划线，但无结尾（__x）属于自动重命名私有成员
# 已双下划线开头和结尾的，通常是系统成员，应避免使用
# 在交互模式下，单下划线返回，最后一个表达式结果
