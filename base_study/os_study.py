# Time: 2020/12/22 15:12
# Author: jiangzhw
# FileName: os_study.py
import glob
import os

root_dir = r'D:\tmp'

"""
# for dirpath, dirnames, filenames in os.walk(path):
#     for file in filenames:
#         fullpath = os.path.join(dirpath, file)
#         print(fullpath)

def all_path(dirname):
    result = []  # 所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        # print("1:", maindir)  # 当前主目录
        # print("2:", subdir)  # 当前主目录下的所有目录
        # print("3:", file_name_list)  # 当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            result.append(apath)
    return result

result = []
for dir in os.listdir(path):  # 遍历当前目录所有文件和目录
    child = os.path.join(path, dir)  # 加上路径，否则找不到
    # print(child)
    if child.endswith(".air"):
        result.append(dir)
    if os.path.isdir(child):  # 如果是目录，则继续遍历子目录的文件
        for file in os.listdir(child):
            if file.endswith(".air"):
                # if os.path.splitext(file)[1] == '.air':  # 分割文件名和文件扩展名，并且扩展名为'air'
                # file = os.path.join(child, file)  # 同样要加上路径
                result.append(file)
    # elif os.path.isfile(child):  # 如果是文件，则直接判断扩展名
    #     if child.endswith(".air"):
    #         if os.path.splitext(child)[1] == '.air':
            # result.append(child)
print(result)
"""
file_result = []

for root, dirs, files in os.walk(root_dir):
    for name in files:
        file_result.append(name)
    for name in dirs:
        file_result.append(name)

print(file_result)
