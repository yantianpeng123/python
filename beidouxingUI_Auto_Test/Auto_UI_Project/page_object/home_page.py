#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  4:58 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : home_page.py
# @Software: PyCharm
'''
from beidouxingUI_Auto_Test.Auto_UI_Project.page_locators.home_page_locators import HomePageLocators
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.base_page import BasePage

class HomePage(BasePage):
    name = "首页"



    def __init__(self,driver):
        self.driver =driver;

    def get_logout_btn(self):
        """
        查找退出按钮是否存在 存在的话返回True
        否则是False
        :return:
        """

        # WebDriverWait(self.driver, timeout=3).until(
        #         EC.visibility_of_element_located(HomePageLocators.logout_btn_locator)
        # );
        return  self.wait_element_is_visiable(HomePageLocators.logout_btn_locator,'获取首页退出按钮').get_element()

    def invest_first_bid(self):

        self.wait_element_is_visiable(HomePageLocators.first_bid_invest_locator,'选择第一个进行投标').click_element();