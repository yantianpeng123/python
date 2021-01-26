#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  7:07 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : login_page_locators.py
# @Software: PyCharm
'''
from selenium.webdriver.common.by import By;


class LoginPageLocators:
    """
    登录页面定位信息
    """
    username_input_locator = (By.XPATH, "//input[@name='phone']");
    password_input_locator = (By.XPATH, "//input[@name='password']");
    login_btn_locator = (By.XPATH, "//button[text()='登录']");

    #错误信息提示框
    error_input_loc =(By.XPATH,"//div[@class='form-error-info']");