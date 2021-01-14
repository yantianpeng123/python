#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/4  8:11 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_file_01.py
# @Software: PyCharm
'''
#python处理csv文本文件 使用迭代的方式打开csv文件 并且组成成二维数组的形式
data = []
with open('jixie.csv',mode='r',encoding='utf-8') as f:
    for _ in f:
        _ = _.strip(',\n');
        _ =_.split(',')
        data.append(_);
print(data);


#把嵌套的二维数据写成csv文件
with open('jiexie1.csv',mode='w',encoding='utf-8') as f:
    for d in data:
        for _ in d:
            f.write(_);
            f.write(',')#每个字段使用逗号分割
        f.write('\n');

#把二维数据写成csv文件
with open('jiexie2.csv',mode='w',encoding='utf-8') as f:
    for item in data:
        line = ''.join(item)+'\n';
        f.write(line);




