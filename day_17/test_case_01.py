#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/13  8:06 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_case_01.py
# @Software: PyCharm
'''
#pytest
import  pytest
class Test_abc:

    '''
        函数级别的前置 运行于每个测试函数始末 每一个测试函数都会运行
    '''
    def setup(self):
        print("------>>>>setup_method");

    def teardown(self):
        print("----->>>teardown_method");


    def test_01(self):
        print("----->>>我是test_01------>>>>")
        assert 1;

    def test_02(self):
        print("----->>>我是test_02----->>>>");
        assert 1;



if __name__ == '__main__':
    pytest.main();