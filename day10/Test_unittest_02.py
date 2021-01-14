#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/17  2:20 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_unittest_02.py
# @Software: PyCharm
'''

from .Login import login_check;
import unittest
from day09.HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
#单元测试:代码测试代码
#针对函数，类 核实他的某个方面是否有问题的测试
#单元测试一般是有开发来完成的。
#测试用例是一组单元测试组合起来的，每个单元测试是一起核实函数或者类在各种情况下的行为都符合要求
#为啥要做单元测试
#1.单元测试通过--->>>集成测试----》》》
#2.可以提早发现bug

#编写测试用例:

# 用例类型       测试数据                                       预期结果
# 账号密码正确   {'username':'amdin','password':'beidouxing'}  {'code':'0','msg':'登录成功'};
# 账号正确密码错误 {'username':'amdin','password':'beidouxing1'}  {'code':'1','msg':'账号密码不匹配'};
# 账号错误密码正确 {'username':'amdin1','password':'beidouxing'}  {'code':'1','msg':'账号密码不匹配'};
# 账号正确，密码长度小于6 {'username':'amdin','password':'bei'}  {'code':'2','msg':'密码长度请在6到18之间'};;
# 账号正确 密码长度大于18 {'username':'amdin','password':'beidouxing1234567890'}  {'code':'2','msg':'密码长度请在6到18之间'};
#创建测试类，并且要继承unittest.TestCase
class Test_login(unittest.TestCase):

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
        test_data ={'username':'amdin','password':'beidouxing'};
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


    def test_login_acterror(self):
        '''
        账号错误，密码正确
        :return:
        '''
        #测试数据
        test_data ={'username':'amdin1','password':'beidouxing'};
        #预期结果
        expect_data = {'code':'1','msg':'账号密码不匹配'};
        #执行测试
        res = login_check(**test_data);
        #断言(判断预期结果和实际结果是否相等)
        self.assertEqual(res, expect_data);

    def test_login_pwdlen_01(self):
        '''
        账号正确密码长度小于6
        :return:
        '''
        #测试数据
        test_data ={'username':'amdin','password':'bei'};
        #预期结果
        expect_data = {'code':'2','msg':'密码长度请在6到18之间'};
        #执行测试
        res = login_check(**test_data);
        #断言处理
        self.assertEqual(res, expect_data);

    def test_login_pwdlen_02(self):
        '''
        账号正确 密码长度大于18
        :return:
        '''
        #测试数据
        test_data = {'username':'amdin','password':'beidouxing1234567890'};
        #预期数据
        expect_data ={'code':'2','msg':'密码长度请在6到18之间'};
        #执行测试
        res = login_check(**test_data);
        #断言处理
        self.assertEqual(res, expect_data);

if __name__ == '__main__':
    #实例化测试套件
    suit = unittest.TestSuite();
    #这是一个比较笨重的方法
    # suit.addTest(Test_login('test_login_success'));#添加测试用例 测试类名('测试方法名')
    # suit.addTest(Test_login('test_login_pwderror'));
    # suit.addTest(Test_login('test_login_acterror'));
    # suit.addTest(Test_login('test_login_pwdlen_01'));
    # suit.addTest(Test_login('test_login_pwdlen_02'));
    # 一般在项目中使用test_loader
    #loader = unittest.TestLoader;#不需要添加括号
    #tl = loader.loadTestsFromTestCase(Test_login);
    #print(tl);
    tloader = unittest.TestLoader();
    ts =tloader.discover('.');#三个参数 第一个:开始查找的目录  第二个:查找模块的规则名字  第三个: 项目的顶层目录
    runner = unittest.TextTestRunner();
    res = runner.run(ts);
    print(type(res),res);
    with open('report.html','w',encoding='utf-8') as fb:
       html_01 =  HTMLTestRunner(stream=fb,description='闫天蓬自动化测试报告',title='自动化测试报告',tester='闫天蓬');
       html_01.run(ts);