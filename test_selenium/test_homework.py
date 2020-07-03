# Time: 2020/7/2 11:37
# Author: jiangzhw
# FileName: test_homework.py
from time import *

import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 测试用户数据完整格式(照片上传方式搞不定暂不考虑)：
# 姓名,账号,别名,性别(0男 1女)
# 国际区号,手机,座机,邮箱,地址
# 部门,职务,身份(0普通成员 1上级),上级身份负责部门
# 对外职务(0同步公司内职务 1自定义),自定义职务,是否通过邮件或短信发送企业邀请(0否 1是)


# 数据驱动
registerdata = [
    (
        "黎晟", "Ethan", "lisheng01",
        1, "62", "17866666666", "101000001", "jajsdjajsd@163.com", "萨达斯柯达",
        None, "测试工程师", 1, None,
        1, "员工", 0
    )]


class TestHomeWork:

    def wait_load(self, pf=0.5, maxtime=10) -> WebDriverWait:
        """定义显式等待方法"""
        return WebDriverWait(self.driver, maxtime, poll_frequency=pf)

    def wait(self, timeout, POLL_FREQUENCY, method):
        """显示等待方法2"""
        WebDriverWait(self.driver, timeout, poll_frequency=POLL_FREQUENCY).until(method)

    def setup(self):
        """每个测试用例执行之前会执行"""
        options = Options()
        options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        options.debugger_address = "127.0.0.1:9222"
        # 打开指定端口的浏览器：
        # win cmd输入：chrome -remote-debugging-port=9222
        self.driver = webdriver.Chrome(
            executable_path=r"D:\ChromeCoreDownloads\chromedriver_win32_83.0.41\chromedriver.exe", options=options)
        # 打开页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 设置隐式等待时间
        self.driver.implicitly_wait(5)

    def teardown(self):
        """每个测试用例执行完毕之后调用的方法"""
        # sleep(3)
        self.driver.quit()

    def open_add_member(self):
        """首页--添加成员"""
        driver = self.driver
        driver.find_element(By.ID, "menu_contacts").click()
        driver.find_element(By.CSS_SELECTOR, ".js_has_member div:nth-child(1) .js_add_member").click()

    @pytest.mark.parametrize(
        "username, english_name, "
        "userid, sex, zipCode, tel, ext_tel, email, address, "
        "dep, pos, Ident, charge_dep, "
        "out_pos, customize, by_email", registerdata)
    def set_data(self, username, english_name,
                 userid, sex, zipCode, tel, ext_tel, email, address,
                 dep, pos, Ident, charge_dep,
                 out_pos, customize, by_email):
        """添加成员设置信息"""
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_name("english_name").send_keys(english_name)
        self.driver.find_element_by_name("acctid").send_keys(userid)

    def wait_add_ele(self, driver):
        size = len(self.driver.find_elements(By.ID, "username"))
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, ".js_has_member div:nth-child(1) .js_add_member").click()
        return size >= 1

    def test_homework(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        WebDriverWait(self.driver, 10).until(self.wait_add_ele)

        # 出现网页按钮判断可点击了，但是点击后还是不跳转页面情况（网页按钮做了防自动化点击情况）可以使用循环点击
        # add_button = (By.CSS_SELECTOR, ".js_has_member div:nth-child(1) .js_add_member")
        # WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(add_button))
        # driver.find_element(*add_button).click()

        self.driver.find_element_by_id("username").send_keys("adbasds")
        self.driver.find_element_by_name("english_name").send_keys("asdasda")
        self.driver.find_element_by_name("acctid").send_keys("asdasdasd")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("17864199999")
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("12312312312")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("111111@qq.com")
        self.driver.find_element_by_id("memberEdit_address").send_keys("啊啥卡卡卡")
        self.driver.find_element(By.CSS_SELECTOR, ".js_member_editor_form div:nth-child(3) .js_btn_save").click()
