#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/23  1:11 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : base_page.py
# @Software: PyCharm
'''
from beidouxingUI_Auto_Test.Auto_UI_Project.common.login_handler import log
from beidouxingUI_Auto_Test.Auto_UI_Project import setting
from selenium import webdriver;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;
import os
from datetime import datetime
from time import sleep


#封装页面的基本功能
class BasePage:
    """
    页面常用的功能
    1.查找 等待 --查找
    2.点击 等待  --查找--点击
    3.输入 等待  -- 查找 --输入
    4.获取元素文本 等待 --查找--获取文本
    5.获取元素属性  等待 --查找 --获取属性
    6.窗口切换
    7.失败截图
    8.获取元素wenb
    9.
    10.
    """
    name ="Base页面";
    log = log;
    setting= setting;

    def __init__(self,driver:webdriver):
        self.driver = driver
        self.element =None;
        self.locator =None;
        self.action = '';




    def wait_element_is_visiable(self,locator,action='',**kwargs):
        """
        等待元素可见
        :param locator:  元素定位信息
        :param action: 操作说明
        :param kwargs:超时，轮询频率 和其他参数
        :return:
        """
        #设置元素查找超时时间
        try:
            self.locator = locator;
            self.action = action;
            timeout = kwargs.get("timeout", self.setting.DEFAULT_TIMEOUT)
            poll_frequency = kwargs.get("poll_frequency", 0.5);
            self.element =  WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            #日志记录
            self.log.exception("在{},{}操作的时候，等待{}元素可见【失败】".format(self.name,action,locator));
            #保存失败截图
            self.get_page_screenshot(action);
            raise e;
        else:
            self.log.info("在{},{}操作的时候，等待{}元素可见【成功】".format(self.name, action, locator));
            return self


    def wait_element_to_be_clickable(self,locator,action='',**kwargs):
        """
        等待元素可以点击
        :param locator: 元素路径
        :param action:  元素动作
        :param kwargs: 动态参数
        :return:
        """
        try:
            self.locator = locator;
            self.action = action;
            timeout = kwargs.get("timeout", self.setting.DEFAULT_TIMEOUT);
            poll_frequency = kwargs.get("poll_frequency", 0.5);
            self.element = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                EC.element_to_be_clickable(locator)
            );
        except Exception as e:
            self.log.warning("在{},{}操作时候,该{}元素可以点击【失败】".format(self.name,action,locator))
            self.get_page_screenshot(action=action);
            raise e;
        else:
            self.log.info("在{},{}操作的时候，该{}元素可以点击【成功】".format(self.name, action, locator));
            return self;

    def wait_element_presence_located(self,locator,action='',**kwargs):
        """
        等待元素出现
        :param locator:  元素位置信息
        :param action:  元素操作
        :param kwargs:
        :return:
        """
        try:
            #初始化参数
            self.locator= locator;
            self.action = action;
            timeout = kwargs.get("timeout", self.setting.DEFAULT_TIMEOUT);
            poll_frequency = kwargs.get("poll_frequency", 0.5);
            self.element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                EC.presence_of_element_located(locator=locator)
            );
        except Exception as e:
            self.log.exception("在{},{}操作的时候，等待{}元素出现【失败】".format(self.name,action,locator))
            self.get_page_screenshot(action=action);
            raise e;
        else:
            self.log.info("在{},{}操作的时候，等待{}元素出现【成功】".format(self.name,action,locator));
            return self;



    def get_element(self):
       """
       获取元素
       """
       if self.element is None:
           raise  RuntimeError("不能在wait方法之前调用此方法")
       return self.element;


    def click_element(self):
       if self.element is None:
           raise RuntimeError("不能在wait方法之前调用此方法");
       try:
           self.element.click();
       except Exception as e:
            self.log.exception("在{},{}操作的时候，点击{}元素【失败】".format(self.name,self.action,self.locator));
            self.get_page_screenshot(action=self.action);
            raise e;
       else:
           self.log.info("在{},{}操作的时候，点击{}元素【成功】".format(self.name,self.action,self.locator));
       finally:
           #操作完成之后清空操作
           self.__clear_cache();
    def get_element_text(self):
        # 获取文本信息


       if self.element is None:
           raise RuntimeError("不能在wait方法之前调用此方法")
       try:
          text = self.element.text
       except Exception as e:
           self.log.exception("在{},{}操作的时候，获取{}元素文本内容【失败】".format(self.name,self.action,self.locator));
           self.get_page_screenshot(action=self.action);
           raise e;
       else:
           self.log.exception("在{},{}操作的时候，获取{}元素文本内容【成功】,内容为:{}".format(self.name, self.action, self.locator,text));
           return text;
       finally:
           self.__clear_cache();
            
            
    def get_element_attr(self,name):
        """

        :return:
        """
        if self.element is None:
            raise RuntimeError("不可以在wait方法调用之前调用此方法");
        try:
            value = self.element.get_attribute(name=name)
        except Exception as e:
            self.log.exception("在{},{}操作的时候,获取元素的属性的值【失败】".format(self.name,self.action,self.locator));
            self.get_page_screenshot(action=self.action);
            raise e;
        else:
            self.log.info("在{},{}操作的时候,获取元素的属性的值【成功】,属性的值是:{}".format(self.name,self.action,self.locator,value));
            return value;
        finally:
            self.__clear_cache();

    def switch_to_new_windows(self,handle=None,action=''):
        """

           :return:
        """
        try:
            if handle:
                self.driver.switch_to.window(handle);
            else:
                original_window = self.driver.current_window_handle
                for handle in self.driver.window_handles:
                    if handle != original_window:
                        self.driver.switch_to.window(handle);
                        break;
        except Exception as e:
            self.log.exception("在{},{}操作的时候,切换到窗口{}【失败】".format(self.name,action,handle));
            self.get_page_screenshot(action=action);
            raise e
        else:
            self.log.info("在{},{}操作的时候，切换到窗口{}【成功】".format(self.name,action,handle));


    def send_keys(self,content):
       """
        向输入框中输入内容
       :return:
       """
       if self.element is None:
           raise RuntimeError("不可以在wait方法之前调用此方法");

       try:
            self.element.send_keys(content);
       except Exception as e:
           self.log.exception("在{},{}操作的时候，对{}元素输入{}【失败】".format(self.name,self.action,self.locator,content));
           self.get_page_screenshot(action=self.action);
           raise e;
       else:
           self.log.info("在{},{}操作的时候，对{}元素输入{}【成功】".format(self.name,self.action,self.locator,content));
       finally:
           self.__clear_cache();

    def get_page_screenshot(self,action):
        """
        获取失败截图，命令规范 xx页面_xx操作_截图时间.png
        :param action:
        :return:
        """
        #拼接错误截图文件名
        img_path =os.path.join(self.setting.ERROR_SCREENSHOT_DIR,
                               "{}_{}操作 {}.png".
                               format(self.name,action,datetime.now().strftime('%Y-%m-%d %H-%M-%S')))
        if self.driver.save_screenshot(img_path):
            self.log.info("生成错误截图:{},【成功】".format(img_path));
        else:
            self.log.error("生成错误截图:{},【失败】".format(img_path));

    def __clear_cache(self):
        """
        清空操作
        :return:
        """
        self.element =None;
        self.action='';
        self.locator = None;

    def wait_time(self,time=0.5):
        """
            延时操作 默认延时0.5毫秒
        :param time:
        :return:
        """

        sleep(time);
        return self;