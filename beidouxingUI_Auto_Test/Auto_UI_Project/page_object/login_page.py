#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  5:04 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : login_page.py
# @Software: PyCharm
'''
from selenium.webdriver.remote.webdriver import WebDriver
from beidouxingUI_Auto_Test.Auto_UI_Project import setting
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;
from time import sleep
from beidouxingUI_Auto_Test.Auto_UI_Project.page_locators.login_page_locators import LoginPageLocators
from beidouxingUI_Auto_Test.Auto_UI_Project.common.login_handler import log

class LoginPage:

    name="登录页面";
    log =log;

    @classmethod
    def setup_class(cls):
        cls.log("====>>{}测试开始<<===".format(cls.name));

    @classmethod
    def teardown_class(cls):
        cls.log("====>>测试结束{}===".format(cls.name));


    def __init__(self,driver: WebDriver):
        self.driver =  driver;


    def login(self,username,password):
        self.driver.get(setting.PROJECT_HOST_VUE + (setting.INTERFACE["login"]));
        # 输入账号和密码
        # 账号
        account = WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(LoginPageLocators.username_input_locator)
        );

        account.send_keys(username);
        # 密码
        password_input = WebDriverWait(self.driver, timeout=3).until(
            EC.visibility_of_element_located(LoginPageLocators.password_input_locator)
        );
        password_input.send_keys(password);
        # 点击登陆
        login_btn = WebDriverWait(self.driver, timeout=3).until(
            EC.element_to_be_clickable(LoginPageLocators.login_btn_locator)
        );
        login_btn.click();
        sleep(3);


    def get_error_tip(self):
        """
        获取错误信息
        :return:
        """
        error_input = WebDriverWait(self.driver,timeout=3).until(
            EC.visibility_of_element_located(LoginPageLocators.error_input_loc)
        );
        return error_input.text