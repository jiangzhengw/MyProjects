import unittest


# test fixture : 测试装置执行的流程

# 1.setUp
# 每个测试用例执行之前会执行
# 2.setUpClass
# 在每个测试类执行之前运行
# 3.setUpMidule
# 解决每个测试类开启关闭文件的问题
# 在所有测试类在调用之前会被执行一次,函数名是固定写法,会被unittest等框架自动识别

# test case : 测试用例
# test suite :
# test runner :

class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass.pr")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")

    # unittest测试用例命名test_XXX
    # 不需要参数就被认为是测试用例
    def test_sum(self):
        print("test_sum")
        x = 1 + 2
        # x.print，ide快捷生成print语句
        print(x)
        self.assertEqual(3, x, f'x={x} exception=3')


# 使终端窗口中的（python）中可以执行测试用例
if __name__ == '__main__':
    unittest.main()

# 菜单栏code-reformat code 快捷键ctrl+alt+L格式化python代码
