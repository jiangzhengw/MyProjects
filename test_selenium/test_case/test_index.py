# Time: 2020/7/7 14:52
# Author: jiangzhw
# FileName: test_index.py

from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        """注册"""
        # self.driver.find_element_by_link_text("立即注册").click()
        # self.driver.find_element(By.ID, "corp_name").send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, "iagree").click()
        # self.driver.find_element(By.ID, "submit_btn").click()
        self.index.goto_register().register("霍格沃兹测试学院")

    def test_login(self):
        """登陆"""
        self.index.goto_login().goto_register().register("黎晟科技有限公司")

    def teardown(self):
        self.index.close_page()
