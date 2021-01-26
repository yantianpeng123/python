#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/17  11:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 元素等待--隐式等待.py
# @Software: PyCharm
'''
"""
selenium 隐式等待
    隐式等待的本质式设置了一个全局等待时间，WebDriver在查找任何元素的时候都会轮询一定时间
    默认情况下隐式等待式禁止使用的
    警告:
        不用混用隐式等待和显式等待，这样会导致不可预测的等待时间
        例如隐士等待设置10秒，显式等待设置15秒 可能会导致在20秒之后发生超时
        
    隐式等待是告诉WebDriver如果在查找一个或者多个不是立即可用的元素时轮询DOM一段时间默认设置为0
    表示禁用，一旦设置好，隐式等待就会被设置为会话的生命周期
"""
from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.implicitly_wait(5)#设置成功之后每次都是等待5秒 设置成功之后就是全局等待
    driver.get("https://www.baidu.com");
