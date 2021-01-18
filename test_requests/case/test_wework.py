# Time: 2021/1/14 9:33
# Author: jiangzhw
# FileName: test_wework.py
import re
import pytest
from pip._vendor import requests

from test_requests.api.wework import WeWork


def create_data():
    """
    create test data: user_id、mobile
    :return:
    """
    # TODO:等价类，边界值数据设计
    # done: 列表生成器
    # data = [(str(random.randint(0, 9999)),
    #          str(random.randint(18100000000,
    #                             18200000000))) for x in range(20)]
    data = [("kenan" + str(x),
             "181%08d" % x, "柯南" + str(x)) for x in range(10)]
    # TODO:迭代生成器
    # data = [("卡卡罗特", "18100000002"), ("比克", "18100000003"), ("秃林", "18100000004")]
    return data


class TestWeWork:
    def setup_method(self):
        self.main = WeWork()

    @pytest.mark.parametrize("user_id,mobile,name", create_data())
    def test_we_work(self, user_id, mobile, name):
        """
        testing all of the wework
        interface integration testings(集成测试)
        :return:
        """
        # done : 少量数据参数化处理
        user_id = user_id
        mobile = mobile
        try:
            assert "created" == self.main.create_member(user_id, mobile, name)["errmsg"]
        except AssertionError as e:
            # TODO: __str__ 函数学习
            if "mobile existed" in e.__str__():
                # TODO: 正则表达式学习
                re_user_id = re.findall(":(.*)'$", e.__str__())
                # print(re_user_id)
                self.main.delete_member(user_id)
                assert "created" == self.main.create_member(user_id, mobile, name)["errmsg"]
        assert name == self.main.find_member(user_id)["name"]
        assert "updated" == self.main.update_member(user_id, name="速八贝吉塔")["errmsg"]
        assert "速八贝吉塔" == self.main.find_member(user_id)["name"]
        assert "deleted" == self.main.delete_member(user_id)["errmsg"]
        assert 60111 == self.main.find_member(user_id)["errcode"]

    def test_demo(self, token):
        """
        test fun
        po idea and data driven use
        """
        print(self.main.create_member("beijita", "17800010001", "贝吉塔"))

    def test_session(self, token):
        s = requests.session()
        s.params = {"access_token": token}
        res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=beijita")
        print(res.json())
