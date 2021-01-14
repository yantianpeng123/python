#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/11  2:46 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_sysexit.py
# @Software: PyCharm
'''
import pytest

def f():
    raise SystemExit(1);


def test_mytest():
    with pytest.raises(SystemExit):
        f();


pytest.main()