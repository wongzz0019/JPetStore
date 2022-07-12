import time
from time import sleep

import pytest

from common import driver
from common.load_yaml import load_yaml
from pages.page_index import Index
from pages.page_login import Login
from pages.page_register import Register


class TestRegister():
    def setup_class(self):
        self.driver = driver.Driver()
        self.driver.get_driver()
        self.login = Login()
        self.index = Index()
        self.register = Register()

    def teardown_class(self):
        self.driver.quit_driver()

    @pytest.mark.parametrize('data', load_yaml('../data/register.yaml'))
    def test_register(self, data):
        # 进入注册页面
        self.index.find_sign_in().click()
        self.login.find_register().click()

        # 文本框输入
        self.register.find_userid().send_keys(data['username'])
        self.register.find_pwd().send_keys(data['pwd'])
        self.register.find_rpwd().send_keys(data['rpwd'])
        self.register.find_firstname().send_keys(data['fname'])
        self.register.find_lastname().send_keys(data['lname'])
        self.register.find_email().send_keys(data['email'])
        self.register.find_phone().send_keys(data['phone'])
        sleep(2)
        self.register.find_address1().send_keys(data['addr1'])
        self.register.find_address2().send_keys(data['addr2'])
        self.register.find_city().send_keys(data['city'])
        self.register.find_state().send_keys(data['state'])
        self.register.find_zip().send_keys(data['zipp'])
        self.register.find_country().send_keys(data['country'])
        sleep(2)

        # 下拉框
        self.register.find_language().select_by_value(data['language'])
        self.register.find_favourite().select_by_value(data['favourite'])

        # 复选框
        if data['mylist'] == 'y':
            self.register.find_mylist().click()
        if data['banner'] == 'y':
            self.register.find_mybanner().click()
        sleep(2)

        # 注册保存
        self.register.find_save().click()


if __name__ == '__main__':
    pytest.main(['-sv', 'test_register.py'])
