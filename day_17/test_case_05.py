#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/14  3:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_case_05.py
# @Software: PyCharm
'''
import pytest



def fun(x):
    return x+1;

@pytest.mark.usefixtures("log")
def test_fun():
    assert 3 ==fun(2);


@pytest.mark.usefixtures("log")
def test_answer():
    assert 3 ==5



@pytest.mark.usefixtures("log","duration")
def test_answer_01():
    print("<<<---测试---->>>>")
    assert 3==3;
if __name__ == '__main__':
    pytest.main("-s","-v");