#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/20  9:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : setting.py
# @Software: PyCharm
'''
import os
#项目根路径
BAST_PATH = os.path.dirname(os.path.abspath(__file__));

#测试用例路径
TEST_CASE_DIR = os.path.join(BAST_PATH,"testcase");

#项目域名
PROJECT_HOST_VUE = "http://8.129.91.152:8765";
#项目后台域名
PROJECT_HOST_ADMIN= "http://8.129.91.152:8765/amdin";

#接口信息
INTERFACE ={
    "login":"/Index/login.html"
}

#日志文件配置
LOG_CONFIG={
    "name": "beidouxing",
    "file": os.path.join(BAST_PATH,'log','beidouxing_web.log'),
    "fmt":"%(asctime)s--->>[%(filename)s--->line:%(lineno)d--%(levelname)s-->>%(message)s]",
    "debug": False
}

#配置账户信息
TEST_NORAML_USERNAME="18684720553";
TEST_NORAML_PASSWORD="python";
#存放测试报告的路径
ALLURE_RESULT_DIR = os.path.join(BAST_PATH,"allure-result");
#元素查找超时时间
DEFAULT_TIMEOUT = 3;

#错误截图路径
ERROR_SCREENSHOT_DIR = os.path.join(BAST_PATH,'screehot');