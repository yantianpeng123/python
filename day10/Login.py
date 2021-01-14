#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/17  2:48 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Login.py
# @Software: PyCharm
'''
def login_check(username,password):
    """
        模拟用户的登录
    :param username:
    :param password:
    :return:
    """
    if 6<=len(password)<=18:
        if username =='amdin' and password=='beidouxing':
            return {'code':'0','msg':'登录成功'};
        else:
            return {'code':'1','msg':'账号密码不匹配'};
    else:
        return {'code':'2','msg':'密码长度请在6到18之间'};