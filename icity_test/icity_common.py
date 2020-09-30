# -*- encoding=utf8 -*-
__author__ = "Administrator"

import re
import time
import datetime
# from airtest.core.helper import device_platform, logwrap, log, task_log
from airtest.core.helper import device_platform, logwrap, log
from airtest.core.android.android import *
from airtest.core.api import *
from poco.exceptions import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(
    use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


def hyper_assert(condition, assert_content):
    """
    @Pramas1:  condition
    @Pramas2:  assert_content
    @Return  Void But it will Snapshot the device screen
    """
    print(condition)
    try:
        assert condition, assert_content
        snapshot(msg=assert_content)
        log(assert_content, None)
    except:
        import traceback
        snapshot(msg=assert_content + "-未找到")
        log('', traceback.format_exc())


@logwrap
def back_click():
    """
      Common Back func
    """
    if poco(textMatches="^.*arrow_left").exists():
        poco(textMatches="^.*arrow_left").click()
    else:
        keyevent("BACK")


@logwrap
def find_appname(name):
    """
      Find the app name
      @params: name -> app_name
    """
    isGuide = True
    num = 0
    while (isGuide):

        if poco(text=name).exists():
            poco(text=name).click()
            break
        elif (num > 3):

            raise PocoNoSuchNodeException("未找到%s" % name)
        elif poco(text="其他服务").exists():
            poco.swipe([0.5, 0.8], [0.5, 0.4])
            time.sleep(1)

            num = num + 1
        else:
            poco.swipe([0.5, 0.8], [0.5, 0.4])
            time.sleep(1)


@logwrap
def loading_more():
    """
      Loading More things
    """
    poco.swipe([0.5, 0.6], [0.5, 0.3])
    isGuide = True
    while (isGuide):

        if poco(text="更多").exists():
            poco(text="更多").click()
            break
        else:
            poco(
                "com.inspur.icity.icityapp:id/recycler_core_operation").swipe([-1, 0])


@logwrap
def enter_module(name):
    """ 
      Enter to module app 
      @params: name -> app_name
    """
    loading_more()
    time.sleep(3)
    find_appname(name)
    # poco.wait_for_all([poco(textMatches="^.*{}.*$".format(name))])


@logwrap
def h5_search_func(text_str):
    """
      Do H5 Search 
      @params: text -> seach text
    """
    if poco("i-search-do").exists():
        poco("i-search-do").click()
    if poco("i-search-input").exists():
        poco("i-search-input").click()
    text(text_str, enter=True, search=True)


@logwrap
def init_app(package):
    """
      Init app 
      @params: package -> package name
    """
    stop_app(package)
    clear_app(package)
    start_app(package)
    time.sleep(1)
    isGuide = True
    while (isGuide):
        if poco(text="首页").exists():
            if poco(textMatches="^.*允许.*$", touchable=True).exists():
                poco(textMatches="^.*允许.*$", touchable=True).click()
                break
            else:
                return
        elif poco(textMatches="^.*不再询问.*$").exists():
            poco(textMatches="^.*允许.*$", touchable=True).click()
        elif poco(text="我知道了").exists():
            poco(text="我知道了").click()
        elif poco(textMatches="^.*允许.*$", touchable=True).exists():
            poco(textMatches="^.*允许.*$", touchable=True).click()
        elif poco(textMatches="^.*确定.*$", touchable=True).exists():
            poco(textMatches="^.*确定.*$", touchable=True).click()
        elif poco(touchable=True).exists():
            poco(touchable=True).click()
        else:
            poco.swipe([0.9, 0.5], [0.1, 0.5], duration=0.3)


@logwrap
def is_login(username, password):
    """
      Logging Function
      @params: username
      @params: password
    """
    if poco(text="立即登录").exists():
        poco(text="立即登录").click()
        sleep(2)
        if existed_click("其他方式登录"):
            if existed_click("请输入手机号"):
                back_click()
                existed_click("密码登录")
                poco(text="请输入手机号/城市号").set_text(username)
                poco("com.inspur.icity.icityapp:id/et_pwd").set_text(password)
                poco(text="登录").click()
                sleep(3)
                if poco(text="跳过").exists():
                    poco(text="跳过").click()
            else:
                raise Exception("Not found 请输入手机号")
        else:
            if existed_click("请输入手机号"):
                back_click()
                existed_click("密码登录")
                poco(text="请输入手机号/城市号").set_text(username)
                poco("com.inspur.icity.icityapp:id/et_pwd").set_text(password)
                poco(text="登录").click()
                sleep(3)
                if poco(text="跳过").exists():
                    poco(text="跳过").click()
            else:
                raise Exception("Not found 请输入手机号")
    elif poco(text="登录看看").exists():
        poco(text="登录看看").click()
        existed_click("请输入手机号")
        back_click()
        existed_click("密码登录")
        poco(text="请输入手机号/城市号").set_text(username)
        poco("com.inspur.icity.icityapp:id/et_pwd").set_text(password)
        poco(text="登录").click()
        poco(text="跳过").exists()
        poco(text="跳过").click()
    elif poco(text="其他方式登录").exists():
        poco(text="其他方式登录").click()
        existed_click("请输入手机号")
        back_click()
        existed_click("密码登录")
        poco(text="请输入手机号/城市号").set_text(username)
        poco("com.inspur.icity.icityapp:id/et_pwd").set_text(password)
        poco(text="登录").click()
    elif poco(text="获取验证码").exists():
        if existed_click("请输入手机号"):
            back_click()
            existed_click("密码登录")
            poco(text="请输入手机号/城市号").set_text(username)
            poco("com.inspur.icity.icityapp:id/et_pwd").set_text(password)
            poco(text="登录").click()
            sleep(3)
            if poco(text="跳过").exists():
                poco(text="跳过").click()
        else:
            raise Exception("Not found 请输入手机号")
    else:
        print("已登录")


@logwrap
def enter_mine():
    isGuide = True
    while (isGuide):
        if poco(text="我的").exists():
            poco(text="我的").click()
            isGuide = False
            break
        else:
            back_click()
            time.sleep(2)


@logwrap
def enter_home():
    isGuide = True
    while (isGuide):
        if poco("com.inspur.icity.icityapp:id/image_home").exists():
            poco("com.inspur.icity.icityapp:id/image_home").click()
            isGuide = False
            #             poco.swipe([0.5,0.2],[0.5,0.8])
            break
        else:
            back_click()
            time.sleep(2)


@logwrap
def logout():
    enter_mine()
    poco(textMatches="^.*设置.*$").click()
    poco(textMatches="^.*退出登录.*$").click()
    time.sleep(1)
    poco(textMatches="^.*确定.*$", touchable=True).click()
    time.sleep(3)
    enter_home()


@logwrap
def open_gps3rd(nav):
    """
      Open Nav Map
      @params: nav 
    """
    if poco(textMatches="^.*{}".format(nav)).exists():
        poco(textMatches="^.*{}".format(nav)).click()

        if poco(textMatches="高德.*$").exists():
            poco(textMatches="高德.*$").click()
        elif poco(textMatches="百度.*$").exists():
            poco(textMatches="百度.*$").click()
        elif poco(textMatches="腾讯.*$").exists():
            poco(textMatches="腾讯.*$").click()
        else:
            print("[ERROR]未找到第三方导航")
    else:
        print("[ERROR]未找到打开导航按钮")
    return


@logwrap
def real_name(real_name, idCard, mobile_phone):
    """
      RealName verify 
      @params: real_name
      @params: idCard
      @params: mobile_phone
    """
    poco("com.inspur.icity.icityapp:id/et_name").click()
    poco("com.inspur.icity.icityapp:id/et_name").set_text(real_name)
    poco("com.inspur.icity.icityapp:id/et_idcard").click()
    poco("com.inspur.icity.icityapp:id/et_idcard").set_text(idCard)
    assert_equal(poco("com.inspur.icity.icityapp:id/et_phone").get_text(),
                 mobile_phone, "验证手机号是否一致")
    poco(text="提交", touchable=True).click()


@logwrap
def select_station(province, city=""):
    """
    Select Station 
    @params: province  
    @params: city
    """
    #     existed_click('我的')
    enter_mine()
    existed_click('设置')
    poco.wait_for_all([poco(text="城市选择")])
    if (city != ""):
        if (poco("com.inspur.icity.icityapp:id/tv_setting_verify_name").get_text() == city):
            enter_home()
            return
    else:
        if (poco("com.inspur.icity.icityapp:id/tv_setting_verify_name").get_text() == province):
            enter_home()
            return
    existed_click('城市选择')
    sleep(3)
    poco(text=province).click()
    if (city != ""):
        poco(text=city).click()


@logwrap
def wait_click(node_name, timeout=10, regx=1):
    """
    Wait Click
    @params:  node_name 
    @params:  timeout
    @params:  regx  0 不用正则  1 使用正则
    @return True / False
    """
    if regx == 1:
        obj = poco(textMatches="^.*{}.*$".format(node_name))
    elif regx == 0:
        obj = poco(text=node_name)
    try:
        if poco.wait_for_all(objects=[obj], timeout=timeout):
            obj.click()
            snapshot(msg="成功点击")
            return True
    except PocoTargetTimeout:
        snapshot(msg="Not Found the node name: %s" % node_name)
        return False


@logwrap
def existed_click(node_name, timeout=1, regx=1):
    """
    exited Click
    @params:  node 
    @params:  regx  0 不用正则  1 使用正则  2 匹配换行 
    @return  True / False
    """
    if regx == 1:
        obj = poco(textMatches="^.*{}.*$".format(node_name))
    elif regx == 2:
        obj = poco(textMatches="\s+{}\s+".format(node_name))
    elif regx == 0:
        obj = poco(text=node_name)
    if obj.exists():
        obj.wait(timeout).click()
        snapshot(msg="成功点击")
        return True
    else:
        snapshot(msg="Not Found the node name: %s" % node_name)
        return False


@logwrap
def photo_select(count=1, max_count=4):
    """
    Photo Select
    @params:  count  选择个数 
    """
    items = poco(
        "com.inspur.icity.icityapp:id/rv_photos").child("android.widget.RelativeLayout")
    for i in range(count):
        items[i].click()
        if i + 1 == max_count + 1:
            snapshot(msg="最多选择4张图片")
    existed_click("完成")


@logwrap
def share(share_name):
    """
    Share Select
    @params:  count  选择个数 
    """
    if not poco("com.inspur.icity.icityapp:id/iv_isShare").exists():
        snapshot(msg="[ERROR]未找到分享按钮")
    poco("com.inspur.icity.icityapp:id/iv_isShare").click()
    existed_click(share_name)


@logwrap
def next_node_click(node_text, childName="android.view.View"):
    """
    Upload Method 2
    @params:  node_text  label name
    @params:  childName  childName
    """

    pattern = re.compile("^.*{}.*$".format(node_text))
    items = poco("app").child(childName)
    items = poco("android.widget.LinearLayout").offspring(
        "app").child(childName)
    click_obj = None
    for i in range(len(items)):
        ok = re.match(pattern, items[i].get_text())
        if ok is not None:
            click_obj = items[i - 1]
            break
    if click_obj:
        click_obj.click()
        snapshot(msg="成功点击")
        return True
    else:
        snapshot(msg="未找到%s" % node_text)
        return False


@logwrap
def wait_loadding(obj, info):
    """ 
    wait loadding 等待出现
    @params: obj   定位点
    @params: info  截图信息
    @return：True 出现了  False 未找到
    """
    count = 0
    while not obj.exists():
        try:
            obj.wait_for_appearance()
        except:
            snapshot(msg=info)
        count += 1

        while count > 10:
            snapshot(msg="加载超时!")
            return False
    return True


def count_time(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()
        func()
        over_time = datetime.datetime.now()
        total_time = (over_time - start_time).total_seconds()
        print('程序共计%s秒' % total_time)
        snapshot(msg='步骤共计%s秒' % total_time)

    return int_time


@logwrap
def v_swipe(up: float, down: float, x=0.5):
    """ 
    垂直滑动 
    @params: up    滑动起始点
    @params: down  滑动终止点
    @return：True 完成  False 出错
    """
    start_pos = [x, up]
    end_pos = [x, down]
    try:
        poco.swipe(start_pos, end_pos)
        snapshot(msg="滑动截图")
        return True
    except:
        return False


@logwrap
def h_swipe(left: float, right: float, y=0.5):
    """ 
    水平滑动 
    @params: left    滑动起始点
    @params: right   滑动终止点
    @return：True 完成  False 出错
    """
    start_pos = [left, y]
    end_pos = [right, y]
    try:
        poco.swipe(start_pos, end_pos)
        snapshot(msg="滑动截图")
        return True
    except:
        return False


def TestPoint(arg):
    def _TestPoint(func):
        def __TestPoint():
            func()
            # task_log(arg)

        return __TestPoint

    return _TestPoint


@logwrap
def getIngrachNum(appId, event, segmentation=""):
    year = datetime.datetime.now().strftime("%Y")
    apiKey = "58cb40dad32709bb2680b419c7b7870e"
    url = "https://ingrach.icity24.cn/o?api_key=" + apiKey + "&app_id=" + appId + "&method=events&event=" + event + "&segmentation=" + segmentation + "&period=1days"
    r = requests.get(url)
    resbody = r.json()
    # print(resbody)
    if resbody.get(year) != None:
        # print(resbody.get(year).get("click") )
        if resbody.get(year).get("click") != None:
            return resbody.get(year).get("click").get("c")
        else:
            return resbody.get(year).get("c")
    else:
        return 0
