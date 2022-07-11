import allure
from selenium.webdriver.support.select import Select

from common.base import Base


class MyAccount(Base):

    @allure.step('进入我的账户')
    def find_my_account(self):
        return self.by_link_text('My Account')

    @allure.step('修改-用户信息-新密码')
    def find_new_pwd(self):
        return self.by_css_selector("input[id='stripes--1437546547']")

    @allure.step('修改-用户信息-确认新密码')
    def find_repeat_pwd(self):
        return self.by_css_selector("input[name='repeatedPassword']")

    @allure.step('修改-账户信息-姓')
    def find_fname(self):
        return self.by_name('account.firstName')

    @allure.step('修改-账户信息-名')
    def find_lname(self):
        return self.by_name('account.account.lastName')

    @allure.step('修改-账户信息-邮箱')
    def find_email(self):
        return self.by_name('account.email')

    @allure.step('修改-账户信息-手机号码')
    def find_phone(self):
        return self.by_css_selector("input[name='account.phone']")

    @allure.step('修改-账户信息-地址一')
    def find_addr1(self):
        return self.by_css_selector("input[name='account.address1']")

    @allure.step('修改-账户信息-地址二')
    def find_addr2(self):
        return self.by_css_selector("input[name='account.address2']")

    @allure.step('修改-账户信息-城市')
    def find_city(self):
        return self.by_css_selector("input[name='account.city']")

    @allure.step('修改-账户信息-状态')
    def find_state(self):
        return self.by_css_selector("input[name='account.state']")

    @allure.step('修改-账户信息-国家')
    def find_country(self):
        return self.by_css_selector("input[name='account.country']")

    @allure.step('下拉框选择-个人资料-语言')
    def find_language(self, language):
        return Select(self.by_css_selector("select[name='account.languagePreference']")).select_by_value(language)

    @allure.step('下拉框选择-个人资料-喜爱类别')
    def find_category(self, Category):
        return Select(self.by_css_selector("select[name='account.favouriteCategoryId']")).select_by_value(Category)

    @allure.step('复选-账户信息-我的列表')
    def find_mylist(self):
        return self.by_css_selector("input[name='account.listOption']")

    @allure.step('复选-账户信息-我的横幅')
    def find_mybanner(self):
        return self.by_css_selector("input[name='account.bannerOption']")

    @allure.step('点击-保存')
    def find_save(self):
        return self.by_css_selector("input[name='editAccount']")

    @allure.step('点击-我的订单')
    def find_orders(self):
        return self.by_link_text('My Orders')

