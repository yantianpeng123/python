#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/24  10:48 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : request_proxies.py
# @Software: PyCharm
'''
import requests
base_url="https://www.example.com"
proxies ={
    "http":"http://10.10.1.10:3128",
    "https":"https://10.10.1.10:443"
}

#这是代理
requests.get("https://www.baidu.com/",proxies=proxies);

#上传文件 使用files参数传递句柄

files = {"file":open('test.xls','rb')}#上传文件位置
requests.post(url=base_url,files=files);


#重定向:在网络请求中我们经常会遇到状态码是2开头的重定向问题，在Requests中默认是开启允许重定向到即遇到重定向时候，会自动继续访问。
res = requests.get("http://www.baidu.com",allow_redirects = False);
print(res.status_code);#返回的状态码

#禁止证书验证:有时候我们使用啦抓包工具，这个时候由于抓包工具提供的证书并不是由授信的数字证书机构颁发的，所以就会显示证书验证失败，我们就需要关闭证书验证。
requests.get("https://www.baidu.com",verify = False);#关闭证书验证
#但是关闭证书验证以后，会有一个warning，可以使用下面的方法解决
from requests.packages.urllib3.exceptions import InsecureRequestWarning;
requests.packages.urllib3.disable_warnings(InsecureRequestWarning);

#设置超时
# 设置访问超时时间 设置参数timeout就可以啦
requests.get("https://www.baidu.com",timeout = 100);#设置参数超时

#响应:



