#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/19  4:01 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Beautidul_test.py
# @Software: PyCharm
'''
from day10.Login import login_check
import unittest
from BeautifulReport import BeautifulReport#需要导入BeautifulReport 模块
class Test_login(unittest.TestCase):#测试用例类

    '''
    如果有前置条件和后置条件，需要重写脚手架
    定义单元测试，但是测试函数(方法)必须是要以test开头
    '''
    def test_login_success(self):
        '''
        账号密码正确
        :return:
        '''
        #测试数据
        test_data ={'username':'amdin','password':'beidouxing1'};
        #预期结果
        expect_data ={'code':'0','msg':'登录成功'};
        #执行测试，使用解包的方式执行
        res = login_check(**test_data);
        #断言处理，判断预期结果和实际结果是否相等
        self.assertEqual(res,expect_data);

    def test_login_pwderror(self):
        '''
        账号正确，密码错误
        :return:
        '''
        test_data={'username':'amdin','password':'beidouxing1'};
        expect_data={'code':'1','msg':'账号密码不匹配'};
        res = login_check(**test_data);
        self.assertEqual(res,expect_data);

if __name__ == '__main__':
    #使用suit测试套件
    suit = unittest.TestSuite();
    suit.addTest(Test_login('test_login_success'))#添加测试用例
    suit.addTest(Test_login('test_login_pwderror'));#添加测试用例
    # with open('report.html','wb') as fb:#生成测试报告，这一块不需要添加encoding='utf8'这个参数
    BeautifulReport(suit).report('yantianpeng','report_01.html');