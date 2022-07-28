# Allure

## 1. 简介

> Allure是一款轻量级并且非常灵活的开源测试报告框架。 它支持绝大多数测试框架， 例如TestNG、Pytest、JUint等。它简单易用，易于集成。

## Allure装饰器功能说明

1. @allure.feature("一级模块") # 主要功能模块，具有相同feature名的用例将合并到一组
2. @allure.story("二级模块")# 子功能模块，具有相同story名的用例将合并到一组，同时存在feature和story时,feature为父节层级
3. @allure.titile("测试用例标题")# 测试用例标题，这样在测试报告中就不会显示测试方法名称了
4. @allure.issue(URL, name='点击我跳转禅道')# 问题标识，说白了就是BUG，可为一个BUG的url链接地址
5. @allure.testcase(URL, name='点击我跳转禅道')# 用例标识，关联用例，可为一个用例的url链接地址
6. @allure.severity("critical")# 用例优先级，包含blocker, critical, normal, minor, trivial 5个不同等级，默认是normal
7. @allure.step("字符串相加：{0}，{1}")# 测试步骤，通过{0}，{1}可以取到函数传参
8. @allure.description()# 测试用例描述
9. @allure.attach.file(r'E:\test.png',"父亲节",allure.attachment_type.PNG)# 用于向测试报告中输入一些附加的信息，如：图片、日志等

