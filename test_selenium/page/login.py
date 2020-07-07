# Time: 2020/7/7 16:44
# Author: jiangzhw
# FileName: login.py
from test_selenium.page.base_page import BasePage
from test_selenium.page.register import Register


class Login(BasePage):
    """登陆页面PO"""

    # todo : 扫码
    def scan_qrcode(self):
        """扫码"""
        pass

    def goto_register(self):
        """跳转注册页面"""
        self._driver.find_element_by_link_text("企业注册").click()
        return Register(self._driver)
