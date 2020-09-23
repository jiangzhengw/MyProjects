# Time: 2020/7/22 18:32
# Author: jiangzhw
# FileName: demo_day1.py

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestXueQiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"

        caps["automationName"] = "UiAutomator2"
        caps["noReset"] = "true"
        caps["dontStopAppOnReset"] = "true"
        # caps["fullRest"] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        self.driver.implicitly_wait(8)

    def test_search(self):
        sleep(5)
        # self.driver.find_element(By.XPATH, "XXXXX")
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_search_and_get_price(self):
        sleep(5)
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        current_price = (MobileBy.ID, "current_price")
        assert float(self.driver.find_element(*current_price).text) > 200
        self.test_get_frame_attribute(current_price, "resource-id")

    def test_scroll(self):
        # print(self.driver.get_window_rect())
        size = self.driver.get_window_size()
        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.2) \
                .release() \
                .perform()

    def test_device(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    def test_page_source(self):
        # 打印xml信息
        print(self.driver.page_source)

    def test_mid_work_xpath(self):
        sleep(5)
        self.driver.find_element(MobileBy.ID, "home_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        title = (By.XPATH, "//*[contains(@resource-id,'title_text') and contains(@text,'股票')]")
        self.driver.find_element(*title).click()

        # print(self.driver.find_element_by_xpath(
        #     "//*[@resource-id='stock_layout']/..//*[contains(@resource-id,'current_price')]").text)

        print(self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text)
        assert float(self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text) < 260

    def test_ui_selector(self):
        scroll_to_element = (MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector()'
                             '.scrollable(true).instance(0)).scrollIntoView(new UiSelector()'
                             '.text("1小时前").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

    def test_get_frame_attribute(self, ele, frame_name):
        # 获取控件的属性
        # self.driver.find_element(*ele).get_property()  # 适用于html
        print(self.driver.find_element(*ele).get_attribute(frame_name))  # 适用于app

    def teardown(self):
        sleep(10)
        self.driver.quit()
