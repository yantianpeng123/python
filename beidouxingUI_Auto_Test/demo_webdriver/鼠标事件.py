#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/19  2:38 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : 鼠标事件.py
# @Software: PyCharm
'''
#鼠标使用过底层接口执行的，需要调用ActionChains对象来执行对应的方法
# clickAndHold 它将移动到该元素中，然后在给定的元素的中间单击(不释放)
# contextClick 此方法首先将鼠标移动到元素位置，然后在给定元素执行上下文点击(右键单击);
# doubleClick 它将移动到该元素，并在给定元素的中间双击
# moveToelment此方法将鼠标移动到元素的中间，执行此操作时，该元素也会滚动到视图中
# moveByoffset 此方法将鼠标从其位置(或者是0，0)移动到给定的偏移量，如果坐标在视图窗口之中，则鼠标最终将在浏览器中
# dragAndDrop 此方法首先在源元素上单击并按住，然后移动到目标元素的位置后释放鼠标
# relase 此操作将释放按下的鼠标左键,如果Webelement转移啦他将释放给定WebElement上按下的鼠标左键

from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


with webdriver.Chrome() as driver:
    driver.get("https://www.w3school.com.cn/js/js_htmldom_events.asp");
    Move_Over_Me = WebDriverWait(driver,timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'鼠标移上来！')]")));
    #把鼠标悬浮在指定的位置
    ActionChains(driver).move_to_element(Move_Over_Me).perform();
    sleep(3);
    #把鼠标从上一个位置向x轴偏移100，y轴偏移100
    ActionChains(driver).move_by_offset(xoffset=100,yoffset=100).perform();
    sleep(3);

    click_hold =WebDriverWait(driver, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'点击我')]")));
    #鼠标点击不放开
    ActionChains(driver).click_and_hold(click_hold).perform()
    sleep(3)
    ActionChains(driver).release(click_hold).perform();
    sleep(3)
    #鼠标点击事件
    # ActionChains(driver).click(click_hold).perform();
    ActionChains(driver).double_click(click_hold).perform();
    sleep(3)
    #鼠标右键
    ActionChains(driver).context_click(click_hold).perform();
    sleep(3)
    #元素1 和元素2 是假设出来的
    div1 = WebDriverWait(driver).until(EC.visibility_of_element_located("//div[contains(text(),'元素1')]"));
    div2 = WebDriverWait(driver).until(EC.visibility_of_element_located("//div[coantains(text(),'元素2')]"));
    ActionChains(driver).drag_and_drop(div1,div2);
    sleep(2)
    driver.quit();
