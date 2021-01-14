#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/20  7:26 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_register_byddt.py
# @Software: PyCharm
'''
import  unittest
from ddt import ddt,data,unpack
from day_11.register import Register;


case_01={'title': '注册成功','username':'python12','password1':'1234567','password2':'1234567','expect':{'code':1,'msg':'注册成功'}}
case_02 ={'title': '两次密码不一致','username': 'python12', 'password1': '12345678', 'password2': '1234567','expect': {'code':0,'msg':'两次密码不一致'}}
case_03 ={'title': '账户已经存在','username': 'python34', 'password1': '1234567', 'password2': '1234567','expect': {'code':0,'msg':'该账户已经存在'}}

cases = [
{'title': '注册成功','username':'python12','password1':'1234567','password2':'1234567','expect':{'code':1,'msg':'注册成功'}},
{'title': '两次密码不一致','username': 'python12', 'password1': '12345678', 'password2': '1234567','expect': {'code':0,'msg':'两次密码不一致'}},
{'title': '账户已经存在','username': 'python34', 'password1': '1234567', 'password2': '1234567','expect': {'code':0,'msg':'该账户已经存在'}}
]


@ddt
class TestRegisterByDDt(unittest.TestCase):


    # @data(case_01,case_02,case_03)
    @data(*cases)#当传递是个列表的时候，可以使用*进行解码
    def test_register(self,case):
        res = Register(username=case['username'],password1=case['password1'],password2=case['password2']).register();
        self.assertEqual(res,case['expect']);

    @data(case_01,case_02,case_03)
    def test_register_01(self,case):
        res =  Register(username=case['username'],password1=case['password1'],password2=case['password2']).register();
        self.assertEqual(res,case['expect']);



