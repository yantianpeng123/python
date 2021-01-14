#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/24  1:00 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : request_handler.py
# @Software: PyCharm
'''
import requests

def send_method(url,method ='GET',**kwargs):

    if method.upper()=="GET":
        return requests.get(url=url,**kwargs);
    elif method.upper()=="POST":
        return requests.post(url=url,**kwargs);
    else:
        return '{请求方法错误}';
