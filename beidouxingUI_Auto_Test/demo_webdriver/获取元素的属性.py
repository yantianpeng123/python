#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/16  10:52 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 获取元素的属性.py
# @Software: PyCharm
'''
from selenium import webdriver;
from time import sleep
driver = webdriver.Chrome();

driver.get("https://www.baidu.com");

element =  driver.find_element_by_id("kw");
name = element.get_attribute("name"); #获取元素的属性值
print("获取搜索框的name属性的值是:{}".format(name));
img_loc = driver.find_element_by_class_name("index-logo-src").get_attribute("src");
print("获取百度log的src属性的值是:{}".format(img_loc))

#定位百度热搜榜单中第一个连接
# hotsearch = driver.find_element_by_class_name("s-news-rank-content")
sleep(2)
hotsearch = driver.find_element_by_css_selector('ul[class="s-hotsearch-content"]');
hot_url = hotsearch.find_element_by_tag_name('a') #获取a标签中所有text文本信息
print("{}".format(hot_url.text));
sleep(10);
driver.quit();