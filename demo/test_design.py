# encoding=utf-8

import allure, pytest, time
from selenium import webdriver
from util import case_data_utils


case_data = case_data_utils.get_case_data(f'\\adapt-api\\file\\apiTestCase.xlsx', 'caseSheet1', 'C端首屏', 'YES')

@allure.epic('crispr')
@allure.testcase( "https://devops.aliyun.com/projex/project/035276605c99ae0d14189c95ba/task#viewIdentifier=1945bcda00c0cf935ebdd8a5&openWorkitemIdentifier=a15741daf7d645f224a454c065")
@allure.feature("C端首屏")
@pytest.mark.parametrize('Function,TestCase,Type,Run,URL,Headers,Parameter,SQL1,SQL2,SQL3,AssertType,Expect1,Expect2,Expect3', case_data)
def test_steps_demo():
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()

        driver.get("http://www.baidu.com")

        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)

        time.sleep(2)

        driver.find_element_by_id("su").click()

        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")

        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()
