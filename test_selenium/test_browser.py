# Time: 2020/6/16 17:22
# Author: jiangzhw
# FileName: test_browser.py
# Time: 2020/6/15 14:18
# Author: jiangzhw
# FileName: test_hogwats.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_hogwats import TestHogwarts


# python类的继承
class TestBrowser(TestHogwarts):
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    def test_mstc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        # 打印窗口信息
        print(self.driver.window_handles)

        # 切换到第二个窗口
        # 等待窗口出现
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "演讲申请").click()

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()
