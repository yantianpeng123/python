#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/23  7:07 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login_06.py
# @Software: PyCharm
'''
#第六版
from beidouxingUI_Auto_Test.Auto_UI_Project.testdata.login_datas import fail_datas,success_datas
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.login_page_01 import LoginPage_01
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.home_page import HomePage
from beidouxingUI_Auto_Test.Auto_UI_Project.common.base_case_test import BaseCase
import pytest
class TestLogin(BaseCase):
    name = "登录页面";

    @pytest.mark.parametrize('data',fail_datas)
    def test_login_fail(self,driver,data):
        self.driver =driver;
        lp  = LoginPage_01(self.driver);
        lp.login(**data["request_data"]);
        self.login_assert(check_data=data['check_data']);

    @pytest.mark.parametrize('data',success_datas)
    def test_login_success(self,driver,data):
        self.driver = driver;
        lp = LoginPage_01(self.driver);
        lp.login(**data["request_data"]);
        self.login_assert(check_data=data['check_data']);



    def login_assert(self,check_data):
        """
        自定义登录断言
        :param check_data:
        :return:
        """
        method =  getattr(self,check_data['method']);
        assert method() ==check_data['value'];

    def get_error_tip(self):
        """
        获取错误提示信息
        :return:
        """
        lp = LoginPage_01(self.driver)
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