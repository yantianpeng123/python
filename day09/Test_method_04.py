#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/15  10:07 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_04.py
# @Software: PyCharm
'''
#静态方法:
#在类中通过staticmethod可以把一个函数定义为一个静态方法
# 静态方法不会接受隐式的第一个参数，他和普通函数是一样，只是被封装到类里面
# 通过类对象就可以调用

class Point:
    @staticmethod
    def sum_01(x,y):
        return x+y;





p1 = Point().sum_01(1,2);
print(p1);


