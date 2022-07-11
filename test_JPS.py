import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base import Base


class TestJSP(object):

    def test_one(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=REPTILES')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        text = self.driver.find_element(By.XPATH, '//*[@id="Catalog"]/table/tbody/tr[2]/td[2]').text
        print(text)
    #
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://petstore.octoperf.com/actions/Catalog.action')
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(3)
    #
    # def teardown(self):
    #     sleep(3)
    #     self.driver.quit()
    #
    # # def teardown_class(self):
    # #     sleep(3)
    # #     self.driver.quit()
    #
    #
    #
    # # 注册
    # def test_register(self):
    #     self.driver.find_element(By.LINK_TEXT, 'Sign In').click()
    #     self.driver.find_element(By.LINK_TEXT, 'Register Now!').click()
    #     # UserID
    #     self.driver.find_element(By.NAME, 'username').send_keys('a22111')
    #     # New password:
    #     self.driver.find_element(By.NAME, 'password').send_keys('123456')
    #     # Repeat password:
    #     self.driver.find_element(By.NAME, 'repeatedPassword').send_keys('123456')
    #     # First name
    #     self.driver.find_element(By.NAME, 'account.firstName').send_keys('一凡')
    #     # Last name:
    #     self.driver.find_element(By.NAME, 'account.lastName').send_keys('五')
    #     sleep(2)
    #     # Email:
    #     self.driver.find_element(By.NAME, 'account.email').send_keys('12367@163.com')
    #     # Phone:
    #     self.driver.find_element(By.NAME, 'account.phone').send_keys('11234456')
    #     # Address 1
    #     self.driver.find_element(By.NAME, 'account.address1').send_keys('中国香港')
    #     # Address 2
    #     self.driver.find_element(By.NAME, 'account.address2').send_keys('中国台湾市')
    #     # City:
    #     self.driver.find_element(By.NAME, 'account.city').send_keys('中国')
    #     # State
    #     self.driver.find_element(By.NAME, 'account.state').send_keys(200)
    #     # Zip:
    #     self.driver.find_element(By.NAME, 'account.zip').send_keys('NO')
    #     # Country:
    #     self.driver.find_element(By.NAME, 'account.country').send_keys('China')
    #     sleep(2)
    #     # Language Preference
    #     element = self.driver.find_element(By.NAME, 'account.languagePreference')
    #     select = Select(element)
    #     select.select_by_value('japanese')
    #     # Favourite Category:
    #     element = self.driver.find_element(By.NAME, 'account.favouriteCategoryId')
    #     select = Select(element)
    #     select.select_by_value('CATS')
    #     sleep(2)
    #     # Enable MyList
    #     self.driver.find_element(By.NAME, 'account.listOption').click()
    #     # Enable MyBanner
    #     self.driver.find_element(By.NAME, 'account.bannerOption')
    #     sleep(2)
    #     # Save
    #     self.driver.find_element(By.NAME, 'newAccount').click()
    #
    # # 登录
    # def test_login(self):
    #     # 进入登录页
    #     self.driver.find_element(By.LINK_TEXT, 'Sign In').click()
    #     # Username
    #     self.driver.find_element(By.NAME, 'username').clear()
    #     self.driver.find_element(By.NAME, 'username').send_keys('a22111')
    #     # Password
    #     self.driver.find_element(By.NAME, 'password').clear()
    #     self.driver.find_element(By.NAME, 'password').send_keys('123456')
    #     sleep(2)
    #     # submit
    #     self.driver.find_element(By.NAME, 'signon').click()
    #     sleep(2)

if __name__ == '__main__':
    pytest.main(['-sv', 'test_JPS.py'])
