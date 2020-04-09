# 课间作业
from jzwpytest.div import div


class TestBreakWork:

    def test_div_1(self):
        """
        b>0
        :return:
        """
        assert div(1, 1) == 1

    def test_div_2(self):
        """
        b=0
        :return:
        """
        assert div(1, 0) is None

    def test_div_3(self):
        """
        b<0
        :return:
        """
        assert div(1, -1) == -1

    def test_div_4(self):
        """
        a>0
        :return:
        """
        assert div(1, 1) == 1

    def test_div_5(self):
        """
        a=0
        :return:
        """
        assert div(0, 1) == 0

    def test_div_6(self):
        """
        a<0
        :return:
        """
        assert div(-1, 1) == -1