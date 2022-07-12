import os
from time import sleep

import pytest

from common.driver import Driver
from pages.page_index import Index
from pages.page_login import Login
from pages.page_my_account import MyAccount
from pages.page_my_orders import Orders


class TestAccount():

    def setup_class(self):
        self.driver = Driver()
        self.driver.get_driver()
        self.index = Index()
        self.login = Login()
        self.account = MyAccount()
        self.orders = Orders()

    def teardown_class(self):
        self.driver.quit_driver()

    def test_select_orders(self):
        # 打开网址并登录
        self.index.find_sign_in().click()
        self.login.find_username().send_keys('a333333')
        self.login.find_pwd().clear()
        self.login.find_pwd().send_keys('333333')
        self.login.find_submit().click()
        # 进入我的账户
        self.account.find_my_account().click()
        # 进入订单列表
        sleep(2)
        self.account.find_orders().click()
        # 获取所有订单ID及金额，并对应打印出来
        self.order_id = self.orders.find_order_id()
        self.order_price = self.orders.find_price()
        id_price = dict(zip(self.order_id, self.order_price))
        print(id_price)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_account.py', '--clean-alluredir', '--alluredir=allure-results'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    os.system(r"allure generate -c -o allure-report")
