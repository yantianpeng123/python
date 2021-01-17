#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/16  11:47 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : iframe切换.py
# @Software: PyCharm
'''

from selenium import webdriver
from time import sleep
from  selenium.webdriver.common.by import By;
#使用with上下文管理器 在程序发生异常的时候也会关闭浏览器
with webdriver.Chrome() as driver:
    """
        切换iframe
        1.webelemnet的方式
        2.先获取到iframe
        iframe =  driver.find_element_by_id("iframeid");
        在切换到
        driver.switch_to.iframe(iframe);
        
        #name/id方式
        直接通过name/id切换
        driver.switch_to.iframe("name/id");
        
        #使用索引切换
        切换到第二个iframe
        driver.switch_to.iframe(1)
    
    """
    #打开网址
    driver.get("https://www.w3school.com.cn/tiy/t.asp?f=html_radiobuttons");
    iframe = driver.find_element(By.ID,"iframeResult"); #通过id/name切换
    iframe = driver.find_element(By.XPATH,'//iframe[@id="iframeResult"]');#通过webelement来切换
    driver.switch_to.frame(1);#通过索引来切换
    driver.find_element(By.XPATH,"//input[@value='female']").click()
    sleep(10)
    driver.switch_to.default_content()#离开ifram回到当前的主页面
    driver.quit();