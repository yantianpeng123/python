#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/25  12:24 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : report_handler.py
# @Software: PyCharm
'''
import os
from datetime import datetime
from beidouxingauto_project.libs.HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport


def report(ts,file='report.html',report_dir='.',title='测试报告',description=None,tester = "beidouxing",type_='htr'):
    """

    :param ts:  测试套件
    :param file:测试报告名称
    :param report_dir:测试报告路径
    :param title: 测试标题
    :param description: 测试描述
    :param tester:测试人
    :return:
    """

    #在文件名加上时间
    file = "{}--{}".format(datetime.now().strftime('%Y-%m-%d %H时%M分%S秒'),file);
    #检测目录是否存在,不存的话要创建
    if not os.path.exists(report_dir):
        os.makedirs(report_dir);
    #拼接报告名称
    file_path =  os.path.join(report_dir,file);
    #生成htmlreport报告
    if type_.lower() =='htr':
        with open(file_path, 'wb') as fb:  # 生成测试报告，这一块不需要添加encoding='utf8'这个参数
            html_01 = HTMLTestRunner(stream=fb, description=description, title=title, tester=tester);
            html_01.run(ts);  # 执行suit
    #可以组装多个类型的测试报告
    elif type_.lower() == 'br':
        BeautifulReport(ts).report(filename=file,description=description,report_dir=report_dir);


# if __name__ == '__main__':
#     ts = 1;
#     report(ts,file='report.html',report_dir='.',title='测试报告',description=None,tester = "beidouxing")