#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/30  7:09 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_Expetion.py
# @Software: PyCharm
'''
#异常处理
#异常概念：
score = input('请输入你分数');
try:
    score  = float(score);
    if score < 60:
        print("不及格");
    else:
        print("及格");
except  Exception as e:
    print('你输入的成绩有误{}'.format(e))


#编写一个程序实现录入学生的的成绩,当输入为q的时候，停止录入，并且从大到小显示学生的成绩是多少和并且计算每个阶段学生的数量

list_01 = [];# 定义一个空的列表用来存储成绩
E_leve_count = 0; # 定义一个变量用来 计算录入E等级的人数.
D_leve_count = 0; # 定义一个变量用来计算录入D等级的学生人数
C_leve_count = 0; #定义一个变量用来计算录入C等级的学生的人数
B_leve_count = 0; #定义一个变量用来计算录入B等级学生的人数
A_leve_count = 0;# 定义一个变量用来计算录入A等级学生的人数。
while True:
    score = input("请输入学生的成绩-->>>>>");
    if score =='q':
        break; #停止录入
    try:
        score = float(score);
        if score <60:
            list_01.append(score);
            E_leve_count+=1;
        elif 60<=score<75:
            list_01.append(score);
            D_leve_count+=1;
        elif 75<=score<80:
            list_01.append(score);
            C_leve_count+=1;
        elif 80<=score<90:
            list_01.append(score);
            B_leve_count+=1;
        elif 90<=score<=100:
            list_01.append(score);
            A_leve_count+=1;
        else:
            print("你输入的成绩有误");
    except Exception as e:
        print("你输入的成绩有误,请重新输入");
list_01.sort()
print(list_01);
print("该班级中成绩等级为A的学生的数量是:{},成绩等级为B的学生的数量是:{},成绩等级为C的学生的数量是:{},"
      "成绩等级为D的学生的数量是{},成绩等级为E的学生的数量是:{}".format(A_leve_count,B_leve_count,C_leve_count,D_leve_count,E_leve_count))


try:
    a ="QWERTYUIOPASDFGHJKLZXCVBNM";
    index = int(input("请输入一个正整数"));
    print(a[index]);
except Exception as e:
    print("你的输入有误");
finally:
    print("不管是正确的还是错误的，都会被执行");
