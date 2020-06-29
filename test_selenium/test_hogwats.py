# Time: 2020/6/15 14:18
# Author: jiangzhw
# FileName: test_hogwats.py
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 函数名焦点上按ctrl可以快捷查看函数的参数

# headless模式，是一种无UI的浏览器模式，为了加速，用的最多的是Chrome headless,详细见Google

# 1.setUp
# 每个测试用例执行之前会执行
# 2.setUpClass
# 在每个测试类执行之前运行
# 3.setUpMidule
# 解决每个测试类开启关闭文件的问题
# 在所有测试类在调用之前会被执行一次,函数名是固定写法,会被unittest等框架自动识别

# 主要元素定位方式
"""
    元素大体的加载过程：
        title出现
        dom出现 presence
        css出现 visibility
        js执行 clickable

    主要元素定位方式：
    
    元素定位要考虑到网页的加载速度，dom元素最先加载也就是document.query()等查询到的，就是css，最后是内容link text

    XPath : 
            driver.find_element_by_xpath('//*[@id="main-nav-menu"]/ul/li[4]/a')
            find_element_by_xpath("//*[@name='username'][@type='button']")
            
    CSS_SELECTOR :  
            driver.find_element_by_css_selector('a[href="/teams"]').click()
            id : driver.find_element_by_id('loginForm')
            name : driver.find_element_by_name('username')
            tag name : driver.find_element_by_tag_name('h1')
            class name : driver.find_element_by_class_name('username')
            
    Link :  link text 指的是标签内的具体内容，一般不稳定
            driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院")
            driver.find_element_by_link_text('霍格沃兹测试学院')
            driver.find_element_by_partial_link_text('霍格沃兹') 选取带有的元素
"""

# 等待和控制台查找元素
"""
    chrome控制台简单的查找元素：
    控制台输入：document.querySelector('css选择器语法') 多个返回值只返回第一个
    或者用 $('css选择器语法')对应 document.querySelectorAll('css选择器语法')语法，但又不完全一样。
    $x('xpath定位语法') 例  :  $x('//*[@data-name="霍格沃兹测试学院"]')
    
    ctrl + B 实现方法的地方
    ctrl + alt + B 定义方法的地方
    
    默认的都是0.5s
    隐式等待：
        跟客户端无关，传了一个配置到服务端去执行等待，客户端不会等待，传给服务端一个参数，服务端找不到元素时会进行等待
        可以代替大量的强制等待
    
    显示等待：
        客户端代码里的等待，python代码
        WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(ele))
                
        详细见下文实操
"""


# todo:pycharm约定支持的一个标签，表示代办事项,可以在底部TODO窗口里代办的代码，便于查看需要编写的代码
class TestHogwarts:
    def setup_method(self):
        # os.getenv()获取系统环境变量
        browser = os.getenv("browser")
        print(browser)
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "phantomjs":
            self.driver = webdriver.PhantomJS()
        else:
            # 初始化webdriver options
            options = webdriver.ChromeOptions()

            # 使用 headless模式
            # options.add_argument("--headless")
            # options.add_argument("--disable-gpu")
            # options.add_argument("--window-size=1280,1696")

            # debugging 模式
            # 使用已经存在的Chrome进程。
            # 1、用于无法绕过登录等页面，可以直接在已有的进程内打开；2、也可以通过绕过cookie来实现
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://testerhome.com/")
        # 隐式等待，尽量不要用强制等待sleep()
        self.driver.implicitly_wait(5)
        # 初始化时定义一个通用的显示等待
        # self.wait = WebDriverWait(self.driver, 10)

    # 简单封装的一个等待方法
    def wait(self, timeout, method):
        # WebDriverWait默认等待时间 poll_frequency = 0.5
        WebDriverWait(self.driver, timeout).until(method)

    def test_hogwarts(self):
        # css定位:
        # 主要用到id,class,tag name,属性值，父子等节点的关系定位
        self.driver.find_element_by_css_selector('a[href="/teams"]').click()
        # xPath定位
        # self.driver.find_element_by_xpath('//*[@id="main-nav-menu"]/ul/li[4]/a').click()

        # time.sleep()
        # 间接css定位
        # self.driver.find_element(By.LINK_TEXT, "社团").click()
        # todo:显示等待
        # 尽量使用css定位元素，link text 有可能会导致解析元素的时候出现异常

        # 定义一个元组存储需要复用的元素
        ele = (By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]')
        self.wait(10, expected_conditions.element_to_be_clickable(ele))

        # 显示等待和隐式等待结合的灵活运用和lambda
        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_elements(ele) > 1)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))

        # element_to_be_clickable   等待元素可点击
        # presence_of_element_located   等待元素出现在Dom中
        # visibility_of_element_located 等待元素出现可以看见

        # 元组的拆箱用*
        self.driver.find_element(*ele).click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()

        # done:隐式等待
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title > a').click()
        # self.driver.find_element(By.CSS_SELECTOR, ".topic-21848 .title > a").click()

        # find_elements()返回多个element元素
        # self.driver.find_elements()

    def test_question(self):
        self.driver.get("https://testerhome.com/topics/21495")
        # 有frame时，要先切换到frame才能找到
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_link_text("提交").click()

    def test_mstc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        # 收起浏览器窗口
        self.driver.minimize_window()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        # 打印窗口信息
        print(self.driver.window_handles)
        # 切换到第二个窗口
        self.driver.switch_to.window(self.driver.window_handles[1])

        # 截图方法
        self.driver.save_screenshot("test.png")
        element = (By.PARTIAL_LINK_TEXT, "演讲申请")
        self.wait(10, expected_conditions.presence_of_element_located(element))
        self.driver.find_element(*element).click()

    # todo ：有时间看一下selenium driver 的一些 api
    def test_js(self):
        # todo : 专项测试的时候会讲如何获取性能
        # driver.execute_script()可以再打开页面时执行一些js语句，获取一些属性值等,
        # 需要加上return关键字返回js获取到的数据
        res1 = self.driver.execute_script('return document.querySelector(".active").title')
        print("\n")
        for code in ['return document.title',
                     'return document.querySelector(".active").action',
                     'return document.querySelector(".active").className',
                     'return JSON.stringify(performance.timing)']:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()
