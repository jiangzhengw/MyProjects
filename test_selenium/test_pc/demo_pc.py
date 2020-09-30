# Time: 2020/9/23 14:20
# Author: jiangzhw
# FileName: demo_pc.py
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestPC:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--remote-debugging-port=9222")  # open devtools for operator element
        options.add_experimental_option('w3c', False)
        path = "D:/driver/chromedriver_win32_80.0.3987.16/chromedriver.exe"
        options.set_capability('platform', 'WINDOWS')  # test windows app
        options.set_capability('version', '10')  # window version
        options.binary_location = "C:/Users/jiangzhw01/AppData/Local/Programs/ccwork-pc/cloudAlpha.exe"  # start up app path
        self.driver = webdriver.Chrome(executable_path=path, options=options)
        self.driver.implicitly_wait(10)

    def test_login_out(self):
        # print(win32gui.FindWindow(None, "云上协同"))
        print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()
        sleep(5)
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        avatar = self.driver.find_element_by_css_selector(".sidebar .user-avatar img")
        ActionChains(self.driver).move_to_element(avatar).perform()
        self.driver.find_element(By.LINK_TEXT, "登出").click()
        self.driver.find_element(By.CSS_SELECTOR, ".chat-primary .chat-title").click()

    def test_login_fwh(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.CSS_SELECTOR, ".chat-primary .chat-title").click()

    def teardown_method(self):
        sleep(15)
        self.driver.quit()
