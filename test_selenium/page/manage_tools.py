# Time: 2020/7/20 10:52
# Author: jiangzhw
# FileName: manage_tools.py
from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.material import Material


class ManageTools(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def goto_content_archive(self):
        """"跳转会话内容存档页面"""
        pass

    def goto_add_member(self):
        """跳转成员加入页面"""
        pass

    def goto_contacts_sync(self):
        """跳转通讯录同步页面"""
        pass

    def goto_send_message(self):
        """跳转消息群发页面"""
        pass

    def goto_user_message(self):
        """跳转用户消息页面"""
        pass

    def goto_material(self):
        """跳转素材库页面"""
        material_locator = (By.CSS_SELECTOR, '[href="#material/text"]')
        self.find(material_locator).click()
        return Material(reuse=True)

    def goto_staff_service(self):
        """跳转员工服务"""
        pass

    def goto_use_analysis(self):
        """跳转使用分析页面"""
        pass

    def goto_reward(self):
        """跳转奖励页面"""
        pass

    def goto_week_summary(self):
        """跳转一周小结页面"""
        pass
