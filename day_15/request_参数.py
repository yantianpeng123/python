#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/23  9:43 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : request_参数.py
# @Software: PyCharm
'''
import requests;

base_url ='http://api.lemonban.com/futureloan';
inface_name='/loans';
#参数拼接
args={
    "pageIndex":1,
    "pageSize":10
}
#设置请求头
headers={
    "X-Lemonban-Media-Type":"lemonban.v2"
}
res = requests.get(url=base_url+inface_name,params=args,headers = headers);
print(res.status_code);
print(res.text);
