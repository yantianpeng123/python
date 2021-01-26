#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/18  3:21 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : prompt框.py
# @Software: PyCharm
'''
from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;
from time import sleep


with webdriver.Chrome() as driver:
    driver.get("https://www.runoob.com/try/try.php?filename=tryjs_prompt");
    #切换iframe
    iframe= WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//iframe[@id='iframeResult']")));
    driver.switch_to.frame(iframe);
    #查找点击按钮
    btn =  WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.TAG_NAME,"button")));
    btn.click();
    sleep(3)
    WebDriverWait(driver,timeout=3).until(EC.alert_is_present());
    send_input = driver.switch_to.alert
    send_input.send_keys("闫天蓬"); #再提示框里面的显示的内容不会改变
    send_input.accept();
    sleep(9)
    driver.quit();