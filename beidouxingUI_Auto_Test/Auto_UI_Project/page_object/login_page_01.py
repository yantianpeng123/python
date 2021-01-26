#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/23  7:12 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : login_page_01.py
# @Software: PyCharm
'''
#升级版登录页面
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.base_page import BasePage
from beidouxingUI_Auto_Test.Auto_UI_Project.page_locators.login_page_locators import LoginPageLocators


class LoginPage_01(BasePage):
    name = "登录页面"


    def login(self,username,password):
        self.driver.get(self.setting.PROJECT_HOST_VUE + (self.setting.INTERFACE["login"]));
        self.wait_element_is_visiable(LoginPageLocators.username_input_locator,'登录').send_keys(username);
        self.wait_element_is_visiable(LoginPageLocators.password_input_locator,'登录').send_keys(password);
        self.wait_element_is_visiable(LoginPageLocators.login_btn_locator,'登录').click_element();


    def get_error_tip(self):
        error_input_text = self.wait_element_is_visiable(LoginPageLocators.error_input_loc,'获取登录错误提示信息');
        return error_input_text.get_element_text();