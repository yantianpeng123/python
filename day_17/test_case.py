#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/13  6:02 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_case.py
# @Software: PyCharm
'''

import pytest




#定义夹具
@pytest.fixture()
def function_fixture():
    print("我是一个函数级的前置");
    yield 4 # 带有返回值 在调用的时候按照参数传进去
    print("我是一个函数级别的后置");




@pytest.fixture()
def function_no_return_fixture():
    print("我是第二个函数级别的前置");
    yield #不带有返回值
    print("我是第二个函数级别的后置");


@pytest.fixture(scope="class")
def class_fixture():
    print("我是一个类级前置");
    yield
    print("我是一个类级后置");


def fun(x):
    return x+3;

@pytest.mark.usefixtures("function_fixture")
def test_fun():
    print("=====我是测试函数========");
    assert fun(1)==function_fixture;


@pytest.mark.usefixtures("function_no_return_fixture")
def test_fun_01():
    print("我是第二个测试函数");
    assert fun(1) ==5;


@pytest.mark.usefixtures("class_fixture")
class TestCase:


    def test_01(self, function_no_return_fixture):
        print("我是测试方法--one---")
        x ="hello";
        assert  "h" in x;

    def test_02(self,function_fixture):
        x= "hello";
        assert  hasattr(x,"hello");



if __name__ == '__main__':
    pytest.main()