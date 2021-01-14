#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/2  9:13 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : logging_02.py
# @Software: PyCharm
'''


import logging
#日志组件：
#   1.logger日志器：产生日志的。
#   2.Handler日志处理器,将日志发送到指定的位置，文件中，控制台等等
#   3.Filter 日志过滤器,过滤日志，
#   4.Formatter日志格式器 用于控制日志的输出格式。


#   日志步骤
#   1.创建日志器

log =  logging.getLogger("beidouxing");# 创建日志器
log.setLevel(logging.DEBUG);
#   2.创建日志处理器
file_handler =  logging.FileHandler(filename='beidouxing.log',encoding='utf-8'); #创建写入文件的日志级别
file_handler.setLevel(logging.DEBUG);# 设置日志级别


console_handler = logging.StreamHandler();#创建控制台的日志输出。
console_handler.setLevel(logging.DEBUG);# 设置日志级别
#   3.创建格式化器
log_format = logging.Formatter(fmt='%(asctime)s--->>[%(filename)s--->line:%(lineno)d--%(levelname)s-->>%(message)s]')


#   4.把格式化器添加到日志处理器上
file_handler.setFormatter(log_format);
console_handler.setFormatter(log_format);
#   5.把日志处理器添加到日志器
log.addHandler(file_handler);
log.addHandler(console_handler);

log.debug("This a debug");
log.debug("===This a debug===");