# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/28
"""
import allure
import pytest

from page_object.run import Run
from public import read_pytestdata


@allure.feature("反应设计")
@allure.story("反应设计操作")
@pytest.mark.run(order=-3)
class TestRun:

    @allure.title("fasta + cas12a + RPA进行设计")
    @allure.description('fasta + cas12a + RPA提交任务"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.parametrize('content, specificity_content', read_pytestdata(__file__, 'test_submit_job_fasta_cas12_rpa'))  #测试数据
    def test_submit_job_fasta_cas12_rpa(self, goDriver, content, specificity_content):
        run = Run(goDriver)

        self.common_step_prepare(run)

        self.common_step_upload_fasta(run, content)

        self.common_step_cas_options(run)

        self.common_step_cas12_fasta(run)

        self.click_submit_button_fasta(run)

    @allure.title("fasta + cas12a + LAMP进行设计")
    @allure.description('fasta + cas12a + LAMP提交任务"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    @pytest.mark.parametrize('content, specificity_content', read_pytestdata(__file__, 'test_submit_job_fasta_cas12_lamp'))  #
    # 测试数据
    def test_submit_job_fasta_cas12_lamp(self, goDriver, content, specificity_content):
        run = Run(goDriver)

        self.common_step_prepare(run)

        self.common_step_upload_fasta(run, content)

        self.common_step_cas_options(run)

        self.common_step_cas12_fasta(run)

        self.click_chose_lamp_fasta(run)

        self.click_submit_button_fasta(run)

    @allure.title("fasta + cas12a + PCR进行设计")
    @allure.description('fasta + cas12a + PCR提交任务"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    @pytest.mark.parametrize('content, specificity_content', read_pytestdata(__file__, 'test_submit_job_fasta_cas12_pcr'))
    def test_submit_job_fasta_cas12_pcr(self, goDriver, content, specificity_content):
        run = Run(goDriver)

        self.common_step_prepare(run)

        self.common_step_upload_fasta(run, content)

        self.common_step_cas_options(run)

        self.common_step_cas12_fasta(run)

        self.click_chose_pcr_fasta(run)

        self.click_submit_button_fasta(run)

    @allure.title("taxon + cas12a + RPA进行设计")
    @allure.description('taxon + cas12a + RPA提交任务"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    @pytest.mark.parametrize('content, specificity_content', read_pytestdata(__file__, 'test_submit_job_taxon_cas12_rpa'))
    def test_submit_job_taxon_cas12_rpa(self, goDriver, content, specificity_content):
        run = Run(goDriver)

        self.common_step_prepare(run)

        self.common_step_chose_taxon(run)

        self.common_step_cas_options(run)

        self.common_step_cas12_taxon(run)

        self.click_submit_button_taxon(run)

    @allure.title("taxon + cas12a + LAMP进行设计")
    @allure.description('taxon + cas12a + LAMP提交任务"')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke  # 用例标记
    @pytest.mark.parametrize('content, specificity_content', read_pytestdata(__file__, 'test_submit_job_taxon_cas12_lamp'))
    def test_submit_job_taxon_cas12_lamp(self, goDriver, content, specificity_content):
        run = Run(goDriver)

        self.common_step_prepare(run)

        self.common_step_chose_taxon(run)

        self.common_step_cas_options(run)

        self.common_step_cas12_taxon(run)

        self.click_chose_lamp_taxon(run)

        self.click_submit_button_taxon(run)

    @allure.title("taxon + cas12a + PCR进行设计")
    @allure.description('taxon + cas12a + PCR提交任务"')
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.my_smoke
    @pytest.mark.parametrize('content, specificity_content', read_pytestdata(__file__, 'test_submit_job_taxon_cas12_pcr'))
    def test_submit_job_taxon_cas12_pcr(self, goDriver, content, specificity_content):
        run = Run(goDriver)

        self.common_step_prepare(run)

        self.common_step_chose_taxon(run)

        self.common_step_cas_options(run)

        self.common_step_cas12_taxon(run)

        self.click_chose_pcr_taxon(run)

        self.click_submit_button_taxon(run)

    def common_step_prepare(self, run: Run):
        with allure.step('切换到run菜单项'):
            run.click_switch_to_run()

    def common_step_upload_fasta(self, run: Run, content):
        with allure.step('选择以fast文件方式上传序列'):
            run.click_chose_fasta_type()

        with allure.step('调出文件上传弹窗'):
            run.click_upload_file()

        with allure.step('上传文件'):
            run.upload_file(content)

    def common_step_chose_taxon(self, run: Run):
        with allure.step('选择以病毒分类形式上传序列'):
            run.click_chose_taxon_type()

        with allure.step('点击获取病毒分类信息'):
            run.click_taxon_options()

        with allure.step('选择一种要设计sgRNA病毒'):
            run.click_chose_viral()

    def common_step_upload_specificity_fasta(self, run: Run, specificity_content):
        with allure.step('屏幕滚动到底部'):
            run.web_scroll('down')

        with allure.step('选择以fasta文件形式添加特异性约束'):
            # run.click_chose_specificity_fasta()
            ele = run.driver.find_element_by_xpath(
                '//*[@id="rc-tabs-0-panel-1"]/div/div/div/div/form/div[7]/div/div[2]/label/button/span')
            ele.click()

        with allure.step('调出特异性文件上传弹窗'):
            run.click_upload_specificity_file()

        with allure.step('上传文件'):
            run.upload_file(specificity_content)

    def common_step_cas_options(self, run: Run):
        self.web_scroll_part(run)
        
        with allure.step('点击获取cas蛋白选项'):
            run.click_cas_options()

    def common_step_cas12_taxon(self, run: Run):
        with allure.step('病毒分类输入选择cas12引导核酸内切酶'):
            run.select_cas12_taxon()

    def common_step_cas12_fasta(self, run: Run):
        with allure.step('fasta文件输入选择cas12引导核酸内切酶'):
            run.select_cas12_fasta()

    def common_step_lamp(self, run: Run):
        with allure.step('选择扩增方案为lamp'):
            run.click_chose_lamp()

    def common_step_pcr_fasta(self, run: Run):
        with allure.step('输入fasta选择扩增方案为pcr'):
            run.click_chose_pcr_fasta()

    def click_chose_lamp_taxon(self, run: Run):
        with allure.step('选择病毒扩增方案为lamp'):
            run.click_chose_lamp_taxon()

    def click_chose_lamp_fasta(self, run: Run):
        with allure.step('fasta文件输入扩增方案为lamp'):
            run.click_chose_lamp_fasta()

    def click_chose_pcr_fasta(self, run: Run):
        with allure.step('fasta文件输入扩增方案为pcr'):
            run.click_chose_pcr_fasta()

    def click_chose_pcr_taxon(self, run: Run):
        with allure.step('选择病毒扩增方案为pcr'):
            run.click_chose_pcr_taxon()

    def web_scroll_part(self, run: Run):
        with allure.step('向下滑动屏幕'):
            run.web_scroll_part(direction='down')

    def click_submit_button_fasta(self, run: Run):

        with allure.step('fasta为输入下点击提交按钮'):
            run.click_submit_button_fasta()

        self.screen_shot(run)

        self.click_confirm_ok(run)

        self.click_show_result(run)

    def click_submit_button_taxon(self, run: Run):

        run.sleep(2)

        with allure.step('选择病毒下点击提交按钮'):
            run.click_submit_button_taxon()
        self.screen_shot(run)

        self.click_confirm_ok(run)

        self.click_show_result(run)

    def screen_shot(self, run: Run):
        run.screen_shot(str(run.__class__.__name__))

        run.sleep(2)

    def click_confirm_ok(self, run: Run):
        with allure.step('点击确认按钮'):
            run.click_confirm_ok()
            run.sleep(2)

    def click_show_result(self, run: Run):
        with allure.step('点击确认按钮'):
            run.click_show_result()
            run.sleep(3)