# Time: 2020/7/7 15:05
# Author: jiangzhw
# FileName: register.py
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Register(BasePage):
    """注册页面PO"""

    def register_fail(self, corp_name):
        """注册失败"""
        self._driver.find_element(By.ID, "corp_name").send_keys(corp_name)
        self._driver.find_element(By.ID, "iagree").click()
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def get_error_message(self):
        """获取注册错误信息"""
        res = []
        for ele in self._driver.find_elements(By.CSS_SELECTOR, ".js_error_msg"):
            res.append(ele.text)
        return res
