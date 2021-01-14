#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/25 3:14 下午
# @Author  : yq
# @Site    : 
# @File    : demo_002.py
# @Software: PyCharm
'''
a = 1;
a+=1;
print(a);#a的值现在是2 程序是从上往下开始执行的

#步骤
#1.接受用户的输入
#input函数:接受用户的输入，以字符串的形式返回，他接受字符串参数作为提示信息输出.
score  =  input("请输入你的成绩>>>>>>>")
score =  int(score);#类型转换
#2.判断成绩
if score>60:
    print("考试及格");#3.作出反应
if score<=60:
    print("考试不及格");#3.作出反应

#多分支结构；
# 成绩评价
#根据成绩分等级  小于40 等级是E  40～60 D 60～75 C 75～85 B  85～100 A
#接受用户的成绩输入
score_01 =  input("请输入你的成绩");
score_01 =  float(score_01);
#判断成绩大小
if score_01<=40:
    print("你的成绩等级是:E");
elif 40<=score_01<60:
    print("你的成绩等级是:D");
elif 60<=score_01<75:
    print("你的成绩等级是:C");
elif 75<score_01<=85:
    print("你的成绩等级是B");
elif 85<=score_01<100:
    print("你的成绩等级是A");
else:
    print("你的分数输入有错误");
#作出反应

