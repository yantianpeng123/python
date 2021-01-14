#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/1  9:10 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm
'''
import  unittest
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
    tl = unittest.TestLoader().discover('.');
    BeautifulReport(tl).report('report.html')
