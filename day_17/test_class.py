#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/11  2:48 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_class.py
# @Software: PyCharm
'''

import pytest
class TestClass:

    def test_one(self):
        x = "this";
        assert "h" in x;

    def test_two(self):
        x = "hello";
        assert  hasattr(x,"check");


pytest.main();
