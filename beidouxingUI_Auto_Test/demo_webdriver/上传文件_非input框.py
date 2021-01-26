#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/20  9:25 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 上传文件_非input框.py
# @Software: PyCharm
'''
from selenium import webdriver;
from time import sleep;
from selenium.webdriver.common.by import By;
import pyautogui
'''
selenium 文件上传 不是input框 我们使用pyautogui框

'''

with webdriver.Chrome() as driver:
    driver.get("https://www.baidu.com");
    sleep(2)
    soutu_btn = driver.find_element(By.XPATH,"//span[@class='soutu-btn']");
    soutu_btn.click();
    upload_btn = driver.find_element(By.XPATH,"//div[@class='upload-wrap']")
    upload_btn.click();
    #写入文件的绝对路径
    pyautogui.write("/Users/yantianpeng/Desktop/1.jpg");
    #按下enter键盘 2表示模式输入
    pyautogui.press('enter',2);
    sleep(10);

    driver.quit();
