# Time: 2020/7/7 14:52
# Author: jiangzhw
# FileName: index.py

from test_selenium.page.base_page import BasePage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(BasePage):
    """Index页面 PO"""
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        """跳转注册页面"""
        self._driver.find_element_by_link_text("立即注册").click()
        return Register(self._driver)

    def goto_login(self):
        """跳转登陆页面"""
        self._driver.find_element_by_link_text("企业登录").click()
        return Login(self._driver)
