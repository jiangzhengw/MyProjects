import allure
import pytest

from jzwpytest.div import div


# type()查看数据类型的方法
# 设置修改pycharm快捷键，ctrl+alt+s，搜索keymap，修改

# pytest --junitxml=jzwpytest/result/junit.xml --alluredir=jzwpytest/allure_results jzwpytest
# allure serve jzwpytest\allure_results 打开报告文件
# allure generate jzwpytest\allure_html 在指定地址下生成一个HTML文件

class TestBreakWork:
    # 注解实现分组执行
    @pytest.mark.happy
    def test_div_int(self):
        assert div(10, 2) == 5
        assert div(10, 5) == 2
        assert div(1000000000, 1) == 1000000000

    # pytest 参数化
    @pytest.mark.happy
    @pytest.mark.parametrize("num1, num2, res", {
        (10, 2, 5),
        (10, 5, 2),
        (10, 5, 3),
        (10000, 1, 10000)
    })
    def test_div_int_param(self, num1, num2, res):
        assert div(num1, num2) == res

    @pytest.mark.happy
    def test_div_float(self):
        # 结果是浮点数，a，b本身就是浮点数
        assert div(10, 3) == 3.33
        assert div(10.2, 0.2) == 50.1

    @pytest.mark.exception
    def test_div_exc(self):
        # 不会出现商业报错，崩溃
        assert div(10, 'a')
        assert div('a', 10)

    @pytest.mark.exception
    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            div(10, 0)

    @pytest.mark.exception
    def test_div_fu(self):
        assert div(10, -1) == -10
        # allure + pytest 报告中插入图片方法，详细见allure官方文档
        allure.attach.file('C:\\Users\\jiangzhw01\\Desktop\\12345.png', attachment_type=allure.attachment_type.PNG)
