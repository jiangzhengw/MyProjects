# Time: 2020/7/7 10:35
# Author: jiangzhw
# FileName: contact.py
import pytest
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    """通讯录页面PO"""
    _add_member_button = (By.CSS_SELECTOR, "xxx")

    def set_tel_code(self, zipCode):
        zip_code_input_locator = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input')
        zip_code_locator = (By.CSS_SELECTOR, 'li[data-value="{}"]'.format(zipCode))
        self.find(zip_code_input_locator).click()
        self.find(zip_code_locator).click()

    def add_member(self, username, english_name, user_id,
                   sex_zip_code, zipCode, mobile, tel, email, address,
                   dep, pos, identity_code,
                   out_pos, customize, send_email):
        """添加成员"""
        name_locator = (By.NAME, 'username')
        english_locator = (By.NAME, 'english_name')
        acctid_locator = (By.NAME, 'acctid')
        gender_locator = (By.NAME, 'gender')
        mobile_locator = (By.NAME, 'mobile')
        tel_locator = (By.NAME, 'ext_tel')
        email_locator = (By.NAME, 'alias')
        address_locator = (By.NAME, 'xcx_corp_address')
        pos_locator = (By.NAME, 'position')
        # todo 部门选择
        identity_locator = (By.NAME, 'identity_stat')
        out_pos_locator = (By.NAME, 'extern_position_set')
        customize_loactor = (By.NAME, 'extern_position')
        send_email_locator = (By.NAME, 'sendInvite')
        save_loactor = (By.CSS_SELECTOR, '.js_member_editor_form div:nth-child(3) .js_btn_save')

        self.find(name_locator).send_keys(username)
        self.find(english_locator).send_keys(english_name)
        self.find(acctid_locator).send_keys(user_id)
        self.finds(gender_locator, sex_zip_code).click()
        self.set_tel_code(zipCode)
        self.find(mobile_locator).send_keys(mobile)
        self.find(tel_locator).send_keys(tel)
        self.find(email_locator).send_keys(email)
        self.find(address_locator).send_keys(address)
        self.find(pos_locator).send_keys(pos)
        self.finds(identity_locator, identity_code).click()
        self.finds(out_pos_locator, out_pos).click()
        if out_pos == 1:
            self.find(customize_loactor).send_keys(customize)
        if send_email == 0:
            self.find(send_email_locator).click()
        self.find(save_loactor).click()

    def search(self, name):
        """查找成员"""
        pass

    def import_users(self, data):
        """导入成员"""
        pass

    def export_users(self):
        """导出成员"""
        pass

    def set_department(self, name):
        """设置部门"""
        pass

    def delete(self):
        """删除部门"""
        pass

    def invite(self):
        """邀请成员"""
        pass

    def add_department(self, dep):
        """添加部门"""
        pass
