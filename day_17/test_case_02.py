#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/13  8:11 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_case_02.py
# @Software: PyCharm
'''
import pytest;

#运行于测试用例类的始末 只会在测试用例的类执行一次

class Test_abc_01:

    def setup_class(self):
        print("setup_class");

    def teardown_class(self):
        print("---teardown_class");

    def test_01(self):
        print("---test_01----");
        assert 1;

    def test_02(self):
        print("----test_02-----");
        assert 2;


if __name__ == '__main__':
    pytest.main();
