#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/29  9:55 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_while.py
# @Software: PyCharm
'''
#从0依次打印小于n的整数 ，n是一个大于0的整数
n =  int(input("请输入你要打印的整数"));
i = 0;
while i<n:
    print(i);
    i+=1;


#使用while循环来循环列表
ls  =  list('asdfghjkl');
print(ls);
i = 0;
while i<len(ls):
    print(ls[i]);
    i+=1;

#while循环来循环字典
dc = {
    "name":"闫天蓬",
    "age":18,
    "sex":"男",
    "score":87
}

i = 0;
while i<len(dc):
    print(dc[list(dc.keys())[i]]);
    i+=1;