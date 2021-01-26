#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  2:43 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login_01.py
# @Software: PyCharm
'''
"""
    问题:
        1.代码冗余度很高，每个功能都要写很多的多余的代码
        2.代码耦合度很高,页面有一点修改就要修改大量的代码
        
"""
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;
from beidouxingUI_Auto_Test.Auto_UI_Project import setting
from time import sleep
#登陆页面
class TestLogin:

    username_input_locator = (By.XPATH,"//input[@name='phone']");
    password_input_locator = (By.XPATH,"//input[@name='password']");
    login_btn_locator =  (By.XPATH,"//button[text()='登录']");

    def test_login(self):
        with webdriver.Chrome() as driver:
            #访问页面
            driver.get(setting.PROJECT_HOST_VUE+(setting.INTERFACE["login"]));
            #输入账号和密码
            #账号
            account =WebDriverWait(driver,timeout=3).until(
                EC.visibility_of_element_located(self.username_input_locator)
            );
            account.send_keys(setting.TEST_NORAML_USERNAME);
            #密码
            password = WebDriverWait(driver,timeout=3).until(
                EC.visibility_of_element_located(self.password_input_locator)
            );
            password.send_keys(setting.TEST_NORAML_PASSWORD);
            #点击登陆
            login_btn =  WebDriverWait(driver,timeout=3).until(
                EC.element_to_be_clickable(self.login_btn_locator)
            );
            login_btn.click();
            sleep(3);
            #验证
            assert  WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='退出']")));



