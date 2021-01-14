#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/20  3:18 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm
'''

import unittest;
from day_11.test_register import Test_Register;
from BeautifulReport import BeautifulReport;

if __name__ == '__main__':
    # suit = unittest.TestSuite();
    # suit.addTest(Test_Register('test_register_ok'));
    # suit.addTest(Test_Register('test_register_agrsIsNull'));
    tld = unittest.TestLoader().discover('.');
    br = BeautifulReport(tld);
    br.report('闫天蓬','report_register.html');
