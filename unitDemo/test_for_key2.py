# 测试用例方法必须以test_开头
import unittest
from time import sleep
from web_ui.WebUIDemo import TestKeywords
from ddt import ddt, data, unpack


@ddt
class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.tk = TestKeywords('http://www.baidu.com', 'chrome')

    # 后置条件
    def tearDown(self) -> None:
        self.tk.quit_browser()

    # 测试用例
    # *表示基于元组的形式进行处理，**表示字典，基于键值对的形式去获取
    @data(['id', '战锤30k'], ['id', '战锤40k'])
    @unpack
    def test_1(self, locator, input_value):
        self.tk.input_text(locator, 'kw', input_value)
        self.tk.click_element('id', 'su')
        sleep(3)


if __name__ == '__main__':
    unittest.main()
