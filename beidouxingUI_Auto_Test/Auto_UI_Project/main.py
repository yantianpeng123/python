#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/20  9:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm
'''
from beidouxingUI_Auto_Test.Auto_UI_Project import setting;
import pytest
import os

if __name__ == '__main__':
    pytest.main([
        "-s",
        "-v",
        # "-m",'other',
        # setting.TEST_CASE_DIR,
        os.path.join(setting.TEST_CASE_DIR,"test_invest.py"),
        "--alluredir={}".format(setting.ALLURE_RESULT_DIR),
        "--clean-alluredir"
    ])
    os.system("allure serve {}".format(setting.ALLURE_RESULT_DIR));  # 执行cmd命令打开allure 服务

