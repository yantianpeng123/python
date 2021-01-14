#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/30  9:04 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method.py
# @Software: PyCharm
'''

# def 函数名字(参数1，参数2):
#     函数体
#     return 返回值

# 案例:打招呼
# hello 小明
# hello 小红
# hello 小黑
print('hello 小明');
print('hello 小红');
print('hello 小黑');
#定义一个函数
def happy():
    print("hello");

#定义一个函数
def happy_name(name):
    print('hello '+name);


#函数的调用
happy();
happy_name('zhangsan');