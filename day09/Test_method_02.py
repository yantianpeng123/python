#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/14  11:07 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_02.py
# @Software: PyCharm
'''

#定义一个my_print函数打印坐标系的x和y的坐标
class Point:
    x = 1;
    y = 2;
    '''
        定义类中的普通的方法就是函数
    '''
    def my_print(Point):
        print('{},{}'.format(Point.x, Point.y));

    '''
    定义成一个类方法
    '''
    @classmethod
    def base_point(cls):
        bp =  cls();
        bp.x = 0;
        bp.y = 0;
        return bp;

p = Point();
p.x = 10;
p.y = 20;
#对象方法的调用 对象.方法名(); 通过对象去调用对象方法的时候，会隐式的把对象传到该方法中。所以对象方法会把第一个参数定义为self。
p.my_print();