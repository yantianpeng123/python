#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/16  6:08 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_mokuai_02.py
# @Software: PyCharm
'''
from day09.Test_mokuai_01 import fib;#在导入模块的时候尽量使用从上一级的目录开始
from day09.Test_mokuai_01 import fib2;
#from 模块名 import * 表示倒入该模块中全部方法和属性
# from day09.Test_mokuai_01 import *

res = fib2(2);
print(res);
fib(2);#模块名.函数名();

