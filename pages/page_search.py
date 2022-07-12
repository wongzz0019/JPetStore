import allure

from common.base import Base


class Search(Base):

    # @allure.step('搜索文本框输入')
    # def find_keyword(self):
    #     return self.by_css_selector("input[name='keyword']")
    #
    # @allure.step('点击搜索按钮')
    # def find_search(self):
    #     return self.by_css_selector("input[value='Search']")

    @allure.step('返回主菜单')
    def find_main_menu(self):
        return self.by_link_text('Return to Main Menu')

    @allure.step('搜索结果 -- 断言宠物名称')
    def find_product_name(self):
        return self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[2]/td[3]').text
