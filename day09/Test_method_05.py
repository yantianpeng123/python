#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/15  10:12 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_05.py
# @Software: PyCharm
'''
#类的继承
#当我们定义一个类的时候我们可以从现有的类继承，新的类被称为子类，被继承的类被称为父类或者基类,超类
#子类可以继承父类的属性和方法。
#创建一个表示三维里的点
class Point:

    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __str__(self):
        return ('{},{}'.format(self.x, self.y));

    def my_print(self):
        print('{},{}'.format(self.x, self.y));



class Tdpoint(Point):#括号里面写上父类表示的是需要继承的父类，会得到子类的所有的属性和方法

    def __init__(self,x,y,z):#子类继承父类并且方法的名称和父类的是一样的，里面参数是不一样的，把父类的方法给覆盖掉了就是重写
        self.x = x;
        self.y = y;
        self.z = z;

    def my_print(self):
        super().my_print();#在子类中调用和父类同名的方法，使用super();
        print('{},{},{}'.format(self.x,self.y,self.z))

    # super重写了父类的方法但是又要调用父类的方法


