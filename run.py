# 生成测试报告  allure测试报告
# 1.pip install allure-pytest
# 2.在github上下载allure包，放到python安装路劲下
# 3.配置allure环境变量， F:\Python39\Lib\site-packages\allure-2.18.1\bin
import os

import pytest

if __name__ == '__main__':
    # 执行测试用例获得测试数据
    # 输出信息，测试用例路径，测试数据目录(--alluredir)，数据路径（./allure-results）
    pytest.main(['-s', '-v', './cases/test_search.py', '--clean-alluredir', '--alluredir=allure-results'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    os.system(r"allure generate -c -o allure-report")
