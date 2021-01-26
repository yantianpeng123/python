#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/24  7:03 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : bid_page.py
# @Software: PyCharm
'''
#标详情页面
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.base_page import BasePage
from beidouxingUI_Auto_Test.Auto_UI_Project.page_locators.bid_page_locators import BidPageLocators
class BidPage(BasePage):
    name = "标详情页面";

    def invest(self,amount):
        """
            投资功能
        :param amount:
        :return:
        """
        self.wait_element_is_visiable(BidPageLocators.invest_input_locator,'输入投资金额').send_keys(amount);
        # self.wait_element_is_visiable(BidPageLocators.invest_btn_locator,'点击投标按钮').click_element();
        self.wait_element_to_be_clickable(BidPageLocators.invest_btn_locator,'点击投标按钮').click_element();

    def invest_notIsten(self,amount):
        self.wait_element_is_visiable(BidPageLocators.invest_input_locator,'输入投资金额').send_keys(amount);
        # self.wait_element_is_visiable(BidPageLocators.invest_btn_locator,'点击投标按钮').get_element_text();

    def get_pop_error_tip(self):
        """
        获取错误提示信息
        :return:
        """

        return self.wait_element_is_visiable(BidPageLocators.error_tip_locator,'获取错误提示信息').get_element_text()

    def get_bid_blance(self):
       #获取表的可以投资的金额
       return self.wait_element_is_visiable(BidPageLocators.blance_amount_locator,'获取标的可投资余额').get_element_attr('data-left');


    def get_user_blance(self):
        """
        获取用户可用余额
        :return:
        """
        return self.wait_element_is_visiable(BidPageLocators.blance_amount_locator,'获取用户的余额').get_element_attr('data-amount');

    def get_pop_success_tip(self):
        """
        获取投资成功按钮
        :return:
        """
        return self.wait_time(3).wait_element_is_visiable(BidPageLocators.succsee_tip_input_locator).get_element();

    def get_error_tip_notIs(self):
        #获取不是10的倍数按钮
       return self.wait_element_is_visiable(BidPageLocators.invest_btn_locator,'点击投资按钮').get_element_text();