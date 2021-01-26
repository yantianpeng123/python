#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/17  11:31 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 元素等待.py
# @Software: PyCharm
'''
"""
浏览器在渲染页面的时候需要时间，如果没有渲染完成对元素进行定位将会找不到该元素
所以需要加延时进行等待，有三种等待方式
1.time.sleep(秒数) 使程序在当前位置暂停，如果在项目中多次使用会造成程序的效率底下
2.显式等待
    显式等待就是在元素操作的钱循环判断操作的条件是否满足，满足后在操作
    selenium通过from selenium.webdriver.support.ui import WebDriverWait 类来实现显式等待。
    WebDriverWait 类实例化可以接受三个参数
        - driver webdriver对象
        - timeout 超时时间，就是最多等待多少秒
        - poll_frequency 检查频率，默认式0.5秒
        条件在selenium.webdriver.support.expected_conditions  模块中
    until中的条件
        常见的条件:
            - presence_of_element_located 元素存在于dom中
            - visibility_of_element_located 元素可见
            - element_to_be_clickable 元素可点击
            - element_to_be_selected 元素可选择
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC;
from selenium.webdriver.common.by import By
from time import sleep

with webdriver.Chrome() as driver:
    driver.get("https://www.baidu.com");
    search_input = driver.find_element(By.ID,"kw");
    search_input.send_keys("闫天蓬 讲师");
    sleep(2) #程序再次暂停
    search_btn = driver.find_element(By.XPATH,"//input[@id='su']");
    search_btn.click();
    #显式等待
    first_url = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='1']/h3/a")));
    first_url.click();
    sleep(2);

    driver.quit();