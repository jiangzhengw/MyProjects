# Time: 2020/7/7 11:28
# Author: jiangzhw
# FileName: test_main.py
from test_selenium.page.main import Main


class TestMain:
    def test_main(self):
        main = Main()
        # 页面之间的跳转，返回其他的po，使用链式调用，实现多页面的操作。
        main.add_member().add_member("xxx")
        assert "aaa" in main.import_user().get_massage()
