# Time: 2020/12/2 14:15
# Author: jiangzhw
# FileName: mitmpro.py
"""Send a reply from the proxy without sending any data to the remote server."""
# 从代理发送答复，而不向远程服务器发送任何数据
import json

from mitmproxy import http


# 将请求存储在flow变量中
# url 存储在 flow变量的request属性中
def request(flow: http.HTTPFlow):
    if "baidu.com" in flow.request.pretty_url:
        with open(r"D:\PythonPro\MyProjects\mitmpro\temp.json", encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),
                {"Content-Type": "application/json"}
                # b"Hello World",  # (optional) content
                # {"Content-Type": "text/html"}  # (optional) headers
            )


def response(flow: http.HTTPFlow):
    if "baidu.com" in flow.request.pretty_url:
        if "baidu.com " in flow.request.pretty_url:
            data = json.load(flow.response.content)
            data["xxx"]["xxx"] = "xxx"
            flow.response.text = json.dumps(data)
