import allure
from selenium.webdriver.support.select import Select

from common.base import Base


# 登录 - 选商品 - 点击商品 - 加入购物车 - 选数量 - 更新购物车 - 付款 - 编辑订单信息 - 确认信息 - ok
class Buy(Base):

    # # 选大种类
    # # 1:Fish; 2:Dogs; 3:Reptiles; 4:Cats; 5:Birds
    # @allure.step('选择大种类')
    # def find_product(self, number):
    #     return self.by_xpath('//*[@id="QuickLinks"]/a[{}]'.format(number))

    # 选择小种类
    @allure.step('选择小种类')
    def find_product_id(self, product_id):
        return self.by_link_text(product_id)

    # 查看商品信息
    @allure.step('查看商品信息')
    def find_item_info(self, item_id):
        return self.by_link_text(item_id)

    # 加购物车
    # item_id宠物id
    @allure.step('加购物车')
    def find_add_cart(self, item_id):
        return self.by_css_selector("a[href$='workingItemId={}']".format(item_id))

    # 定位数量输入框
    @allure.step('输入商品数量')
    def find_quantity(self, item_id):
        return self.by_name(item_id)

    # 更新购物车
    @allure.step('更新购物车')
    def find_update_cart(self):
        return self.by_name('updateCartQuantities')

    # 结账
    @allure.step('结账')
    def find_proceed_to_checkout(self):
        return self.by_link_text('Proceed to Checkout')

    # 付款卡类型
    @allure.step('现在付款卡类型')
    def find_card_type(self, card_type):
        return Select(self.by_name('order.cardType')).select_by_value(card_type)

    @allure.step('付款卡号')
    def find_credit_card(self):
        return self.by_name('order.creditCard')

    @allure.step('到日期')
    def find_expiry_date(self):
        return self.by_name('order.expiryDate')

    # 账单地址
    @allure.step('账单姓')
    def find_bill_fname(self):
        # 姓
        return self.by_name('order.billToFirstName')

    @allure.step('账单名')
    def find_bill_lname(self):
        return self.by_name('order.billToLastName')

    @allure.step('账单地址1')
    def find_bill_addr1(self):
        return self.by_name('order.billAddress1')

    @allure.step('账单地址2')
    def find_bill_addr2(self):
        return self.by_name('order.billAddress2')

    @allure.step('城市')
    def find_bill_city(self):
        return self.by_name('order.billCity')

    @allure.step('账单状态')
    def find_bill_state(self):
        return self.by_name('order.billState')

    @allure.step('邮政编码')
    def find_bill_zip(self):
        return self.by_name('order.billZip')

    @allure.step('国家')
    def country(self):
        return self.by_name('order.billCountry')

    # 复选框-配送到其它地址
    def find_ship_to_diff_addr(self):
        return self.by_name('shippingAddressRequired')

    # continue按钮
    @allure.step('点击continue按钮')
    def find_neworder(self):
        return self.by_css_selector('input[name="newOrder"]')

    # 获取账单地址信息内容
    @allure.step('获取订单地址信息')
    def find_bill_addr_text(self):
        fname = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[3]/td[2]').text
        lname = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[4]/td[2]').text
        addr1 = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[5]/td[2]').text
        addr2 = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[6]/td[2]').text
        city = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[7]/td[2]').text
        state = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[8]/td[2]').text
        zip = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[9]/td[2]').text
        country = self.by_xpath('//*[@id="Catalog"]/table/tbody/tr[10]/td[2]').text
        return fname, lname, addr1, addr2, city, state, zip, country

    # confirm按钮
    @allure.step('点击confirm按钮')
    def find_confirm(self):
        return self.by_link_text('Confirm')

    # 获取成功信息
    @allure.step('获取提示信息')
    def find_messages(self):
        return self.by_css_selector('.messages>li')

