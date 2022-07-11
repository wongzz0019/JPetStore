import time
from time import sleep

import pytest

from common.load_yaml import load_yaml
from pages.page_register import Register


class TestRegister():

    @pytest.mark.parametrize('data', load_yaml('../data/register.yaml'))
    def test_register(self, data):
        register = Register()

        # 进入相关页面
        register.open('https://petstore.octoperf.com/actions/Catalog.action')
        register.find_sign_in().click()
        register.find_register().click()

        # 文本框输入
        register.find_userid().send_keys(data['username'])
        register.find_pwd().send_keys(data['pwd'])
        register.find_rpwd().send_keys(data['rpwd'])
        register.find_firstname().send_keys(data['fname'])
        register.find_lastname().send_keys(data['lname'])
        register.find_email().send_keys(data['email'])
        register.find_phone().send_keys(data['phone'])
        sleep(2)
        register.find_address1().send_keys(data['addr1'])
        register.find_address2().send_keys(data['addr2'])
        register.find_city().send_keys(data['city'])
        register.find_state().send_keys(data['state'])
        register.find_zip().send_keys(data['zipp'])
        register.find_country().send_keys(data['country'])
        sleep(2)

        # 下拉框
        register.find_language().select_by_value(data['language'])
        register.find_favourite().select_by_value(data['favourite'])

        # 复选框
        if data['mylist'] == 'y':
            register.find_mylist().click()
        if data['banner'] == 'y':
            register.find_mybanner().click()
        sleep(2)

        # 注册保存
        register.find_save().click()
        print(time.localtime())
        register.close()


if __name__ == '__main__':
    pytest.main(['-sv', 'test_register.py'])
