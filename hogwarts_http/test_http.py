# Time: 2020/12/9 19:47
# Author: jiangzhw
# FileName: test_http.py
import json

# 将已编码的json字符串解码成python对象
# json.load()

# 将python对象编码成json字符串
# json.dumps()

# requests是一个很实用的Python HTTP客户端库
import requests
import pystache
import jsonpath
from hamcrest import *
from requests_xml import XMLSession
from jsonschema import validate


class TestDemo:

    def test_demo(self):
        r = requests.get("http://httpbin.testing-studio.com/")
        print(r.content)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        # payload是post请求时，所携带的有效数据的意思
        payload = {
            "level": 1,
            "name": "MrJ",
            "pwd": "123456a?"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "MrJ",
            "pwd": "123456a?"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "MrJ",
            "pwd": "123456a?"
        }
        # json = 会自动把请求数据转换成json格式
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1

    def test_post_xml(self):
        xml = """<?xml version='1.0'encoding='utf-8'?> <a>test</a>"""
        headers = {"Content-Type": "application/xml"}
        r = requests.post("http://httpbin.testing-studio.com/post", data=xml, headers=headers)
        print(r.text)
        assert r.json()["headers"]["Content-Type"] == "application/xml"
        assert "xml" in r.json()["data"]

    def test_post_file(self):
        files = {"file": open("report.xls", "rb")}
        r = requests.post("url", files=files)

    # 基本信息：r.url ,r.status_code , r.headers , r.conkies
    # 响应结果:
    # r.text = r.encoding + r.content 返回编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
    # r.content 返回二进制结果
    # r.json() = r.encoding + r.content + content type json 返回JSON格式，可能抛出异常
    # r.raw.read(10) 返回原始socket response，需要加参数stream=True
    def test_header(self):
        r = requests.get('http://httpbin.testing-studio.com/get', headers={"h": "header test"})
        print(r.content)
        print(r.text)
        print(r.json())
        print(r.raw.read(10))
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header test"

    # 复杂数据解析
    # 数据保存：将复杂的json或xml请求体保存到文件模板中
    # 数据处理：
    #     使用mustache、freemaker等工具解析
    #     简单的字符串替换
    #     使用json xml api进行结构化的解析
    # 数据生成：生成最终的结果
    def test_complex_data(self):
        # Todo：遇到复杂请求体时实现
        pass

    # 断言:
    #     json断言：assert r.json()

    def test_hogwarts_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.json())
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"

    #     json path断言 和 xml 对应的xpath 语法类似
    def test_json_path(self):
        r = requests.get("https://ceshiren.com/categories.json")
        assert jsonpath.jsonpath(r.json(), '$..name')[0] == "开源项目"

    # xml 断言,不过 好像不支持python 3.7
    def test_xml(self):
        session = XMLSession()
        r = session.get("https://ceshiren.com/categories.json")
        assert r.xml.xpath('..//name')[0] == "开源项目"

    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(jsonpath.jsonpath(r.json(), '*..name'))
        assert_that(r.json()["category_list"]["categories"][0]["name"], equal_to("开源项目"))

    # 用于判断增量的接口变化，不过复杂的规则需要自己去实现判断策略
    def test_get_jsonschema(self):
        # Todo：可手工生成schema，也可自动生成schema
        url = "https://ceshiren.com/categories.json"
        data = requests.get(url).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)

    # header and cookie
    def test_demo01(self):
        url = "http://httpbin.testing-studio.com/cookies"
        header = {
            'User-Agent': 'hogwarts'
        }
        cookie_data = {
            'hogwarts': 'school',
            'name': 'jiangzhw'
        }
        res = requests.get(url=url, headers=header, cookies=cookie_data)
        print(res.request.headers)

    # auth 参数传递认证信息
    def test_auth(self):
        from requests.auth import HTTPBasicAuth
        url = "http://httpbin.testing-studio.com/basic-auth/admin/admin"
        res = requests.get(url=url, auth=HTTPBasicAuth('admin', 'admin'))
        print(res)
