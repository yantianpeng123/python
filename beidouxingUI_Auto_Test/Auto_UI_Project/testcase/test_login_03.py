#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  4:32 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login_03.py
# @Software: PyCharm
'''
import pytest
from selenium import webdriver;
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.login_page import LoginPage
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.home_page import HomePage

from time import sleep
from beidouxingUI_Auto_Test.Auto_UI_Project import setting

#定义一个pytest夹具 来实现数据共享
@pytest.fixture(scope="class")
def driver():
    with webdriver.Chrome() as wd:
        wd.maximize_window();
        yield wd

class TestLogin_01:


    def test_03(self,driver):
        LoginPage(driver).login(username=setting.TEST_NORAML_USERNAME,password=setting.TEST_NORAML_PASSWORD);
        sleep(3);
        assert True==HomePage(driver).get_logout_btn();
