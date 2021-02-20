# 导包
from selenium import webdriver


def open_browser(browser_type):
    if browser_type == 'chrome':
        driver = webdriver.Chrome()
        return driver
    elif browser_type == 'firefox':
        driver = webdriver.Firefox()
        return driver
    else:
        print('type error')


class TestKeywords(object):
    # 调用浏览器
    def __init__(self, url, browser_type):
        self.driver = open_browser(browser_type)
        self.driver.get(url)

    # 元素定位
    def locator(self, locator_type, value):
        if locator_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
            return el
        elif locator_type == 'id':
            el = self.driver.find_element_by_id(value)
            return el
        elif locator_type == 'name ':
            el = self.driver.find_element_by_name(value)
            return el

    # 输入
    def input_text(self, locator_type, value, text):
        self.locator(locator_type, value).send_keys(text)

    # 点击
    def click_element(self, locator_type, value):
        self.locator(locator_type, value).click()

    # 关闭浏览器，释放资源
    def quit_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    tk = TestKeywords('https://www.baidu.com/', 'chrome')
    tk.input_text('id', 'kw', '自动化测试')
    tk.click_element('id', 'su')
