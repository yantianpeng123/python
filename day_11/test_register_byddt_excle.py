#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/21  11:21 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_register_byddt_excle.py
# @Software: PyCharm
'''
import  unittest
from ddt import ddt ,data
from day_11.register import Register;
from day_11.read_openpyxl import Openxls;
@ddt()
class test_register_excle(unittest.TestCase):


    #获取excle中用例的数据
    cases = Openxls('case_01.xlsx','login').readContent();


    @data(*cases)
    def test_register(self,case):
        res = Register(username=case['username'],password1=case['password1'],password2=case['password2']).register();
        self.assertEqual(res,case['expect']);