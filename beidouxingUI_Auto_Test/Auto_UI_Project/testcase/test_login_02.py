#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  3:22 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login_02.py
# @Software: PyCharm
'''
"""
    s
"""
import pytest;
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;
from beidouxingUI_Auto_Test.Auto_UI_Project import setting
from time import sleep
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.login_page import LoginPage
from beidouxingUI_Auto_Test.Auto_UI_Project.page_object.home_page import HomePage


#定义一个pytest夹具 来实现数据共享
@pytest.fixture(scope="function")
def driver():
    with webdriver.Chrome() as wd:
        wd.maximize_window();
        yield wd
        wd.quit();


class TestLogin:

    def test_login_01(self,driver):
        driver.get(setting.PROJECT_HOST_VUE + (setting.INTERFACE["login"]));
        # 输入账号和密码
        # 账号
        account = WebDriverWait(driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='phone']")));
        account.send_keys(setting.TEST_NORAML_USERNAME);
        # 密码
        password = WebDriverWait(driver, timeout=3).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")));
        password.send_keys(setting.TEST_NORAML_PASSWORD);
        # 点击登陆
        login_btn = WebDriverWait(driver, timeout=3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='登录']")));
        login_btn.click();
        sleep(3);
        # 验证
        assert WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='退出']")));
        sleep(3)



    def test_03(self,driver):
        LoginPage(driver).login(username=setting.TEST_NORAML_USERNAME,password=setting.TEST_NORAML_PASSWORD);
        sleep(3);
        assert True==HomePage(driver).get_logout_btn();