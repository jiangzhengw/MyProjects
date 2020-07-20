# Time: 2020/7/7 11:22
# Author: jiangzhw
# FileName: main.py
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact


class Main(BasePage):
    """登陆后首页PO"""
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def add_member(self):
        """添加成员"""
        locator = (By.LINK_TEXT, '添加成员')
        # self.find(locator).click()
        # 原生点击无法处理，可以调用js点击实现
        self._driver.execute_script("arguments[0].click();", self.find(locator))
        return Contact(reuse=True)

    def add_member_error(self):
        """添加成员失败"""
        # 不同的情况返回的页面不同
        # return AddMemberPage()
        pass

    def download(self):
        """立即下载"""
        pass

    def import_user(self, file):
        """发起邀请"""
        return self

    def goto_apps(self):
        """探索企业应用"""
        pass

    def goto_company(self):
        """验证公司主体信息"""
        pass

    def get_massage(self):
        """了解详情"""
        return "aaa"

    def send_massage(self):
        pass

