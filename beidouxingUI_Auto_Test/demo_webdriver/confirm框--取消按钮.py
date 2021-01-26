#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/18  2:49 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : confirm框--取消按钮.py
# @Software: PyCharm
'''
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;
from time import sleep

with webdriver.Chrome() as driver:
    driver.get("https://www.runoob.com/try/try.php?filename=tryjs_confirm");
    #切换iframe
    iframe = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//iframe[@id='iframeResult']")));
    driver.switch_to.frame(iframe);
    #点击按钮
    btn =  WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.TAG_NAME,"button")));
    btn.click();

    #切换到弹出框
    driver.switch_to.alert;
    alter = WebDriverWait(driver,timeout=3).until(EC.alert_is_present());#等待弹出框出现
    sleep(1)
    print(alter.text)
    alter.dismiss();#点击取消按钮
    sleep(9)