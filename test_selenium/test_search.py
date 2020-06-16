# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实现鼠标相关的复杂操作
from selenium.webdriver.common.actions import *
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# selenium-ide方便用于初始化时生成代码。
class TestDefaultSuite():
    # python的fixture : 测试装置执行的流程
    def setup_method(self, method):
        # 调用Chrome的浏览器驱动driver
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        # case完成后关闭浏览器
        # self.driver.quit()
        pass

    def test_testsearch(self):
        # selenium的driver的一些api方法
        # get打开一个地址
        self.driver.get("https://testerhome.com/")
        # 设置windows窗口大小
        self.driver.set_window_size(1316, 784)
        # find_element找到节点后，返回一个element的对象，element对应有一些api操作
        self.driver.find_element(By.NAME, "q").click()
        # 输入文字
        self.driver.find_element(By.NAME, "q").send_keys("appium")
        # 回车
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-search").click()
