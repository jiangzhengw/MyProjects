# Time: 2020/7/20 11:13
# Author: jiangzhw
# FileName: material.py
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage


class Material(BasePage):
    def go_back(self):
        """返回按钮"""
        pass

    def material_search(self):
        """搜索框"""
        pass

    def switch_to_test_list(self):
        """切换到文字栏"""
        pass

    def switch_to_image_text(self):
        """切换到图文栏"""
        pass

    def switch_to_image(self):
        """切换到图片栏"""
        image_locator = (By.CSS_SELECTOR, '[href="#material/image"]')
        self.find(image_locator).click()
        return self

    def add_image(self, image_path):
        """添加图片"""
        print(image_path)
        add_image_locator = (By.CSS_SELECTOR, '.js_upload_file_selector')
        upload_locator = (By.NAME, 'uploadImageFile')

        # upload_image_locator = (By.CSS_SELECTOR, '.material_pic_list_item')
        upload_image_locator = (By.CSS_SELECTOR, '.ww_dialog_body .material_picCard_text.js_pic_name_show')
        submit_locator = (By.CSS_SELECTOR, '[d_ck="submit"]')
        self.find(add_image_locator).click()
        self.find(upload_locator).send_keys(image_path)
        # down:显示等待无效问题:find方法要拆分元组，不然传参不对
        # ele定位加了括号，相当于只传了一个参数所以找不到
        # 报错等待超时
        self.wait(10, expected_conditions.element_to_be_clickable(upload_image_locator))
        # 报错typeerror：list和int不可比较
        # self.wait(10, lambda x: self.search_elements(upload_image_locator) > 1)

        # print(len(self._driver.find_elements(*upload_image_locator)))
        # WebDriverWait(self._driver, 10).until(lambda x: len(self._driver.find_elements(*upload_image_locator)) >= 1)
        self.find(submit_locator).click()

    def switch_to_voice(self):
        """切换到语音栏"""
        pass

    def switch_to_video(self):
        """切换到视频栏"""
        pass

    def switch_to_doc(self):
        """切换到文件栏"""
        pass

    def switch_to_send_message(self):
        """切换到发消息tab"""
        pass

    def switch_to_sent_message(self):
        """切换到已发送tab"""
        pass

    def switch_to_sent_material(self):
        """切换到素材库tab"""
        pass
