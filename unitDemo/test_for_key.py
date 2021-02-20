# 测试用例方法必须以test_开头
import unittest
from time import sleep
from web_ui.WebUIDemo import TestKeywords


class TestForKey(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.tk = TestKeywords('http://www.baidu.com', 'chrome')

    # 后置条件
    def tearDown(self) -> None:
        self.tk.quit_browser()

    # 测试用例1
    def test_1(self):
        self.tk.input_text('id', 'kw', '战锤30k')
        self.tk.click_element('id', 'su')
        sleep(3)

    # 测试用例2
    def test_2(self):
        self.tk.input_text('id', 'kw', '战锤40k')
        self.tk.click_element('id', 'su')
        sleep(3)


if __name__ == '__main__':
    unittest.main()
