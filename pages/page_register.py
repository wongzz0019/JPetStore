from time import sleep

from selenium.webdriver.support.select import Select

from common.base import Base


class Register(Base):
    # 进入注册面
    def find_sign_in(self):
        return self.by_link_text('Sign In')

    # 进入注册面
    def find_register(self):
        return self.by_link_text('Register Now!')

    # userid
    def find_userid(self):
        return self.by_name('username')

    # pwd
    def find_pwd(self):
        return self.by_name('password')

    # rpwd
    def find_rpwd(self):
        return self.by_name('repeatedPassword')

    # firstname
    def find_firstname(self):
        return self.by_name('account.firstName')

    # lastname
    def find_lastname(self):
        return self.by_name('account.lastName')

    # email
    def find_email(self):
        return self.by_name('account.email')

    # phone
    def find_phone(self):
        return self.by_name('account.phone')

    # address1
    def find_address1(self):
        return self.by_name('account.address1')

    # address2
    def find_address2(self):
        return self.by_name('account.address2')

    # city
    def find_city(self):
        return self.by_name('account.city')

    # state
    def find_state(self):
        return self.by_name('account.state')

    # zip
    def find_zip(self):
        return self.by_name('account.zip')

    # country
    def find_country(self):
        return self.by_name('account.country')

    # 语言——下拉框
    def find_language(self):
        element = self.by_name('account.languagePreference')
        select_language = Select(element)
        return select_language

    # 喜好——下拉框
    def find_favourite(self):
        element = self.by_name('account.favouriteCategoryId')
        select_favourite = Select(element)
        return select_favourite

    # 复选框——MyList
    def find_mylist(self):
        return self.by_name('account.listOption')

    # 复选框——MyList
    def find_mybanner(self):
        return self.by_name('account.bannerOption')

    # 保存注册
    def find_save(self):
        return self.by_name('newAccount')


