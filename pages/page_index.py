import allure

from common.base import Base


class Index(Base):

    @allure.step('购物车')
    def find_cart(self):
        return self.by_css_selector("img[name='img_cart']")

    @allure.step('登录')
    def find_sign_in(self):
        return self.by_link_text('Sign In')

    @allure.step('帮助')
    def find_help(self):
        return self.by_css_selector("a[href*='help.html']")

    @allure.step('搜索文本框')
    def find_keyword(self):
        return self.by_css_selector("input[name='keyword']")

    @allure.step('搜索按钮')
    def find_search(self):
        return self.by_css_selector("input[value='Search']")

    # FISH; DOGS; REPTILES; CATS; BIRDS
    @allure.step('宠物种类')
    def find_pet(self, pet):
        return self.by_css_selector("a[href$='{}']".format(pet))
