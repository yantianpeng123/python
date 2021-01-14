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
from beidouxingauto_project import setting
from beidouxingauto_project.common.report_handler import report

if __name__ == '__main__':
    tld = unittest.TestLoader().discover(setting.TEST_DATA_DIR)
    report(ts=tld,**setting.TEST_REPORT_CONIFIG);