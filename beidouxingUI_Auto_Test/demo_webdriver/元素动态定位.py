#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/16  11:33 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 元素动态定位.py
# @Software: PyCharm
'''

from  selenium import webdriver;
from time import sleep
from selenium.webdriver.common.by import By;


"""
动态定位通过选择定位当时来实现
把定位方式封装称一个类来动态选择
"""


driver = webdriver.Chrome();
driver.get("http://www.baidu.com");

id_loc="kw"; #通过id定位
xpathsearch = "//input[@id='kw']" #通过xpath定位
xpath_loc="//input[@id='su']";

e1 = driver.find_element(By.ID,id_loc) #通过ID定位
e1.send_keys("元素动态定位"); #像输入框输入数据
sleep(3);

e2 =  driver.find_element(By.XPATH,xpathsearch);
e2.clear();#清空输入框的内容
e2.send_keys("我通过xpath定位");

sleep(3);
e3 = driver.find_element(By.XPATH,xpath_loc);
e3.click()# 点击按钮
sleep(3);

driver.quit();