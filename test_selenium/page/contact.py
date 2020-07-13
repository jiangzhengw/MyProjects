# Time: 2020/7/7 10:35
# Author: jiangzhw
# FileName: contact.py
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    """通讯录页面PO"""
    _add_member_button = (By.CSS_SELECTOR, "xxx")

    def add_member(self, data):
        """添加成员"""
        name = (By.NAME, "username")
        english_name = (By.NAME, "memberAdd_english_name")
        acctid = (By.NAME, "acctid")
        mobile = (By.NAME, "mobile")

        self.find(name).send_keys("测试姜")
        self.find(english_name).send_keys("Ethan")
        self.find(acctid).send_keys("1111122222")
        self.find(mobile).send_keys("19999999999")
        return self

    def search(self, name):
        """查找成员"""
        pass

    def import_users(self, data):
        """导入成员"""
        pass

    def export_users(self):
        """导出成员"""
        pass

    def set_department(self, name):
        """设置部门"""
        pass

    def delete(self):
        """删除部门"""
        pass

    def invite(self):
        """邀请成员"""
        pass

    def add_department(self, dep):
        """添加部门"""
        pass
