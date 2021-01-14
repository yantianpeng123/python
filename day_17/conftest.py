#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/14  4:07 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : conftest.py
# @Software: PyCharm
'''
# 共享夹具
import pytest


#定义共享夹具
@pytest.fixture()
def log():
    print("---->>>开始测试<<<-----");
    yield
    print("--->>>结束测试<<<------");


@pytest.fixture
def duration():
    print("耗时多少秒---");
    yield
    print("测试结束---")