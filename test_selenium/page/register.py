# Time: 2020/7/7 15:05
# Author: jiangzhw
# FileName: register.py
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Register(BasePage):
    """注册页面PO"""

    def register(self, corp_name):
        """注册"""
        self._driver.find_element(By.ID, "corp_name").send_keys(corp_name)
        self._driver.find_element(By.ID, "iagree").click()
        self._driver.find_element(By.ID, "submit_btn").click()
