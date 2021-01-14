#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/1  8:49 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : base_test_case.py
# @Software: PyCharm
'''

#抽象出一个测试基础类 用来继承

import  unittest;
from beidouxingauto_project.common.log_handler import log
from beidouxingauto_project.common.mysql_handler import db
from beidouxingauto_project import setting
from beidouxingauto_project.common.read_excle import OpenExcel;
from beidouxingauto_project.common.request_handler import send_method
from beidouxingauto_project.common.test_data_handler import get_phone

class BaseTestCase(unittest.TestCase):
    name = None; #模块名称

    logger = log; #日志模块

    db =db;   #数据库模块

    auth_key = 'v1';#鉴权请求头

    setting = setting;#配置文件加载

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info("开始测试{}".format(cls.name))

    @classmethod
    def tearDown(cls) -> None:
        cls.logger.info("{}功能结束".format(cls.name));

    @classmethod
    def loads_case(cls,sheet_name):
        return OpenExcel(cls.setting.TEST_DATA_FILE_PATH,sheet_name).open_read_excle_str();

    #发送请求
    def send_request(self,url,method="GET",**kwargs):
        #自动处理请求头
        kwargs.setdefault("headers",{});
        kwargs["headers"].update(self.setting.CUSTOMER_HEADER[self.auth_key]); #更新请求头
        #后续处理
        if self.auth_key=="v2":
            pass
        elif self.auth_key=="v3":
            pass;
        return send_method(url,method,**kwargs);

    @classmethod
    def get_no_use_phone(cls,sql_templeta):
        '''
        生成一个没有使用的手机号码
        :return:
        '''
        while True:
            phone_num = get_phone();#生成一个手机号
            # sql="select * from member where mobile_phone ='{}'".format(phone_num)
            # if phone_num.startswith("154",0,3):
            #     phone_num = get_phone();
            if  not cls.db.Isexist(sql=sql_templeta.format(phone_num)):
                return phone_num;