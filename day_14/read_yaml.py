#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/20  8:57 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : read_yaml.py
# @Software: PyCharm
'''
#解析yaml文件 使用第三方库 pyyaml
import yaml

with open(file='config.yaml',mode='r',encoding='utf-8') as f :
    config =  yaml.load(f,Loader=yaml.FullLoader);
print(config);