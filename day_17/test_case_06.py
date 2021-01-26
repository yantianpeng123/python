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
test_data = [("3+5",8),("2+4",6),("6*9",24)];


@pytest.mark.parametrize("data",test_data)
def test_eval(data):
    assert eval(data[0])==data[1];


# @pytest.mark.parametrize("test_input,expect",test_data) #类似于字典的解包
# def test_eval_01(test_input,expect):
#     assert eval(test_input==expect);
import os
if __name__ == '__main__':
    #pytest + allure 运行步骤
    # pytest --alluredir report  运行测试用户并且生成测试报告 report使用的是相对路径
    # allure serve report 启动allure服务 查看测试报告

    pytest.main(["-s","-v","--alluredir=report"]);
