#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  7:11 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : home_page_locators.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By;

class HomePageLocators:
    #首页退出定位
    logout_btn_locator = (By.XPATH, "//a[text()='退出']");

    #第一个标的抢投标按钮
    first_bid_invest_locator =(By.XPATH,"//div[@class='b-unit-list clearfix']/div[2]//a[text()='抢投标']");
