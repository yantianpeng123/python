#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  7:00 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login_04.py
# @Software: PyCharm
'''
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.home_page import HomePage;
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.login_page import LoginPage
from beidouxingUI_Auto_Test.Auto_UI_Project.common.base_case_test import BaseCase

class TestLogin:

    name ="登录页面"

    def test_login_04(self,driver):
        lp = LoginPage(driver=driver);
        lp.login(username=self.setting.TEST_NORAML_USERNAME,password=self.setting.TEST_NORAML_PASSWORD);
        hp = HomePage(driver=driver);
        assert True == hp.get_logout_btn()