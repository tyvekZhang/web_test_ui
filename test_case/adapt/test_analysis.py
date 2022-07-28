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
@ pytest.mark.run(order = -1)
class TestRun:

    @allure.title("酶标仪数据分析")
    @allure.description('Spark型号分析"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.smoke  # 用列标记
    @pytest.mark.parametrize('content', read_pytestdata(__file__, 'test_analysis_opt_one'))  # 测试数据
    def test_analysis_opt_one(self, goDriver, content):

        analysis = Analysis(goDriver)

        with allure.step('切换到analysis菜单'):
            analysis.click_switch_to_analysis()

        with allure.step('点击获取酶标仪分类信息'):
            analysis.click_plate_info()

        with allure.step('选择酶标仪类型'):
            analysis.click_chose_plate_type()

        with allure.step('调出文件上传弹窗'):
            analysis.click_upload_file()

        with allure.step('上传文件'):
            analysis.upload_file(content[0])

        with allure.step('下载分析结果'):
            analysis.click_download_result()

        analysis.sleep(5)