#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/20  3:08 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_register.py
# @Software: PyCharm
'''
import unittest

from day_11.register import Register;

#测试注册的测试用例类
class Test_Register(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.reg_user = Register('python','1234567','1234567');


    def test_register_ok(self):
        '''
        注册成功
        '''
        self.reg_user = Register('python', '1234567', '1234567');
        res = self.reg_user.register();
        self.assertEqual(res,{'code':1,'msg':'注册成功'});

    def test_register_agrsIsNull(self):
        '''
            参数为空
        '''
        self.reg_user = Register('python', '1234567', '1234567');
        res = self.reg_user.register();
        self.assertEqual(res,{'code':0,'msg':'所有参数不能为空'});

    def test_register_pwd1Ispwd2(self):
        '''
        两次密码不一致
        '''
        res = Register('python', '12345678', '1234567').register();
        self.assertEqual(res,{'code':0,'msg':'两次密码不一致'});

    def test_register_accIsexist(self):
        '''
        账号已经存在
        '''
        res =  Register('python34','1234567','1234567').register();
        self.assertEqual(res,{'code':0,'msg':'该账户已经存在'});

    def test_register_pwdIsnotlen5(self):
        '''
        密码为5位
        '''
        res = Register('python12', '12345', '12345').register();
        self.assertEqual(res,{'code':0,'msg':'账号和密码必须在6-18位之间'})

    def test_register_pwdIsnotlen19(self):
        '''
        密码位19位
        '''
        res =  Register('python12','1234567890123456789','1234567890123456789').register();
        self.assertEqual(res,{'code':0,'msg':'账号和密码必须在6-18位之间'});

    def test_register_accIsnotlen5(self):
        '''

        账号位5位
        '''
        res = Register('pytho','1234567','1234567').register();
        self.assertEqual(res,{'code':0,'msg':'账号和密码必须在6-18位之间'});

    def test_register_accIsnotlen19(self):
        '''

        账号位19位
        '''
        res = Register('1234567890123456789','1234567','1234567').register();
        self.assertEqual(res,{'code':0,'msg':'账号和密码必须在6-18位之间'});
