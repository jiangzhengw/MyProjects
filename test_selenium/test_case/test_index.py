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
        self.index.goto_register().register_fail("黎晟科技有限公司1")

    def test_login(self):
        """登陆"""
        register_page = self.index.goto_login().goto_register().register_fail("黎晟科技有限公司2")
        # 断言错误信息
        # Python join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        print("|".join(register_page.get_error_message()))
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close_page()
