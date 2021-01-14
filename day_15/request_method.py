#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/23  9:33 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : request_method.py
# @Software: PyCharm
'''
import requests;
'''
发起请求的步骤
1。url
2。请求方法
3。请求头
4。请求体(body里面的参数)
'''
res = requests.get('https://www.baidu.com/');
#状态码
print(res.status_code);
#响应数据
print(res.content);
#文本属性
res.encoding='utf-8';
print(res.text);
#headers属性 获取响应头

print(res.headers);

#获取url
print(res.url);
