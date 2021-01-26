#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/18  2:30 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : confirm框.py
# @Software: PyCharm
'''
"""
    和警告框不同的是confirm还有一个取消按钮
"""
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from time import sleep


with webdriver.Chrome() as driver:
    #打开网址
    driver.get("https://www.runoob.com/try/try.php?filename=tryjs_confirm");
    #切换iframe
    iframe = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//iframe[@id='iframeResult']")));
    driver.switch_to.frame(iframe);
    btn = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.TAG_NAME,"button")));
    btn.click();

    driver.switch_to.alert

    alter =  WebDriverWait(driver,timeout=3).until(EC.alert_is_present());
    # text =  btn.text;
    # print(text);
    sleep(9);
    alter.accept();

    sleep(9);

    driver.quit();
