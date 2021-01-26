#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  6:58 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
'''
#使用conftets.py文件实现夹具共享
# pytetst 会自动读取该文件中的内容和代码

import pytest
from selenium import webdriver
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.login_page_01 import LoginPage_01
from beidouxingUI_Auto_Test.Auto_UI_Project import setting


@pytest.fixture(scope="class")
def driver():
    with webdriver.Chrome() as wd:
        #窗口最大化
        wd.maximize_window();
        yield wd;

#继承上面的夹具 --driver
@pytest.fixture(scope="class")
def login_driver(driver):
    LoginPage_01(driver).login(username=setting.TEST_NORAML_USERNAME,password=setting.TEST_NORAML_PASSWORD);
    yield driver;
