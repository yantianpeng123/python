#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/24  1:24 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_data.py
# @Software: PyCharm
'''
from day_16.request_handler import send_method
import random

if None:
    print("22");
else:
    print("33");



print(random.choice('358'))

phone = ['1',random.choice('358')]
print(phone);
for i in range(9):
    phone.append(random.choice('0123456789'));
phone =''.join(phone)
print(phone);


base_url ="http://api.lemonban.com/futureloan/member/withdraw";
request_data = {
    "member_id":"1",
    "amount":100
}


expect_data = {
    "code": 1007,
    "msg": "无权限访问，请检查参数",
    "data": "null",
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}
res = send_method(url=base_url,method="post",json=request_data,headers=headers).json();
print(res);
print(res['code']);
print(expect_data['code']);