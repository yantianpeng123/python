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
        res =  requests.get(url=url,**kwargs);
    elif method.upper()=="POST":
        res =  requests.post(url=url,**kwargs);
    elif method.upper()=="PATCH":
        res = requests.patch(url=url,**kwargs);
    #5XX异常 服务端异常
    if res.status_code >= 500:
            raise ValueError("服务端异常");
    #4XX 客户端异常
    elif res.status_code>=400:
        raise ValueError("客户端异常");
    return res;