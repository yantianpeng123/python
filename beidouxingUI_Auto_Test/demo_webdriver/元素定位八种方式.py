#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/16  9:42 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 元素定位八种方式.py
# @Software: PyCharm
'''
from selenium import webdriver
from time import sleep
"""
#1.通过id元素定位
driver.find_element_by_id("");
#2.通过那么定位
driver.find_element_by_name("");
#3.通标签名定位
driver.find_element_by_tag_name("");
#4.通过css选择器定位
driver.find_element_by_css_selector("");
#5.通过xpath定位
driver.find_elements_by_xpath("");
#6.通过class_name定位
driver.find_element_by_class_name("");
#7.通过匹配连接标签text内容定位
driver.find_elements_by_partial_link_text("")
#8.通过连接标签text内容定位
driver.find_element_by_link_text("");
以上的方法只适合返回匹配的第一个元素
"""
#打开浏览器
# global driver;
driver = webdriver.Chrome();
#打开网址
driver.get("https://www.baidu.com/");

#通过id定位 在百度框中输入内容
driver.find_element_by_id("kw").send_keys("自动化测试");
#通过id定位 点击百度按钮
driver.find_element_by_id("su").click();

# 通过name定位 在百度框中输入内容
driver.find_element_by_name("wd").send_keys("自动化测试")
driver.find_element_by_id("su").click();

# 通过tag_name 标签命定位
driver.find_element_by_tag_name("button").click();

# 通过css选择器进行定位
driver.find_element_by_css_selector("input[id='kw']").send_keys("css选择器定位");
driver.find_element_by_css_selector('input[id="su"]').click();

#通过xpath进行定位
driver.find_element_by_xpath("//input[@id='kw']").send_keys("xpath元素定位");
driver.find_element_by_xpath("//input[@id='su']").click();

# 通过class_name元素定位
driver.find_element_by_class_name("s_ipt").send_keys("s_ipt")
driver.find_element_by_class_name("s_btn").click();

driver.find_element_by_link_text("hao123").click();
driver.find_element_by_partial_link_text("hao").click();

sleep(10)
driver.quit();


