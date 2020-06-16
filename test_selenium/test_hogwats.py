# Time: 2020/6/15 14:18
# Author: jiangzhw
# FileName: test_hogwats.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 函数名上按ctrl可以快捷查看函数的参数

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
        self.driver = webdriver.Chrome()
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
        # 显示等待和隐式等待结合的灵活运用
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

    def teardown_method(self):
        time.sleep(5)
        self.driver.quit()
