# Time: 2020/6/16 14:29
# Author: jiangzhw
# FileName: work_mid_me.py

from selenium import webdriver
from time import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMidMe:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    def wait_click(self, timeout, ele):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(ele))

    def test_mid_me(self):
        self.driver.find_element(By.CSS_SELECTOR, '[title="MTSC2020-深圳站 议题征集开始啦！"]').click()
        element_button_1 = (By.CSS_SELECTOR, '[data-toggle="dropdown"]')
        element_href_1 = (By.CSS_SELECTOR, 'ul.list li:nth-child(4) .toc-item-link')
        self.wait_click(10, element_button_1)
        self.driver.find_element(*element_button_1).click()
        self.wait_click(10, element_href_1)
        self.driver.find_element(*element_href_1).click()

    def teardown_method(self):
        sleep(10)
        self.driver.quit()
