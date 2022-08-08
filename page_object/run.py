# coding: utf-8

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

    def upload_file(self, content):
        """
        上传文件
        """
        self.web_upload(text=content)

    def click_chose_taxon_type(self):
        """
        选择以病毒分类形式上传序列
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def click_taxon_options(self):
        """
        点击获取病毒分类信息
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)


    def click_chose_viral(self):
        """
        选择一种要设计sgRNA病毒
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def click_cas_options(self):
        """
        点击获取cas蛋白选项
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def click_cas_options(self):
        """
        点击获取cas蛋白选项
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def select_cas12_taxon(self):
        """
        病毒下选择cas12引导核酸内切酶
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def select_cas13_taxon(self):
        """
        病毒分类输入选择cas13引导核酸内切酶
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def select_cas12_fasta(self):
        """
        fasta输入下选择cas12引导核酸内切酶
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def select_cas13_fasta(self):
        """
        fasta输入下选择cas13引导核酸内切酶
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def sel_rna_guided_endonucleases_cas13(self):
        """
        选择cas13引导核酸内切酶
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_lamp(self):
        """
        选择扩增方案为lamp
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_pcr_fasta(self):
        """
        输入fasta选择扩增方案为pcr
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_pcr_taxon(self):
        """
        选择病毒扩增方案为pcr
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_lamp_taxon(self):
        """
        选择病毒扩增方案为lamp
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_lamp_fasta(self):
        """
        fasta文件输入扩增方案为lamp
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_specificity_taxon(self):
        """
        以病毒分类添加特异性约束
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_taxon_specificity_taxon(self):
        """
        选择病毒分类下以病毒分类添加特异性约束
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_fasta_specificity_taxon(self):
        """
        输入为fasta下选择病毒分类为特异性条件
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_specificity_taxon_options(self):
        """
        点击获取特异性病毒分类信息
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_specificity_viral(self):
        """
        选择一种特异性病毒并确认
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_taxon_specificity_viral(self):
        """
        输入为选择病毒下选择一种特异性病毒并确认
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_specificity_fasta(self):
        """
        选择以fasta文件形式添加特异性约束
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_chose_taxon_specificity_fasta(self):
        """
        选择以fasta文件形式添加特异性约束
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_upload_specificity_file(self):
        """
        调出特异性文件上传弹窗输入为选择病毒
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def click_upload_specificity_file_fasta(self):
        """
        调出特异性文件上传弹窗输入为fasta
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def click_upload_taxon_specificity_file_fasta(self):
        """
        调出特异性文件上传弹窗输入为fasta
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def click_submit_button_fasta(self):
        """
        fasta为输入下点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_submit_button_fasta_specificity(self):
        """
        fasta为输入考虑特异性下点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_submit_button_taxon_fasta_specificity(self):
        """
        taxon为输入,考虑fasta特异性下点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_submit_button_taxon_specificity(self):
        """
        选择病毒考虑特异下点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_submit_button_taxon_taxon_specificity(self):
        """
        输入为选择病毒下选择病毒考虑特异下点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_submit_button_fasta_taxon_specificity(self):
        """
        fasta输入下选择病毒考虑特异下点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_submit_button_taxon(self):
        """
        选择病毒下点击提交按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_confirm_ok(self):
        """
        点击确认按钮
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )

    def click_show_result(self):
        """
        点击查看结果
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, )