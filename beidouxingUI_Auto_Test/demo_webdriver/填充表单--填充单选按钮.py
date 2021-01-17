#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/17  4:38 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 填充表单--填充单选按钮.py
# @Software: PyCharm
'''
from selenium import webdriver
from time import sleep;
from selenium.webdriver.common.by import By;

with webdriver.Chrome as driver:
    #打开网址
    driver.get("https://www.w3school.com.cn/tiy/t.asp?f=html_radiobuttons");
    #切换iframe
    iframe =  driver.find_element(By.XPATH,'//iframe[@id="iframeResult"]');
    driver.switch_to.frame(iframe);
    #获取单选框元素的位置
    radio_btn = driver.find_element(By.XPATH,"//input[@value='female']")
    #点击选中该元素
    radio_btn.click();
    sleep(10);