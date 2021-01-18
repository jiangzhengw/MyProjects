# Time: 2021/1/18 10:17
# Author: jiangzhw
# FileName: base_api.py
import requests
import json


class BaseApi:
    """base api"""
    params = {}

    def send(self, data):
        """
        发送requests请求方法
        :return:
        """
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        return requests.request(**data).json()
