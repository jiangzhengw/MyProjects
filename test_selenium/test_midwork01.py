# Time: 2020/6/15 11:16
# Author: jiangzhw
# FileName: test_midwork01.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_MidWork01:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://testerhome.com/')

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()

    def test_testmidwork01(self):
        self.driver.get("https://testerhome.com/")
        self.driver.set_window_size(1316, 784)
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".topic-23817 .title").click()

    def test_mainpage(self):
        self.driver.find_element(By.CSS_SELECTOR, '#main-nav-menu > ul > li:nth-child(4) > a').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.panel-body > div > div:nth-child(1) > div > div.media-body > div.media-heading > a').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.panel-body > div:nth-child(1) > div.infos.media-body > div.title.media-heading > a').click()
