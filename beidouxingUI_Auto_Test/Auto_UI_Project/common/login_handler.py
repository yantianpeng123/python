#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/21  2:19 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : login_handler.py
# @Software: PyCharm
'''
#配置项目日志
import logging
from logging import handlers
from beidouxingUI_Auto_Test.Auto_UI_Project.setting import LOG_CONFIG
'''
    日志处理器
'''
def get_log(name=__name__,file="log.log",debug = False,fmt="'%(asctime)s--->>[%(filename)s--->line:%(lineno)d--%(levelname)s-->>%(message)s]'"):
    if debug:
        file_level =  logging.DEBUG;    #文件日志等级
        console_level = logging.DEBUG;  #控制台日志等级
    else:
        file_level = logging.WARNING;
        console_level =logging.INFO;
    #创建日志处理
    log = logging.getLogger(name);
    log.setLevel(logging.DEBUG);
    #创建日志处理器
    #文件日志等级
    file_handle =  logging.FileHandler(filename=file,encoding='utf-8');
    file_handle.setLevel(file_level);

    #控制台日志等级
    console_handle =  logging.StreamHandler();
    console_handle.setLevel(console_level);

    #特定时间间隔的轮换日志按小时生成日志文件
    th = handlers.TimedRotatingFileHandler(filename=file,when='D');
    th.setLevel(logging.DEBUG);
    th.suffix = "%Y-%m-%d.log" #
    #创建格式化器
    fmt = logging.Formatter(fmt=fmt);

    file_handle.setFormatter(fmt=fmt);
    console_handle.setFormatter(fmt=fmt);

    #时间轮转
    th.setFormatter(fmt=fmt);

    log.addHandler(file_handle);
    log.addHandler(console_handle);
    log.addHandler(th);

    return log;


# config = Config('../config/config.yaml',type_='yaml').parse();
# log = get_log(name=config['log']['file'],file=config['log']['file'],fmt=config['log']['format'])

log =  get_log(**LOG_CONFIG);
