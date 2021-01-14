#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/14  2:15 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_case_04.py
# @Software: PyCharm
'''
import pytest

@pytest.fixture(scope="function",autouse=True,params=[1,3,4])
def before(request):
    print("我是测试夹具，在测试开始之前执行...")
    yield request.param # 在使用返回值的时候必须作为参数传到需要接受的方法中


class Test_abc_03:

    def test_01(self,before):
        print("----->>>>我是测试方法<<<<----");
        assert 3 == before;



if __name__ == '__main__':
    pytest.main();
