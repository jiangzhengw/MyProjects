# Time: 2020/10/14 15:28
# Author: jiangzhw
# FileName: test_yzm.py
import os
import shutil
from time import sleep

from selenium import webdriver
import re
from PIL import Image
import pytesseract
from aip import AipOcr
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

APP_ID = '22821370'
API_KEY = 'czeeQzdYwq6aO1KNIDixaZzG'
SECRET_KEY = 'XcHO6MfkmHeoHtk2u7IbR6q6KlG16b3a'


class TestYZM:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.chaojiying.com/user/login/")
        self.driver.implicitly_wait(15)
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def test_yzm(self):
        print("\n" + "进入 test_yzm 用例！")
        self.get_pictures()

    """ 读取图片 """

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def get_pictures(self):
        # 整个页面截图的图片存放路径
        shutil.rmtree(r'D:\PythonPro\Hogwars01\yzm\picture')
        os.mkdir(r'D:\PythonPro\Hogwars01\yzm\picture')
        self.driver.save_screenshot(r'D:\PythonPro\Hogwars01\yzm\picture\poo1.png')
        # id是验证码在页面上的id
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'img[src="/include/code/code.php?u=1"]')))
        sleep(3)
        pg = self.driver.find_element(By.CSS_SELECTOR, 'img[src="/include/code/code.php?u=1"]')
        left = pg.location['x']
        top = pg.location['y']
        right = pg.size['width'] + left
        height = pg.size['height'] + top
        im = Image.open(r'D:\PythonPro\Hogwars01\yzm\picture\poo1.png')
        image_obj = im.crop((left, top, right, height))
        # 验证码截图的图片存放路径
        image_obj.save(r'D:\PythonPro\Hogwars01\yzm\picture\poo2.png')
        images = image_obj.convert("L")  # 转灰度
        images.save(r'D:\PythonPro\Hogwars01\yzm\picture\poo3.png')
        """
        pixdata = images.load()
        w, h = images.size
        # 像素值
        threshold = 190
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        """
        pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'  # 设置tesseract到环境变量内
        result = pytesseract.image_to_string(images)  # 图片转文字
        image_baidu = self.get_file_content(r'picture/poo2.png')
        # result2 = self.client.basicGeneral(image_baidu)
        result2 = self.client.basicAccurate(image_baidu)
        print(result + "\n----------")
        print(result2)
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        result_four = resultj[0:4]  # 只获取前4个字符
        print(result_four)  # 打印识别的验证码
        return result_four

    def teardown(self):
        sleep(20)
        self.driver.quit()
