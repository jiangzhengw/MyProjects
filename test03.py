import sys

from hogwarts.sdet.Student import Students
from test02 import Student, Teacher

stu1 = Student()
stu1.name="xxxx"
print(stu1.name)
a=stu1.study("mike","hah")
print(a)

Teacher.shar(1,2,3)

# 包package：规范类结构
# 包导入同级目录可以from 包路径 import 类
# 不同级需要sys.path.append()
# sys.path.append("")
Students()
for i in sys.path:
    print(i+"\n")