#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/15  9:56 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_03.py
# @Software: PyCharm
'''
#特殊方法，有特殊功能的方法，都是一双下滑线开头的。
# __init__ 初始化方法，构造方法对象属性一般都定义在里面,
#当创建对象时候他会被自动调用，创建的对象会被传递给第一个参数
# 会接受类名括号里传入的参数(从第二个参数开始传递)

#__str__();
#print()一个对象的时候，实际上调用这个对象的__str__()方法，打印这个方法的返回值。

class Point:
    def __init__(self,x,y):
        self.x = x;
        self.y =y;

    def __str__(self):
        return ('{},{}'.format(self.x,self.y));

    def my_print(self):
        print('{},{}'.format(self.x,self.y));

#创建对象point 同时给x和y传递值

p1 = Point(1,2);
p1.my_print();

print(p1);

