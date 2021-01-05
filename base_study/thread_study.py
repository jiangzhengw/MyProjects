# Time: 2021/1/4 9:48
# Author: jiangzhw
# FileName: thread_study.py
import threading


def test1():
    print("test1")


def test2():
    print("test2")


def main():
    t1 = threading.Thread(test1(), args=(1,))
    t2 = threading.Thread(test2(), args=(2,))
    t1.setDaemon(True)
    t1.start()
    t2.start()
    event = threading.Event()
    print(str(event)+"1111")


if __name__ == '__main__':
    main()
