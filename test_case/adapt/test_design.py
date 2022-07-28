# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/27
"""

import allure
import pytest
from page_object.design import Design


@allure.feature("反应查询")  # 测试用例特性(主要功能模块)
@allure.story("反应结果操作")  # 模块说明
class TestDesign:

    @allure.title("反应结果查询及下载")
    @allure.description('cas12a + RPA结果"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.smoke  # 用列标记
    def test_target_search_cas12_rpa(self, goDriver):
        design = Design(goDriver)

        with allure.step('点击获取cas蛋白选项'):
            design.click_cas_options()

        with allure.step('选择cas12引导核酸内切酶'):
            design.sel_rna_guided_endonucleases_cas12()

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

        with allure.step('下载查询结果'):
            design.click_download_result()

        with allure.step('forward_primer局部搜索'):
            design.click_forword_primer_blast()

        with allure.step('reverse_primer局部搜索'):
            design.click_reverse_primer_blast()

        with allure.step('click_sgrna_blast局部搜索'):
            design.click_sgrna_blast()

        design.sleep(5)

        assert design.web_visibility_of_element_located('xpath', '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[4]')
