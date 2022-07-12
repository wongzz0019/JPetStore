import os
from time import sleep

import allure
import pytest

from common import driver
from pages.page_buy import Buy
from pages.page_index import Index
from pages.page_login import Login


@allure.feature('购买')
class TestBuy():

    def setup_class(self):
        self.driver = driver.Driver()
        self.driver.get_driver()
        self.login = Login()
        self.buy = Buy()
        self.index = Index()

    def teardown_class(self):
        self.driver.quit_driver()

    @allure.title('成功购买')
    @allure.story('登录购买商品')
    def test_buy(self):
        # 登录
        self.index.find_sign_in().click()
        self.login.find_username().send_keys('a333333')
        self.login.find_pwd().clear()
        self.login.find_pwd().send_keys('333333')
        self.login.find_submit().click()
        # 选商品
        self.index.find_pet('BIRDS').click()
        sleep(2)
        self.buy.find_product_id('AV-CB-01').click()
        # 加购物车
        self.buy.find_add_cart('EST-18').click()
        # 数量选择
        self.buy.find_quantity('EST-18').clear()
        self.buy.find_quantity('EST-18').send_keys(4)
        # 更新
        self.buy.find_update_cart().click()
        sleep(2)
        # 结账、
        self.buy.find_proceed_to_checkout().click()
        self.buy.find_neworder().click()
        # 订单信息
        bill_addr_text = self.buy.find_bill_addr_text()
        print(bill_addr_text)
        self.buy.find_confirm().click()
        sleep(2)
        # 获取购买成功提示信息
        message = self.buy.find_messages().text
        assert message == 'Thank you, your order has been submitted.'


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_buy.py', '--clean-alluredir', '--alluredir=allure-results'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    os.system(r"allure generate -c -o allure-report")
