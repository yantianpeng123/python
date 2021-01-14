#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/14  7:02 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_case_06.py
# @Software: PyCharm
'''
import pytest
test_data = [("3+5",8),("2+4",6),("6*9",42)];


@pytest.mark.parametrize("data",test_data)
def test_eval(data):
    assert eval(data[0])==data[1];


if __name__ == '__main__':
    pytest.main(["-s" "-v","test_case_06.py"]);
