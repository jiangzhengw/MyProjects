# Time: 2021/1/14 9:33
# Author: jiangzhw
# FileName: test_wework.py
import json
import random
import re

import pytest
import requests


def create_data():
    """
    create test data: user_id、mobile
    :return:
    """
    # done: 列表生成器
    data = [(str(random.randint(0, 9999)), str(random.randint(18100000000, 18200000000)))
            for x in range(3)]
    # TODO:迭代生成器
    # data = [("卡卡罗特", "18100000002"), ("比克", "18100000003"), ("秃林", "18100000004")]
    return data


class TestWeWork:

    def test_create(self, token, user_id, mobile, name="贝吉塔", department=None):
        """
        create member
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        res_body = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": [1],
        }
        r = requests.post(url, json=res_body)
        return r.json()

    def test_update(self, token, user_id, name=None, mobile=None):
        """
        update member messages
        :return:
        """
        res_body = {
            "userid": user_id,
            "name": name,
            "mobile": mobile
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
        r = requests.post(url, json=res_body)
        return r.json()

    def test_delete(self, token, user_id="beijta"):
        """
        delete member
        :return:
        """
        res_params = {
            "access_token": token,
            "userid": user_id
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = requests.get(url, params=res_params)
        return r.json()

    def test_find(self, token, user_id):
        """
        find member messages
        :return:
        """
        res_params = {
            "access_token": token,
            "userid": user_id
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = requests.get(url, params=res_params)
        return r.json()

    def test_add_department(self, token):
        """
        add departments
        :return:
        """
        res_body = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create"
                          f"?access_token={token}", json=res_body)
        return r.json()

    @pytest.mark.parametrize("user_id,mobile", create_data())
    def test_we_work(self, token, user_id, mobile):
        """
        testing all of the wework
        interface integration testings
        :return:
        """
        # done : 少量数据参数化处理
        user_id = user_id
        mobile = mobile
        try:
            assert "created" == self.test_create(token, user_id, "18100000001")["errmsg"]
        except AssertionError as e:
            # TODO: __str__ 函数学习
            if "mobile existed" in e.__str__():
                # TODO: 正则表达式学习
                re_user_id = re.findall(":(.*)'$", e.__str__())
                print(re_user_id)
                self.test_delete(token, user_id)
                assert "created" == self.test_create(token, user_id, mobile)["errmsg"]
        assert "贝吉塔" == self.test_find(token, user_id)["name"]
        assert "updated" == self.test_update(token, user_id, name="速八贝吉塔")["errmsg"]
        assert "速八贝吉塔" == self.test_find(token, user_id)["name"]
        assert "deleted" == self.test_delete(token, user_id)["errmsg"]
        assert 60111 == self.test_find(token, user_id)["errcode"]