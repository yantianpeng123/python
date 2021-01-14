#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/23  9:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : request_post.py
# @Software: PyCharm
'''
import requests;
base_url ='http://api.lemonban.com/futureloan';
inface_name='/member/register';
#设置请求头
headers = {
    "X-Lemonban-Media-Type":"lemonban.v2"
}
#设置参数传入到body体中
data = {
    "mobile_phone":"13858389766",
    "pwd":"12345678"
}

res = requests.post(url=base_url+inface_name,headers=headers,json=data);
print(res.json());#返回的数据必须是json格式，否则出现解析失败