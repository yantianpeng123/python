#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/1  3:14 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_file.py
# @Software: PyCharm
'''
#文件操作
#打开文件
fb = open('test.txt',mode='r',encoding='utf-8');
#操作文件
contenet = fb.read();
print(contenet);
#关闭文件
fb.close();

#with 上下文管理器使用with 上下文管理器 不需要手动关闭文件
with open('test.txt',mode='r',encoding='utf-8') as fb:
    contenet = fb.read();
    print(contenet);


print('+++++++');
with open('test.txt',mode='r',encoding='utf-8') as fb:
    print(fb.readline());# 逐行读取
    print(fb.readline());# 逐行读取


print('=======');
#迭代读取每一行
with open('test.txt',mode='rb',encoding='utf-8') as fb:
    for _ in fb:
        print(_);

#写入文件
with open('test.txt',mode='w',encoding='utf-8') as f:
    f.write("上海市北京市");

#在文件的末尾进行追加
with open('test.txt',mode='a',encoding='utf-8') as f:
    f.write('这是追加写');

with open('test.png',mode='wb',encoding='utf-8') as f:
    f.write('二进制文件');


#读写模式r+ 表示即可读又可以写
with open('test.txt',mode='r',encoding='utf-8') as f:
    contenet = f.read();#先读取文本内容
    f.write('上海市');#在开始写文本内容


