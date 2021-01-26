#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  7:56 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login_05.py
# @Software: PyCharm
'''
#第五版测试
import pytest
from beidouxingUI_Auto_Test.Auto_UI_Project.common.base_case_test import BaseCase
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.login_page import LoginPage
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.home_page import HomePage
from beidouxingUI_Auto_Test.Auto_UI_Project.testdata.login_datas import success_datas,fail_datas;


"""
    需要注意的是我们把错误的失败用例放在前面执行，否则的话用例会执行不成功
    如果我们需要把成功的测试用例放到前面执行的话，我们需要在哎Home_Page页面一个退出方法，
    并且在成功的用例执行结束之后调用该退出方法，使页面退出到登录页面
"""

class TestLogin(BaseCase):
    name = "登录模块"


    @pytest.mark.parametrize('data', fail_datas)
    def test_login_fail(self, driver, data):
        self.log.info("====>>{}:开始测试<<<====".format(data['title']))
        self.driver = driver;
        lp = LoginPage(driver);
        lp.login(**data['request_data']);
        # 调用断言方法 我们不需要在此处判断
        self.is_login_assert(data['check_data']);
        self.log.info("====>>{}:结束测试<<<====".format(data['title']))

    @pytest.mark.parametrize('data',success_datas)
    def test_login_success(self,driver,data):
       self.log.info("====>>{}:开始测试<<<====".format(data['title']))
       self.driver = driver
       lp =  LoginPage(driver);
       lp.login(**data['request_data']);
       #断言
       #1.取出data方法，进行执行
       #2.判断执行结果是否和预期结果相等
       # method  =  getattr(self,data['check_data']['method'])#动态获取参数方法
       # assert method() == data['check_data']['value'];
       self.is_login_assert(data['check_data']);
       self.log.info("====>>{}:结束测试<<<====".format(data['title']))






    def is_login_assert(self,check_data):
        """
        实现动态断言
        :param check_data:
        :return:
        """
        method = getattr(self,check_data['method']);
        assert method()==check_data['value'];

    def get_error_tip(self):
        lp = LoginPage(self.driver)
        return lp.get_error_tip();

    #在页面对象值不做断言判断
    def is_login(self):
        """
        判断是否登录
        :param driver:
        :return:
        """
        hp = HomePage(self.driver)
        try:
            hp.get_logout_btn();
            return True
        except Exception as e:
            return False
