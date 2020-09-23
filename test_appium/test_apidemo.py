# Time: 2020/9/21 18:03
# Author: jiangzhw
# FileName: test_apidemo.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestApi:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"

        caps["automationName"] = "UiAutomator2"
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        # caps["fullRest"] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        self.driver.implicitly_wait(8)

    def test_api(self):
        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector()'
                             '.scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                             '.text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector()'
                             '.scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                             '.text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        self.driver.find_element(By.XPATH, "//*[@text='Make a Popup!']").click()
        self.driver.find_element(By.XPATH, "//*[@text='Search']").click()

    def teardown(self):
        sleep(10)
        self.driver.quit()
