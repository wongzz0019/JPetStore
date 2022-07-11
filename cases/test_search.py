import os
from time import sleep

import allure
import pytest

from common.load_yaml import load_yaml
from pages.page_search import Search


@allure.feature('商品查询')
class TestSearch():

    @allure.title('商品查询成功')
    @allure.story('商品查询成功')
    @pytest.mark.parametrize('data', load_yaml('../data/search.yaml'))
    def test_search(self, data):
        search = Search()
        search.open_url('https://petstore.octoperf.com/actions/Catalog.action')
        search.find_keyword().send_keys(data['name'])
        # sleep(2)
        search.find_search().click()
        assert str(data['name']) == search.find_product_name()
        search.close()


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_search.py', '--clean-alluredir', '--alluredir=allure-results'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    os.system(r"allure generate -c -o ../allure-report")