# Time: 2020/9/24 17:25
# Author: jiangzhw
# FileName: demo_logging.py
import logging


def main():
    # 指定要记录的日志级别
    logging.basicConfig(filename="test.log", filemode='a', level=logging.DEBUG)
    # logging.basicConfig(level=logging.DEBUG)
    # 输出不同级别的日志
    """
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")
    """
    # 也可这样写
    logging.log(logging.DEBUG, "This is a debug log.")
    logging.log(logging.INFO, "This is a info log.")
    logging.log(logging.WARNING, "This is a warning log.")
    logging.log(logging.ERROR, "This is a error log.")
    logging.log(logging.CRITICAL, "This is a critical log.")


if __name__ == '__main__':
    main()
