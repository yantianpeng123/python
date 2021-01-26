#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/21  2:46 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_001.py
# @Software: PyCharm
'''
#
from beidouxingUI_Auto_Test.Auto_UI_Project.common.login_handler import log
import os
from beidouxingUI_Auto_Test.Auto_UI_Project.testcase.test_login_01 import TestLogin
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object import LoginPage
from beidouxingUI_Auto_Test.Auto_UI_Project import setting

from selenium import webdriver
if __name__ == '__main__':
    driver =  webdriver.Chrome()
    LoginPage(driver).login(username="123",password="124")
    os.system("allure serve {}".format(setting.ALLURE_RESULT_DIR));  # 执行cmd命令打开allure 服务
