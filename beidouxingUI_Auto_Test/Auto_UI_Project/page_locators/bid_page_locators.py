#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/24  7:05 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : bid_page_locators.py
# @Software: PyCharm
'''
#标详情页面
from selenium.webdriver.common.by import By


class BidPageLocators:

    #投资输入框
    invest_input_locator = (By.XPATH,"//div[@class='in']/div/input");
    #投标按钮
    # invest_btn_locator = (By.XPATH,"//button[text()='投标']");
    invest_btn_locator = (By.XPATH,"//div[@class='pd-right']//button");
    #投标按钮不可点击
    invest_btnenble_locator = (By.XPATH,"//div[@class='pd-right']//button");

    #获取错误提示信息
    error_tip_locator = (By.XPATH,"//div[@id='layui-layer1']//div[@class='text-center']");

    #用户余额
    blance_amount_locator = (By.XPATH,"//div[@class='in']/div/input");

    #查看用户
    succsee_tip_input_locator = (By.XPATH,"//div[contains(@id,'layui-layer')]//button");