#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/4  8:45 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_file_02.py
# @Software: PyCharm
'''
data = [];
dic = {};
with open('jiexie1.csv',mode='r',encoding='utf-8') as f:
    line =f.readline();
    line = line.strip(',\n').split(',');
    j=0;
    while j<len(line):
        for item in f:
            item = item.strip(',\n').split(',')
            if len(item)<5:
                continue;
            j = 0;
            dic ={};
            for i in item:
               dic[line[j]]=i;
               j =j+1;
            data.append(dic);
