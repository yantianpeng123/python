#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/31  7:55 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_03.py
# @Software: PyCharm
'''
#lamdba函数
ls = [('大杏子',100),('点点',99),('曹66',80)]
ls.sort();
print(ls);

def sort_by(item):
    return item[1];

ls.sort(key=sort_by);
print(ls)

ls_01 = [('大杏子',100),('点点',99),('曹66',80)]
lambda item:item[1];# 相当于上面的sort_by
ls_01.sort(key=lambda item:item[1]);
print(ls_01);

def is_add(x,y):
    return x+y;
# 冒号前面的x,y表示的是参数，冒号后面的表示的返回值
aa = lambda x,y:x+y;
print(aa(1,2))


a = 1;
b = 2;