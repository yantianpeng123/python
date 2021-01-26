#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/20  8:52 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 上传文件_input框.py
# @Software: PyCharm
'''
#文件上传input框
from selenium import webdriver
from time import sleep;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;

with webdriver.Chrome() as driver:
    driver.get("https://www.baidu.com");
    soutu_btn =WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='soutu-btn']")));
    soutu_btn.click();
    sleep(2);
    # tupian = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='upload-pic']")));
    tupian = driver.find_element(By.XPATH,"//input[@class='upload-pic']");
    # tupian_01 = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@class='upload-pic']")));
    #在此处需要写图片的绝对路径
    tupian.send_keys("/Users/yantianpeng/Desktop/1.jpg");
    sleep(9);
    driver.quit();
