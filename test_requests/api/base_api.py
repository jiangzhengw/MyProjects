# Time: 2021/1/18 10:17
# Author: jiangzhw
# FileName: base_api.py
import requests


class BaseApi:
    """base api"""

    def send(self, data):
        """
        发送requests请求方法
        :return:
        """
        return requests.request(**data).json()
