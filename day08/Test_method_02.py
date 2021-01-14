#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/31  7:19 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_02.py
# @Software: PyCharm
'''
#作业；
# 实现is_add()函数，接受一个整数，如果是奇数返回True，否则返回False
def is_add(a):
    if a%2 == 0:
        return True;
    else:
        return False;

# 实现is_num()函数，参数为一个字符串，如果这个字符串属于整数或者浮点数，则返回True 否则返回False
def is_num(s):
    if isinstance(s,int) or isinstance(s,float):
        return True;
    else:
        return False;

#实现multi()函数    ，最少接受两个参数，返回所有参数的乘积
def multi(a,b,*args):
    multi_01 = a*b;
    for _ in args:
        multi_01*=_;
    return multi_01;
print(multi(1,2,3));

#实现is_prime()函数，参数为整数，要有异常处理，如果是质数返回True，否则返回False
def is_prime(a):
    try:
        if a<=1:
            return False;
        for _ in range(2,a):
            if a % _ ==0:
                return False;
        return True;
    except:
        print('传入的参数不是整数');

print(is_prime(3));
a = is_add(3);
print(a)
b = is_num(2);
print(b);