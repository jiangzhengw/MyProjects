# Time: 2020/7/7 11:18
# Author: jiangzhw
# FileName: test_contact.py
from test_selenium.page.contact import Contact


class TestContact:
    def test_add_member(self):
        contact = Contact()
        contact.add_member("xxx")
        