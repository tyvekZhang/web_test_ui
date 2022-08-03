# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/28
"""
import os
import sys
from public import Web

sys.path.append(os.pardir)


class Analysis(Web):

    def click_switch_to_analysis(self):
        """
        切换到analysis菜单项
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_plate_info(self):
        """
        点击获取酶标仪分类信息
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_spark(self):
        """
        选择spark类型的酶标仪
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_enspire(self):
        """
        选择enspire类型的酶标仪
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_upload_file(self):
        """
        调出文件上传弹窗
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def upload_file(self, content):
        """
        上传文件
        """
        self.web_upload(text=content)

    def click_download_result(self):
        """
        下载分析结果
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)


