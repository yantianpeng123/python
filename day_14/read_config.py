#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/20  8:44 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : read_config.py
# @Software: PyCharm
'''
#解析ini文件
#导入配置文件
from configparser import ConfigParser;

#实例化
config = ConfigParser();
#读取配置文件
config.read('config.ini');
#获取配置文件的所有的节点
secs =  config.sections();

print(config.sections());
print(config.options(secs[0]));
#config.get('log','file')#获取对应健的值
print(config.get('log','file'))

print(config['log']['debug']);
# print(config['log']['format'])
print(config['mysql']['db']);