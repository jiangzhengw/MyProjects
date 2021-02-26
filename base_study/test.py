# Time: 2020/11/19 15:20
# Author: jiangzhw
# FileName: test.py


def debug(func):
    print(func)

    def wrapper():
        print("test")
        return func()

    return wrapper


@debug
def say_hello():
    print('hello')


say_hello()
