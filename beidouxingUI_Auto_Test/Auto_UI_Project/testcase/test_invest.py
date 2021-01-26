#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/24  6:31 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_invest.py
# @Software: PyCharm
'''
#投资测试用例
import pytest
import allure
from time import sleep
from decimal import Decimal
from beidouxingUI_Auto_Test.Auto_UI_Project.common.base_case_test import BaseCase
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.home_page import HomePage
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.bid_page import BidPage
from beidouxingUI_Auto_Test.Auto_UI_Project.testdata.invest_datas import invest_data_fail,success_invest_data,fail_invest_notIsten

class TestInvest(BaseCase):
    name = "投资页面"


    @allure.title('')
    @pytest.mark.parametrize('data',invest_data_fail)
    def test_invest_fail(self,login_driver,data):
        allure.dynamic.title(data['title']);
        login_driver.get(self.setting.PROJECT_HOST_VUE);
        self.driver = login_driver;
        #选择一个标，进入表的详情页面
        hp = HomePage(self.driver).invest_first_bid();
        #进行投资
        bp = BidPage(self.driver).invest(**data['request_data']);

        #断言
        self.beidouxing_assert(data['check_data'],msg=data['title']);



    @allure.title('')
    @pytest.mark.success
    @pytest.mark.parametrize('data',success_invest_data)
    def test_invest_success(self,login_driver,data):
        self.log.info("====={}开始测试=====".format(data['title']));
        allure.dynamic.title(data['title']);
        self.driver = login_driver;
        #保证执行前是在Home页面
        self.driver.get(self.setting.PROJECT_HOST_VUE);
        #选择一个标
        hp = HomePage(self.driver).invest_first_bid();
        user_blance_before_invest = self.get_user_amonut();
        # 标的投资前余额
        bid_blance_before_invest = self.get_bid_amount();
        #进行投资
        bp = BidPage(self.driver).invest(**data['request_data']);
        #断言
        self.beidouxing_assert(check_data=data['check_data'],msg=data['title']);
        #sql校验
        #获取投资后金额
        self.driver.refresh();#刷新页面
        user_blance_after_amount = self.get_user_amonut();
        bid_blance_after_amount = self.get_bid_amount();
        #断言
        # 用户投资前余额-用户投资后余额 = 投资金额
        self.assert_equal((user_blance_before_invest-user_blance_after_amount),Decimal(data['request_data']['amount']))
        #获取标的投资钱
        #标的投资前余额-标的投资后余额 = 投资金额
        self.assert_equal((bid_blance_before_invest-bid_blance_after_amount),Decimal(data['request_data']['amount']));

    @pytest.mark.other
    @allure.title('')
    @pytest.mark.parametrize('data',fail_invest_notIsten)
    def test_invest_fail_notIsten(self,data,login_driver):
        pass;
        self.log.info("====={}:开始测试=====".format(data['title']));
        allure.dynamic.title(data['title']);
        #保持项目在首页
        self.driver = login_driver;
        self.driver.get(self.setting.PROJECT_HOST_VUE);

        hp = HomePage(self.driver).invest_first_bid();
        bp = BidPage(self.driver).invest_notIsten(**data['request_data']);
        # 断言
        self.beidouxing_assert(check_data=data['check_data'],msg=data['title'])
        self.log.info("====={}:结束测试=====".format(data['title']));

    def get_pop_error_tip(self):
        """
        获取错误提示信息
        :return:
        """
        return BidPage(self.driver).get_pop_error_tip();

    def get_user_amonut(self):
       #获取用户的余额
       return Decimal(BidPage(self.driver).get_user_blance());

    def get_bid_amount(self):
        """
        获取标的金额
        :return:
        """
        return Decimal(BidPage(self.driver).get_bid_blance());

    def get_pop_success_tip(self):
        #获取投资成功按钮
       try:
           if BidPage(self.driver).get_pop_success_tip():
               return True
       except Exception as e:
           return False;

    def get_error_tip_notIs(self):
        """
        获取不是10的倍数按钮内容
        :return:
        """
        return BidPage(self.driver).get_error_tip_notIs()