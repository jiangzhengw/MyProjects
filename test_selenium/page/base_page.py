# Time: 2020/7/7 15:42
# Author: jiangzhw
# FileName: base_page.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """BASIC API"""

    # driver=None这样写系统会识别不到driver的类型从而没有方法提示，
    # 因此初始化的时候需要指定driver的类型
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)

            self._driver.get(self._base_url)
        else:
            self._driver = driver

    def close_page(self):
        sleep(10)
        self._driver.quit()
