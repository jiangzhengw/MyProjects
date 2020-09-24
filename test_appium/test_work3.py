# Time: 2020/9/24 9:58
# Author: jiangzhw
# FileName: test_work3.py
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestWork3:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "UiAutomator2"
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        # caps["fullRest"] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_work3(self):
        self.driver.find_element(By.ID, "home_search").click()
        self.driver.find_element(By.ID, "search_input_text").send_keys("alibaba")
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'title_text')and contains(@text,'股票')]").click()
        self.driver.find_element(By.XPATH,
                                 "//*[@text='09988']/../../..//*[contains(@resource-id,'follow_btn')]").click()
        self.driver.find_element(By.ID, "action_delete_text").click()
        self.driver.find_element(By.ID, "search_input_text").send_keys("alibaba")
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'title_text')and contains(@text,'股票')]").click()
        assert self.driver.find_element(By.XPATH,
                                        "//*[@text='09988']/../../..//*[contains(@resource-id,'followed_btn')]").get_attribute(
            "text") == "已添加"

    def teardown(self):
        sleep(10)
        self.driver.quit()
