#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/2  8:07 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : logging_01.py
# @Software: PyCharm
'''
#日志模块
import logging

logging.basicConfig(level=logging.DEBUG
                    ,format='%(asctime)s--->>[%(filename)s--->line:%(lineno)d--%(levelname)s-->>%(message)s]'
                    ,filename='beidouxing_001.log')#设置日志的等级的级别，和输入格式,日志输出地址
#asctime：表示的是时间
#filename:表示的是当前文件的名字
#lineno:表示日志的行数
#levelname:表示当前日志的级别
#message:表示日志的内容信息

#默认情况下日志的等级warning警告级别
logging.debug("This a debug log,在调试阶段开始使用");
logging.info("这是info日志,在信息阶段使用");
logging.warning("这是警告日志,用来做警告日志");
logging.error("这是错误日志,这是错误日志，用来做错误记录");
logging.critical("这是致命错误,这是程序发生啦致命的错误");