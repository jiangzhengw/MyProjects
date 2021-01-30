# Time: 2021/1/16 16:19
# Author: jiangzhw
# FileName: wework.py
import requests
import yaml

from test_requests.api.base_api import BaseApi
from test_requests.api.utils import get_token


class WeWork(BaseApi):
    """ we work api """

    def __init__(self):
        self.token = get_token()
        self.params["token"] = self.token
        with open(r"D:\PythonPro\MyProjects\test_requests\data\wework.yml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def create_member(self, user_id, mobile, name, department=None):
        """
        create member
        :return:
        """
        if department is None:
            department = "1"
        # r = requests.post(url, json=res_body)
        # data = {
        #     "method": "post",
        #     "url": url,
        #     "json": {
        #         "userid": user_id,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department
        #     }
        # }

        # TODO: 数据驱动
        self.params["user_id"] = user_id
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department

        return self.send(self.data["create"])

    def update_member(self, user_id, name=None):
        """
        update member messages
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "method": "post",
            "url": url,
            "json": {
                "userid": user_id,
                "name": name
            }
        }
        return self.send(data)

    def delete_member(self, user_id="beijta"):
        """
        delete member
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        data = {
            "method": "get",
            "url": url,
            "params": {
                "access_token": self.token,
                "userid": user_id
            }
        }
        return self.send(data)

    def find_member(self, user_id):
        """
        find member messages
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        data = {
            "method": "get",
            "url": url,
            "params": {
                "access_token": self.token,
                "userid": user_id
            }
        }
        return self.send(data)

    def add_department(self):
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
                          f"?access_token={self.token}", json=res_body)
        return r.json()
