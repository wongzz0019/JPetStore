import os
import time

import allure
import pytest

from common import driver
from common.driver import Driver
from common.load_yaml import load_yaml
from pages.page_login import Login


@allure.feature('登录')
class Test_Login():

    def setup_class(self):
        self.driver = driver.Driver()
        self.driver.get_driver()
        self.login = Login()

    def teardown_class(self):
        self.driver.quit_driver()

    @allure.title('登录商品网站')
    @pytest.mark.parametrize('data', load_yaml('../data/login.yaml'))
    def test_login(self, data):
        self.login.login(data['username'], data['pwd'])
        print(time.thread_time())


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py', '--clean-alluredir', '--alluredir=allure-results'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    os.system(r"allure generate -c -o allure-report")
