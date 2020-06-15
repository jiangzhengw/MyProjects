# Time: 2020/6/15 14:18
# Author: jiangzhw
# FileName: test_hogwats.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# todo:表示代办事项
class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        # 隐式等待，尽量不要用强制等待
        self.driver.implicitly_wait(5)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        # todo:显示等待
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
        # todo:显示等待
        self.driver.find_element(By.CSS_SELECTOR, ".topic-21848 .title > a").click()

    def teardown_method(self):
        time.sleep(20)
        self.driver.quit()
