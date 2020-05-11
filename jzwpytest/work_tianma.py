import os
import time
import allure
import pytest

# 能够正常返回结果的类似整数测试数据,数据格式(预期值，a,b,标题)
data_int = [
    (5, 10, 2, '正常整数'),
    (1024, 4294967296, 4194304, '大数值整数'),
    (-6.25, -25, 4, '含负数整数'),
    (0, 0, 999999, '被除数为0整数'),
    (1.25 - 0.25j, 3 + 2j, 2 + 2j, '复数数据')
]

# 能够正常返回结果的类似浮点数测试数据,数据格式(预期值，a,b,精度,标题)
data_float = [
    (5, 10.5, 2.1, 0, '返回值为整数的浮点数'),
    (3.38709677, 10.5, 3.1, 0.00000001, '返回值为无限位浮点数的浮点数'),
    (3.6, 7.92, 2.2, 0.00000001, '返回值为有限位浮点数的浮点数'),
    (10, 10, True, 0, '布尔数据-True'),
    (121.91780821, 89e-5, 73e-7, 1e-8, '科学计数法数据')
]

# 不能正常返回结果，预期会报错的测试数据,数据格式(预期错误，a,b,标题)
data_error = [
    ('ZeroDivisionError', 10, 0, '除数为零报错'),
    ('TypeError', 10, {1, 2}, '集合数据'),
    ('TypeError', 10, {1: 2}, '字典数据'),
    ('TypeError', 10, (1, 2), '元祖数据'),
    ('TypeError', 10, [1], '列表数据'),
    ('TypeError', 10, 'a', '字符串数据'),
    ('ZeroDivisionError', 10, False, '布尔数据-False')
]


# 待测功能
def div(a, b):
    return a / b


# 预期正常返回结果的int测试用例
@allure.suite('整数数据组')
@allure.title('{title}')
@pytest.mark.parametrize('expected,a,b,title', data_int)
def test_int_div(expected, a, b, title):
    assert expected == div(a, b)


# 预期正常返回结果的float测试用例
@allure.suite('浮点数数据组')
@allure.title('{title}')
@pytest.mark.parametrize('expected,a,b,precision,title', data_float)
def test_float_div(expected, a, b, precision, title):
    # python abs() :  函数返回数字的绝对值
    # assert precision >= abs(div(a, b) - expected)  # 浮点数按照精度判断
    assert pytest.approx(expected) == div(a, b)  # pytest提供的近似判断方法(默认精度1e-6)

# 预期会报错的测试用例
@allure.suite('报错数据组')
@allure.title('{title}')
@pytest.mark.parametrize('expected,a,b,title', data_error)
def test_error_div(expected, a, b, title):
    # python eval()
    with pytest.raises(eval(expected)):
        div(a, b)


# 进行旧测试数据的清理，测试报告的生成和展示
if __name__ == "__main__":
    print(__file__)
    # print("-------------------------------12222222222")
    # 清空allure_results文件夹，清理掉allure历史记录
    path = "jzwpytest/allure_results"
    # os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
    for i in os.listdir(path):
        if os.listdir(path) != "":
            os.remove('{a}/{b}'.format(a=path, b=i))
    time.sleep(1)

    # 执行测试并保存allure需要的结果,pytest -v 显示每条用例的执行结果
    os.system('pytest -v --alluredir=jzwpytest/allure_results {}'.format(__file__))
    time.sleep(1)

    # 使用allure展示测试报告
    os.system(r'allure serve jzwpytest\allure_results')

    # 自动退出allure报告模式,待实现
    # os.system('')
