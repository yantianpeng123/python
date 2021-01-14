#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/24  12:44 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_register.py
# @Software: PyCharm
'''
#测试注册
import unittest;
import json
from day_16.log_handler import log #日志模块
from day_16.read_excle import OpenExcel  #解析excle
from ddt import ddt ,data
from day_16.request_handler import send_method


case_json =  OpenExcel(file='ningmengban.xlsx',sheetname='register').open_read_excle_str();
@ddt()
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
       log.info("开始测试注册功能")

    @classmethod
    def tearDown(self) -> None:
        log.info("测试注册功能结束");


    #测试注册功能
    @data(*case_json)
    def test_register(self,case):
        #1.测试数据(request_data,expect_data)
        request_date = json.loads(case['request_data']);
        expect_data =  json.loads(case['expect_data']);
        #2.测试步骤
            #发送请求
        base_url = case['url'];
        method = case['method'];
        headers = {
            "X-Lemonban-Media-Type":"lemonban.v2"
        }
        res = send_method(url=base_url,method=method,json=request_date,headers=headers);
        #3.断言
        rel_data = res.json();
        try:
            self.assertEqual(rel_data['code'], expect_data['code']);
            self.assertEqual(rel_data['msg'],expect_data['msg'])
        except Exception as e:
            log.warning('{}:测试失败'.format(case['title']));
            log.warning('测试数据:{}'.format(request_date));
            log.warning('测试结果:{}'.format(rel_data));
            log.warning('期望结果是:{}'.format(expect_data));
            raise e;



if __name__ == '__main__':
    unittest.main();