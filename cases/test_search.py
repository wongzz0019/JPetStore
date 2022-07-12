import os
from time import sleep

import allure
import pytest

from common import driver
from common.load_yaml import load_yaml
from pages.page_index import Index
from pages.page_search import Search


@allure.feature('商品查询')
class TestSearch():

    def setup_class(self):
        self.driver = driver.Driver()
        self.driver.get_driver()
        self.index = Index()
        self.search = Search()

    def teardown_class(self):
        self.driver.quit_driver()

    @allure.title('商品查询成功')
    @allure.story('商品查询成功')
    @pytest.mark.parametrize('data', load_yaml('../data/search.yaml'))
    def test_search(self, data):

        self.index.find_keyword().clear()
        self.index.find_keyword().send_keys(data['name'])
        # sleep(2)
        self.index.find_search().click()
        assert str(data['name']) == self.search.find_product_name()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_search.py', '--clean-alluredir', '--alluredir=allure-results'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    os.system(r"allure generate -c -o ../allure-report")