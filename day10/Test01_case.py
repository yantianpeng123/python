#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/19  4:17 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test01_case.py
# @Software: PyCharm
'''
import unittest
from BeautifulReport import BeautifulReport
class Test01_login(unittest.TestCase):

    def setUp(self) -> None:
        '''
        在每个测试函数执行前开始执行,可以作为前置条件写到里面
        :return:
        '''
        print("每个测试函数执行前开始执行")

    def tearDown(self) -> None:
        '''
        每个测试函数执行后开会执行,可以作为后置条件写到里面
        :return:
        '''
        print('在每个测试函数执行完毕后执行')

    def test_01_success(self):
        self.assertEqual("AAA",'aaa'.upper());

    def test_02_error(self):
        self.assertEqual('aaa',"AAA".lower());



if __name__ == '__main__':
    suit = unittest.TestSuite();
    suit.addTest(Test01_login('test_01_success'));
    suit.addTest(Test01_login('test_02_error'));
    BeautifulReport(suit).report('闫天蓬','report_02.html');
