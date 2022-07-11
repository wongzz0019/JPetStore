import allure

from common.base import Base


class Orders(Base):

    @allure.step("获取所有订单id")
    def find_order_id(self):
        return self.by_css_selectors("a[href^='/actions/Order.action?viewOrder=&orderId=']")

    @allure.step("获取所有订单的金额")
    def find_price(self):
        return self.by_xpaths('//*[@id="Content"]/table/tbody/tr/td[3]')



