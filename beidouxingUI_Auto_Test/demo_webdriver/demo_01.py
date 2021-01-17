#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/16  12:17 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : demo_01.py
# @Software: PyCharm
'''
from selenium import webdriver

#打开浏览器 并且返回一个浏览器对象
driver = webdriver.Chrome();
driver.get("http://www.baidu.com"); # 打开网站

driver.close()#  关闭浏览器
driver.quit(); #关闭浏览器，并且退出浏览器进程和chromedriver进行