import unittest
from PageObject.search import *
from ddt import ddt, data


@ddt
class pageObjectUnit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.sp.quit()

    @data("https://www.baidu.com")
    def test_a(self, url):
        self.sp = SearchPage(self.driver, url)
        self.sp.search_content('战锤40k')


if __name__ == '__main__':
    unittest.main()
