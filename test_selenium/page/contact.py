# Time: 2020/7/7 10:35
# Author: jiangzhw
# FileName: contact.py
from selenium.webdriver.common.by import By


class Contact:
    """通讯录页面PO"""

    _add_member_button = (By.CSS, "xxx")

    def add_member(self, data):
        """添加成员"""
        # self.driver.find_element("xxxx")
        # send_keys()
        # click_save()
        pass

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
