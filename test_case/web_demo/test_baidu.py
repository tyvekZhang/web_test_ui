# -*- coding: utf-8 -*-

"""
Author：tyvek_zhang
Date：2022/07/26
"""

import allure
import pytest
from page_object.baidu import BaiDu
from public.read_data import read_pytestdata

@allure.feature("百度搜索")  # 测试用例特性(主要功能模块)
@allure.story("所搜验证")  # 模块说明
class TestBaiDu:

    @allure.title("输入内容并搜索")  # 用例标题
    @allure.description('输入多参数搜索')  # 用例描述
    @allure.link("https://xxx/testcase/list", name='用例链接link')
    @pytest.mark.testbaidu_web  # 用列标记
    @pytest.mark.parametrize('content', read_pytestdata(__file__, 'test_baidu_search'))  # 测试数据
    def test_baidu_search(self, goDriver, content):
        baidu = BaiDu(goDriver)

        with allure.step('输入搜索内容'):
            baidu.input_search_content(content)

        with allure.step('点击搜索'):
            baidu.click_search_button()

            baidu.sleep(3)

            res = content[0] in baidu.web_title
            assert content[0] in baidu.web_title
