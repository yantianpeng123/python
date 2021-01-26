#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/17  10:51 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 切换窗口和标签页.py
# @Software: PyCharm
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By;

#webdriver 不区分窗口和标签页，打开一个新的标签页或者窗口，selenium会使用窗口切换句柄来处理
# 每一个窗口都有一个唯一的标识符号,该标识符在单个会话中保持持久性
# 1获取当前窗口句柄
# driver.current_window_handle
# 2 切换窗口或者标签页 使用循环遍历的方式来切换
with webdriver.Chrome() as driver:
    driver.get("https://www.baidu.com");

    search_input = driver.find_element(By.ID,"kw");
    search_input.send_keys("闫天蓬 讲师");

    search_btn =  driver.find_element(By.XPATH,"//input[@id='su']");
    search_btn.click();
    sleep(2);
    #获取当前的窗口
    origin_handle = driver.current_window_handle;
    print("当前窗口的句柄是{}".format(origin_handle));
    print("当前窗口的标题是{}".format(driver.title));
    #点击搜索的第一个连接
    first_url = driver.find_element(By.XPATH,"//div[@id='1']/h3/a");
    first_url.click();
    sleep(3)
    #driver.window_handles 获取当前所有的活动窗口或者标签页
    #循环遍历切换窗口
    for handle in driver.window_handles:
        if handle !=origin_handle:
            driver.switch_to.window(handle);
            break;

    print("新打开的窗口句柄是:{}".format(driver.current_window_handle));
    print("新打开的窗口的标题是:{}".format(driver.title));
    sleep(4)
    driver.quit();
