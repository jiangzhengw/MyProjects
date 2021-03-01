# Time: 2020/7/7 15:42
# Author: jiangzhw
# FileName: base_page.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """BASIC Page PO"""

    # driver=None这样写系统会识别不到driver的类型从而没有方法提示，
    # 因此初始化的时候需要指定driver的类型
    # ide 按住ctrl可以查看变量的类型和方法的返回值类型等
    _base_url = ""

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
            # _base_url在继承的类里初始化
            # self._driver.get(self._base_url)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        """查找元素"""
        # 判断元素是否是一个一直类型
        if isinstance(by, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator)

    def finds(self, locator, index):
        """查找多个元素"""
        return self._driver.find_elements(*locator)[index]

    def search_elements(self, locator):
        """查找多个元素"""
        return self._driver.find_elements(*locator)

    def wait(self, timeout, method):
        """显示等待"""
        WebDriverWait(self._driver, timeout).until(method)

    def close_page(self):
        """关闭页面"""
        sleep(10)
        self._driver.quit()
