from time import sleep

import allure

from common.base import Base


class Login(Base):

    @allure.step('输入username')
    def find_username(self):
        return self.by_name('username')

    @allure.step('输入pwd')
    def find_pwd(self):
        return self.by_name('password')

    @allure.step('点击登录按钮')
    def find_submit(self):
        return self.by_name('signon')

    @allure.step('进入注册面')
    def find_register(self):
        return self.by_link_text('Register Now!')

    @allure.step('点击退出登录')
    def find_sign_out(self):
        return self.by_link_text('Sign Out')

    def login(self, username, pwd):
        # self.open_url(url)
        # # 进入登录页
        # self.find_sign_in().click()
        # username
        self.find_username().clear()
        self.find_username().send_keys(username)
        # pwd
        self.find_pwd().clear()
        self.find_pwd().send_keys(pwd)
        # submit
        self.find_submit().click()
        self.find_sign_out().click()
