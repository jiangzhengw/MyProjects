# Time: 2020/7/7 11:28
# Author: jiangzhw
# FileName: test_main.py
from test_selenium.page.main import Main


class TestMain:

    def setup(self):
        self.main = Main(resue=True)

    def test_add_member(self):
        """添加成员"""
        # 页面之间的跳转，返回其他的po，使用链式调用，实现多页面的操作。
        self.main.add_member().add_member("xxx")
        assert "aaa" in self.main.get_massage()

    def test_import_user(self):
        """导入成员"""
        self.main.import_user("xxxx.file")
        assert "success" in self.main.import_user().get_massage()

    def test_send_message(self):
        """发送消息"""
        self.main.send_massage()
        assert "xxx" in self.main.get_massage()
