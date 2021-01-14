#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/11  2:30 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_sample.py
# @Software: PyCharm
'''

import pytest

def fun(x):
    return x+1;

def test01_fun():
    assert fun(3)==5;

def test02_fun():
    return fun(3)==4;

pytest.main();