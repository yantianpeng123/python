#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/20  7:39 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 执行Js代码--滚动1.py
# @Software: PyCharm
'''
from selenium import webdriver;
from time import sleep;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.common.by import By;


with webdriver.Chrome() as driver:
    driver.get("https://image.baidu.com/");
    #定位搜索框
    search_input =  WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='kw']")));
    search_input.send_keys("闫天蓬");
    search_btn =  WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@value='百度一下'and@class='s_newBtn']")));
    search_btn.click();
    sleep(3)
    #向下滚动指定的坐标
    driver.execute_script("window.scrollTo(0,200)");
    sleep(3)
    # 向下滚动指定的坐标
    driver.execute_script("window.scrollTo(0,300)");
    sleep(3)
    # 向下滚动指定的坐标
    driver.execute_script("window.scrollTo(0,10000)");
    sleep(3);
    #滚动到顶部
    driver.execute_script("window.scrollTo(0,0)");
    sleep(6)
    #滚动到底部
    # driver.execute_script("window.scrollTo(0,document.body.scrollToHeight)");

    sleep(9)
    driver.quit();