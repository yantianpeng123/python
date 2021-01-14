#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/16  6:06 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_mokuai_01.py
# @Software: PyCharm
'''
def fib(n):
    a,b = 0,1;
    while a<n:
        print(a,end=' ');
        a,b = b,a+b;
    print();

def fib2(n):
    result = [];
    a,b = 0,1;
    while a<n:
        result.append(a);
        a,b = b,a+b;
    return result;