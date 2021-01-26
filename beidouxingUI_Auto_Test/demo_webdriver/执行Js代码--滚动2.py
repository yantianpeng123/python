#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/20  8:04 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 执行Js代码--滚动2.py
# @Software: PyCharm
'''
#selenium 执行js有几个方法，这里我们使用最常用的方法execute_script
# 执行js时候,还可以传递参数给js脚本
# 下面的案例：
# 打开页面，并滚动到指定的元素可见
# 下面的代码div被传递给啦arguments,通过切片的方式取出


from time import sleep;
from selenium import webdriver
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;

with webdriver.Chrome() as driver:
    driver.get("https://www.w3school.com.cn/js/js_htmldom_events.asp");
    sleep(2);

    js_a = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//a[text()='JS 日期']")));
    #移动到当前元素的低端与当前窗口的底部对齐
    driver.execute_script("arguments[0].scrollIntoView(false)",js_a);
    sleep(9);
    #移动到当前元素的顶端与当前窗口顶部对齐
    driver.execute_script("arguments[0].scrollIntoView(true)",js_a);
    sleep(9);
    driver.quit()
