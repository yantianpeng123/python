#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/24  1:38 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm
'''
import unittest
from BeautifulReport import BeautifulReport;

if __name__ == '__main__':
    tld = unittest.TestLoader().discover(".")
    bf =BeautifulReport(tld);
    bf.report("闫天蓬","report.html")