#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/24  7:56 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : setting.py
# @Software: PyCharm
'''
import os

#项目根路径
BASE_PATH =  os.path.dirname(os.path.abspath(__file__));#项目的根目录
# print(BASE_PATH)
#测试数据
TEST_DATA_FILE_PATH =os.path.join(BASE_PATH,'testdata','ningmengban.xlsx');#测试数据文件路径配置
#测试用例路径
TEST_DATA_DIR= os.path.join(BASE_PATH,'testcases');
#配置项目路径和接口信息
PROJECT_URL = "http://api.lemonban.com/futureloan";

#接口地址
INTERFACE={
    "register":"/member/register",  #注册接口
    "login":"/member/login",        #登录接口
    "recharge":"/member/recharge",  #充值接口
    "withdraw":"/member/withdraw",  #提现接口
    "updateNickname":"/member/update",  #更新昵称
    "getInfo":"/member/{member_id}/info",#获取单个用户信息
    "add_project":"/loan/add",  #新增项目
    "audit_project":"/loan/audit",  #审核项目
    "invest_project":"/member/invest" ,#投资项目
    "loans_list":"/loans"    #分页获取项目列表
}

#鉴权方式自定义请求头
CUSTOMER_HEADER = {
    "v1": {"X-Lemonban-Media-Type":"lemonban.v1"},
    "v2": {"X-Lemonban-Media-Type":"lemonban.v2"},
    "v3": {"X-Lemonban-Media-Type":"lemonban.v3"}
}

#配置报告
TEST_REPORT_CONIFIG={
    "file":"report.html",
    "report_dir":os.path.join(BASE_PATH,"reports"),
    "title":"自动化测试报告",
    "description":"北斗星自动化测试报告",
    "tester":"yantianpeng",
    "type_":"br" #测试报告呢模版 htr表示html模版  br表示Beautifule模版
}


#日志配置
LOG_CONFIG = {
    "name":"beidouxing",
    "file":os.path.join(BASE_PATH,'log','beidouxing.log'),#路径的拼接
    "fmt":"%(asctime)s--->>[%(filename)s--->line:%(lineno)d--%(levelname)s-->>%(message)s]",
    "debug":False
}

#数据库配置
MYSQL_DATA_CONFIG = {
     "host": "api.lemonban.com",
     "port": 3306,
     "user": "future",
     "password": "123456",
     "db": "futureloan",
     "autocommit": True, #解决可重复的
     "charset": "utf8"
}

#配置allure结果路径
ALLURE_RESULT_DIR = os.path.join(BASE_PATH,"allure-result");