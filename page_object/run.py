# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/28
"""
import os
import sys
from public import Web

sys.path.append(os.pardir)


class Run(Web):

    def click_switch_to_run(self):
        """
        切换到run菜单项
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_fasta_type(self):
        """
        选择以fast文件方式上传序列
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_upload_file(self):
        """
        调出文件上传弹窗
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def click_cas_options(self):
        """
        点击获取cas蛋白选项
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def sel_rna_guided_endonucleases_cas12(self):
        """
        选择cas12引导核酸内切酶
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_submit_button(self):
        """
        点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )
