#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/17  4:32 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 填充表单--填充文本框.py
# @Software: PyCharm
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("http://www.baidu.com");
    search_input = driver.find_element(By.ID,"kw")
    #填充文本框使用的send_keys("文本内容");
    search_input.send_keys("闫天蓬 讲师");
    search_button =  driver.find_element(By.XPATH,"//input[@id='su']");
    #点击按钮操作
    search_button.click();
    sleep(5);
    driver.quit();