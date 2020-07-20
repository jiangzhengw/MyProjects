# Time: 2020/7/20 14:26
# Author: jiangzhw
# FileName: test_material.py
from time import sleep

from test_selenium.page.manage_tools import ManageTools


class TestMaterial:

    def setup(self):
        self.manage_tools = ManageTools(reuse=True)

    def test_material(self):
        self.manage_tools.goto_material().switch_to_image().add_image(
            r"D:\PythonPro\Hogwars01\test_selenium\weixinbg.jpg")

    def teardown(self):
        sleep(10)
        self.manage_tools.close_page()
