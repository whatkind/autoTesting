# coding:utf-8
from Base.base_page import *
from selenium.webdriver.common.by import By
from selenium import webdriver


class SearchPage(BasePage):
    # 定义一个id = kw的元素
    input_id = (By.ID, 'kw')  # 元组数据类型
    click_id = (By.ID, 'su')

    # 定位搜索内容的填入
    def input_text(self, content):
        self.locator_element(*self.input_id).send_keys(content)

    # 定位百度一下按钮，点击次
    def click_element(self):
        self.locator_element(*self.click_id).click()

    def search_content(self, content):
        self.open()
        self.input_text(content)
        self.click_element()
        self.quit()


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    content = '战锤40k'
    driver = webdriver.Chrome()
    sp = SearchPage(driver, url)
    sp.search_content(content)
