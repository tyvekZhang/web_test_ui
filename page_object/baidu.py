# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/26
"""
import os
import sys
from public import Web

sys.path.append(os.pardir)

'''
page_object  对应 locatorYAML 操作页面
'''


class BaiDu(Web):

    def input_search_content(self, content):
        """
        输入搜索内容
        :param content: 输入内容
        :return:
        """
        # self.webexe(__file__,sys._getframe().f_code.co_name)
        # __file__ 代表当前运行的py文件 运行的py文件必须和locatorYAML保持文件名称一样
        # sys._getframe().f_code.co_name 获取当前运行函数名称  次函数名称必须和 locatorYAML 的casename保持一致

        self.webexe(__file__, sys._getframe().f_code.co_name, text=content)
        # self.webexe(__file__, 'input_search_content', text=content)

    def click_search_button(self):
        """
        点击百度一下
        :return:
        """

        self.webexe(__file__, sys._getframe().f_code.co_name, )
