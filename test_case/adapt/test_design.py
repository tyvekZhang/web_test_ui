# coding: utf-8

"""
Author：tyvek_zhang
Date：2022/07/27
"""

import allure
import pytest
from page_object.design import Design


@allure.feature("反应查询")  # 测试用例特性(主要功能模块)
@allure.story("反应结果操作")  # 模块说明
@pytest.mark.run(order=-2)
class TestDesign:

    @allure.title("cas13 + RPA组合操作")
    @allure.description('cas13 + RPA结果查询及文件下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    def test_target_search_cas13_rpa(self, goDriver):
        design = Design(goDriver)

        self.common_step_for_cas_options(design)

        self.common_step_for_cas13(design)

        self.common_step_for_rna_guided_endonucleases(design)

    @allure.title("cas13 + LAMP组合操作")
    @allure.description('cas13 + LAMP结果查询及文件下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    def test_target_search_cas13_lamp(self, goDriver):
        design = Design(goDriver)

        self.common_step_for_cas_options(design)

        self.common_step_for_cas13(design)

        self.click_chose_lamp(design)

        self.common_step_for_rna_guided_endonucleases(design)

    @allure.title("cas13 + PCR组合操作")
    @allure.description('cas13 + PCR结果查询及文件下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    def test_target_search_cas13_pcr(self, goDriver):
        design = Design(goDriver)

        self.common_step_for_cas_options(design)

        self.common_step_for_cas13(design)

        self.click_chose_pcr(design)

        self.common_step_for_rna_guided_endonucleases(design)

    @allure.title("cas12a + RPA组合操作")
    @allure.description('cas12a + RPA结果查询及文件下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    def test_target_search_cas12_rpa(self, goDriver):
        design = Design(goDriver)

        self.common_step_for_cas_options(design)

        self.common_step_for_cas12a(design)

        self.common_step_for_rna_guided_endonucleases(design)


    @allure.title("cas12 + LAMP组合操作")
    @allure.description('cas12 + LAMP结果查询及文件下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    def test_target_search_cas12_lamp(self, goDriver):
        design = Design(goDriver)

        self.common_step_for_cas_options(design)

        self.common_step_for_cas12a(design)

        self.click_chose_lamp(design)

        self.common_step_for_rna_guided_endonucleases(design)

    @allure.title("cas12 + PCR组合操作")
    @allure.description('cas12 + PCR结果查询及文件下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    def test_target_search_cas12_pcr(self, goDriver):
        design = Design(goDriver)

        self.common_step_for_cas_options(design)

        self.common_step_for_cas12a(design)

        self.click_chose_pcr(design)

        self.common_step_for_rna_guided_endonucleases(design)

    def common_step_for_cas12a(self, design: Design):
        with allure.step('选择cas12引导核酸内切酶'):
            design.sel_rna_guided_endonucleases_cas12()

    def common_step_for_cas13(self, design: Design):
        with allure.step('选择cas13引导核酸内切酶'):
            design.sel_rna_guided_endonucleases_cas13()

    def click_chose_lamp(self, design: Design):
        with allure.step('选择扩增方案为lamp'):
            design.click_chose_lamp()

    def click_chose_pcr(self, design: Design):
        with allure.step('选择扩增方案为pcr'):
            design.click_chose_pcr()

    def common_step_for_cas_options(self, design: Design):
        with allure.step('点击获取cas蛋白选项'):
            design.click_cas_options()

    def common_step_for_rna_guided_endonucleases(self, design: Design):
        with allure.step('点击获取分类信息'):
            design.click_tax_info()

        with allure.step('点击一级分类'):
            design.click_tax_fir()

        with allure.step('点击二级分类'):
            design.click_tax_sec()

        with allure.step('点击三级分类'):
            design.click_tax_thi()

        with allure.step('点击查询按钮'):
            design.click_query_button()

        design.screen_shot(str(design.__class__.__name__))

        with allure.step('下载查询结果'):
            design.click_download_result()

        with allure.step('forward_primer局部搜索'):
            design.click_forword_primer_blast()

        with allure.step('reverse_primer局部搜索'):
            design.click_reverse_primer_blast()

        with allure.step('click_sgrna_blast局部搜索'):
            design.click_sgrna_blast()

        design.sleep(10)
