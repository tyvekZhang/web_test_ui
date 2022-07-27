# conding=utf-8

from time import sleep


class BasePage:
    """selenium的常用函数封装"""

    def __init__(self, driver):
        """
        构造函数
        :param driver: 浏览器驱动
        """
        self.driver = driver

    def open(self):
        """
        打开指定网页
        :param url: 网页地址
        """
        self.driver.get(self.url)

    def locator(self, loc):
        """
        元素定位
        :param loc: 定位因子
        :return: 定位到的元素
        """
        return self.driver.find_element(*loc)

    def input_content(self, loc, content):
        """
        输入
        :param loc: 定位因子
        :param content: 要输入的内容
        """
        self.locator(loc).send_keys(content)

    def click(self, loc):
        """
        点击
        :param loc: 定位因子
        """
        self.locator(loc).click()

    def wait(self, time_sec):
        """
        系统等待
        :param time_sec: 等待的秒数
        :return:
        """
        sleep(time_sec)
