# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/28
"""

import allure
import pytest

from page_object.analysis import Analysis
from public import read_pytestdata


@allure.feature("数据分析")  # 测试用例特性(主要功能模块)
@allure.story("数据分析操作")  # 模块说明
@pytest.mark.run(order=-1)
class TestRun:

    @allure.title("Spark酶标仪分析操作")
    @allure.description('Spark型号分析文件并下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    @pytest.mark.parametrize('content', read_pytestdata(__file__, 'test_analysis_spark'))  # 测试数据
    def test_analysis_spark(self, goDriver, content):
        analysis = Analysis(goDriver)

        self.common_step_analysis_download_prepare(analysis)

        self.common_step_choose_spark(analysis)

        self.common_step_analysis_download(analysis, content)

    @allure.title("Enspire酶标仪分析操作")
    @allure.description('Enspire型号分析文件并下载"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    @pytest.mark.parametrize('content', read_pytestdata(__file__, 'test_analysis_enspire'))  # 测试数据
    def test_analysis_enspire(self, goDriver, content):
        analysis = Analysis(goDriver)

        self.common_step_analysis_download_prepare(analysis)

        self.common_step_choose_enspire(analysis)

        self.common_step_analysis_download(analysis, content)

    def common_step_analysis_download_prepare(self, analysis: Analysis):
        with allure.step('切换到analysis菜单'):
            analysis.click_switch_to_analysis()

        with allure.step('点击获取酶标仪分类信息'):
            analysis.click_plate_info()

    def common_step_choose_spark(self, analysis: Analysis):
        with allure.step('选择spark类型的酶标仪'):
            analysis.click_chose_spark()

    def common_step_choose_enspire(self, analysis: Analysis):
        with allure.step('选择enspire类型的酶标仪'):
            analysis.click_chose_enspire()

    def common_step_analysis_download(self, analysis: Analysis, content):
        with allure.step('调出文件上传弹窗'):
            analysis.click_upload_file()

        with allure.step('上传文件'):
            analysis.upload_file(content[0])

        analysis.screen_shot(str(analysis.__class__.__name__))

        with allure.step('下载分析结果'):
            analysis.click_download_result()

        analysis.sleep(5)
