from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.driver import Driver


class Base():
    def __init__(self):
        # self.driver = webdriver.Chrome()  #type:# webdriver
        self.driver = Driver().get_driver()

    # name定位
    def by_name(self, elem):
        return self.driver.find_element(By.NAME, elem)

    # 类名定位
    def by_class_name(self, elem):
        return self.driver.find_element(By.CLASS_NAME, elem)

    # xpath定位
    def by_xpath(self, elem):
        return self.driver.find_element(By.XPATH, elem)

    def by_xpaths(self, elem):
        return self.driver.find_elements(By.XPATH, elem)

    # id定位
    def by_id(self, elem):
        return self.driver.find_element(By.ID, elem)

    # 绝对文本定位
    def by_link_text(self, elem):
        return self.driver.find_element(By.LINK_TEXT, elem)

    # 包含文本定位
    def by_partial_link_text(self, elem):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, elem)

    # css定位
    def by_css_selector(self, elem):
        return self.driver.find_element(By.CSS_SELECTOR, elem)

    def by_css_selectors(self, elem):
        return self.driver.find_elements(By.CSS_SELECTOR, elem)

    # def open_url(self, url):
    #     self.driver.get(url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #
    # def close(self):
    #     # sleep(3)
    #     self.driver.quit()
    #     self.driver = None



