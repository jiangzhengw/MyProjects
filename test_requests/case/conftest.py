# Time: 2021/1/14 14:34
# Author: jiangzhw
# FileName: conftest.py
import pytest
import requests

# TODO:文件锁，防止用例并发生成多个session造成大量时间浪费
@pytest.fixture(scope="module")
def token():
    """
    获取access_token
    :return:
    """
    res_params = {
        "corpid": "wwa2fcd79577974bd3",
        "corpsecret": "6KMV_5vrtuiyeaaJf66xsxndsHat_M_Xcw2ygIaZ-to"
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    r = requests.get(url, params=res_params)
    return r.json()['access_token']

