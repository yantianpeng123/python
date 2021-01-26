#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/18  12:10 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : 警告框.py
# @Software: PyCharm
'''
'''
Webdriver提供了一个API，用于处理JavaScript提供的三种类型的原生弹窗的消息
1.Alerts 警告框
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.common.by import By
from time import sleep


with webdriver.Chrome() as driver:
    #打开网址
    driver.get("https://www.w3school.com.cn/tiy/t.asp?f=hdom_alert");
    #切换iframe
    driver.switch_to.frame(1);
    #查找弹出框按钮并点击
    sleep(1);
    # aa =driver.find_element(By.XPATH,"//input[@type='button']");
    # aa.click();
    # locater = "//input[@type='button']";
    #元素显式等待
    aa= WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@type='button']")));
    aa.click();#d点击确定按钮
    alter = WebDriverWait(driver,timeout=3).until(EC.alert_is_present());#查找大当前的警告框
    driver.switch_to.alert;#切换到警告框
    alter_text=alter.text;#获取警告框的内容
    print(alter_text);
    sleep(5);
    alter.accept(); #点击警告框确定按钮

    sleep(9)
    driver.quit();