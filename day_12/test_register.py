#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/1  8:57 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_register.py
# @Software: PyCharm
'''
import  unittest#单元测试模块
from ddt import ddt,data;#ddt数据驱动
from day_11.register import Register#注册方法
from day_12.read_excle import OpenExcel;
import json
from day_13.log_handler import log


cases = OpenExcel(file='../day_11/case_01.xlsx',sheetname='register').open_read_excle();
case_json =  OpenExcel(file='../day_11/case_01.xlsx',sheetname='register1').open_read_excle_str();

@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # log.info("====开始测试注册功能====");
        log.info("====开始测试注册功能====")

    @classmethod
    def tearDown(self) -> None:
        log.info("====测试注册功能结束====")


    @data(*cases)
    def test_register(self,case):
        '''
        注册功能
        '''
        res = Register(username=case['username'],password1=case['password1'],password2=case['password2']).register();
        #断言
        self.assertEqual(case['expect'],res);

    @data(*case_json)
    def test_register_json(self,case):
        request_data = json.loads(case['request_data']);
        expect_data = json.loads(case['expect_data']);
        res = Register(**request_data).register();
        try:
            self.assertEqual(res,expect_data);
        except Exception as e:
            log.warning()
            log.warning('{}:测试失败'.format(case['title']));
            log.warning('测试数据:{}'.format(request_data));
            log.warning('测试结果:{}'.format(res));
            log.warning('期望结果是:{}'.format(expect_data));
            raise e;
