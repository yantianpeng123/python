#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/4  10:24 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_class.py
# @Software: PyCharm
'''
'''
class 类名:
    属性
    方法/函数
    类名规则 一般是大驼峰命名字
'''
#表示平面坐标系的一个点
class point:
    '''

    '''
    name ='闫天蓬';

print(type(point))

#对象的实例化 类名加括号
p = point();
#访问 类名.属性名();
#访问 对象.属性名()
print(p.name)