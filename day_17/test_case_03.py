#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/14  1:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_case_03.py
# @Software: PyCharm
'''
import pytest


@pytest.fixture(scope="function",autouse=True)
def before():
    print("我是测试夹具,在测试开始之前执行");
    yield
    print("在测试结束之后开始执行")

def test_02():
    print("----->>>>我是测试函数2<<<<---")


class Test_abc_02:

    '''
        scope :被标记放的作用域
        function: 作用于每个测试方法，每个test执行一次
        class:作用域整个类 每个class 类的所有的test值运行一次
        module:作用域整个模块，每个module的所有test只运行一次
        session:作用域真个session，每个session只运行一次

        autouse: 是否自动运行 默认是False 不运行 设置为True自动运行

    '''
    # @pytest.fixture(scope="function",autouse=True)
    # def before(self):
    #     print("在测试执行之前开始执行");

    # @pytest.mark.usefixtures("before")
    def test_a(self):
        print("---->>>我是测试方法a<<<----");
        assert 1;

if __name__ == '__main__':
    pytest.main();