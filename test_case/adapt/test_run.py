# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/28
"""
import allure
import pytest
from page_object.run import Run
from public import read_pytestdata
from pywinauto import Desktop

@allure.feature("反应设计")  # 测试用例特性(主要功能模块)
@allure.story("反应设计操作")  # 模块说明
@ pytest.mark.run(order = -3)
class TestRun:

    @allure.title("提交反应设计任务")
    @allure.description('fasta + cas12a + RPA组合"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.smoke  # 用列标记
    @pytest.mark.parametrize('content', read_pytestdata(__file__, 'test_submit_job_opt_one'))  # 测试数据
    def test_submit_job_opt_one(self, goDriver, content):
        run = Run(goDriver)

        with allure.step('切换到run菜单项'):
            run.click_switch_to_run()

        with allure.step('选择以fast文件方式上传序列'):
            run.click_chose_fasta_type()

        with allure.step('调出文件上传弹窗'):
            run.click_upload_file()

        with allure.step('上传文件'):
            run.upload_file(content[0])

        with allure.step('点击获取cas蛋白选项'):
            run.click_cas_options()

        with allure.step('选择cas12引导核酸内切酶'):
            run.sel_rna_guided_endonucleases_cas12()

        with allure.step('点击提交按钮'):
            run.click_submit_button()

        run.sleep(5)
