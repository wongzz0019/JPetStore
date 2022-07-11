"""
浏览器对象工具类
"""

from time import sleep

from selenium import webdriver


class Driver(object):
    """浏览器对象管理类"""
    # 说明：对象变量只需要在类定义内部使用，因此定义为私有
    __driver = None   # 浏览器对象变量初始化状态

    # 类方法
    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 说明：为了防止在同一次测试过程中，调用获取浏览器对象方法时
        # 都会创建一个新的浏览器对象，因为有必要先判断对象是否存在，不存在时就创建！
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get('https://petstore.octoperf.com/actions/Catalog.action')
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(3)
        return cls.__driver

    # 类方法
    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 说明：必须保证浏览器对象存在，才能执行退出操作
        if cls.__driver:  # 等价于if cls.driver is not None:
            sleep(3)
            cls.__driver.quit()
            cls.__driver = None  # 保险手段：移除对象后，保留对象变量，以备下一次使用


if __name__ == '__main__':
    # 说明：定义为类方法,可以直接有类对象调用，省略实例化对象步骤
    Driver.get_driver()
    sleep(2)
    Driver.quit_driver()