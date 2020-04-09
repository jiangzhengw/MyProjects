from jzwpytest.div import div


# type()查看数据类型的方法
# 设置修改pycharm快捷键，ctrl+alt+s，搜索keymap，修改
class TestBreakWork:
    def test_div_int(self):
        assert div(10, 2) == 5
        assert div(10, 5) == 2
        assert div(1000000000, 1) == 1000000000

    def test_div_float(self):
        # 结果是浮点数，a，b本身就是浮点数
        assert div(10, 3) == 3.33
        assert div(10.2, 0.2) == 50.1

    def test_div_exc(self):
        # 不会出现商业报错，崩溃
        assert div(10, 'a')
        assert div('a', 10)

    def test_div_zero(self):
        assert div(10, 0) == None

    def test_div_fu(self):
        assert div(10, -1) == -10
