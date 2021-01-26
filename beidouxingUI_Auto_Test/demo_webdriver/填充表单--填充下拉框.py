#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/17  4:54 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 填充表单--填充下拉框.py
# @Software: PyCharm
'''
from selenium import webdriver;
from time import sleep
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.select import Select

#切换下拉框
with webdriver.Chrome() as driver:
    driver.get("https://www.w3school.com.cn/tiy/t.asp?f=html_select"); #打开网址
    #切换iframe
    ifram =  driver.find_element(By.ID,"iframeResult");
    driver.switch_to.frame(ifram);
    sleep(1);
    #1.通过value的属性去找xpath
    audi =driver.find_element(By.XPATH,"//option[@value='audi']");
    audi.click();
    sleep(2);
    #通过Select类找

    select_01 = Select(driver.find_element(By.TAG_NAME,"select"));
    #使用索引去查找 索引是从0开始的
    select_01.select_by_index(1);
    sleep(2)
    #通过text的可见的值来选择
    select_01.select_by_visible_text("Opel");
    sleep(2)
    #通过value的值来选择
    select_01.select_by_value("volvo");
    sleep(2);

    driver.quit();