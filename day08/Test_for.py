#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/30  8:40 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_for.py
# @Software: PyCharm
'''
#for循环变量

# for 临时变量 in 需要循环的列表
#     代码块
#for循环用来循环列表
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9];#定义一个列表
for i in ls:
    print(i);


#for循环用来循环字符串
for i in 'asdfghjkl':
    print(i);

#散列的循环 取值的数据是没有顺序的
st = {'1','2','3', '4', '5'};
for i in st:
    print(i);


#for循环循环字典
dc = {
    "name": "yantianpeng",
    "age": 12,
    "score": 120,
    "weight": 90.0,
    "salary": 12345
}

#for循环根据字典取值
for i in dc.keys():
    print(dc[i]);

#for循环 同时取值字典的键和值
for i,j in dc.items():
    print(i,j);


for i in range(1,9):
    print(i);

#创建一个列表存放成绩 判断是否有不及格同学
score = [98, 90,65,56,23,34,90];
#统计不及格学生的数量
num = 0 #用来统计不及格学生的数量
for i in score:
    if i<60:
        # print("该同学的成绩是：{},该同学不及格。".format(i));
        num+=1;
        print("一共有{}学生不及格".format(num));


#判断是否有成绩不及格，一旦发现有成绩小于60的就停止循环
#break关键字 跳出当前循环，代码继续执行。

for i in score:
    if i<60:
        print("有同学不及格");
        break;

#输处所有不及格的成绩;
#使用continue 停止本次循环，继续下一次循环，代码块中continue后的代码不在执行，直接跳转到下一次循环中
for i in score:
    if i>=60:
        continue;
    print(i)


#else:检查代码是正常结束还是被break掉啦
for i in range(10):
    if i %2 != 0:
        continue;
    print(i);
else:
    print("循环结束");#上面是continue的话这句话会输出。如果是break的话则不会输出。

#双重循环
ls_01  = [1,2,3];
ls_02 = ['a','b','c'];
for i in ls_01:#第一次执行最外面的循环，
    for j in ls_02:#执行最里面的循环 里面的循环执行完毕，在去执行外面的循环
        print(i,j);

#嵌套循环实现九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,(i*j)),end=' ');
    print()


#编写程序实现，在程序预设一个0到9之间的数字，让用户通过键盘输入所猜的数，
# 如果大于预设的数，表示太遗憾啦，太大啦，小于预设的数，显示 遗憾啦，太小啦
# 如此循环直到猜中该数，显示预测N次，你猜中啦，其中N是用户输入数字的次数

count = 0;#计算用户猜啦多少次
computer = 7;
while True:
    num = int(input("请输入你预测的数字:"))
    if num>computer:
        count += 1;
        print("遗憾啦，太大了");
    elif num<computer:
        count += 1;
        print("遗憾啦,太小啦");
    else:
        count+=1;
        print("预测"+str(count)+"次,你终于猜中啦！！");
        break;

#编写程序实现，用户从键盘输入一行字符串，统计并输出其中的英文字符，数字 空格和其他字符的数量;
user_input = input("请输入任意的字符，包含英文 数字 空格 和其他的字符")
num_count = 0; # 数字出现的次数
str_count = 0; # 字符出现的次数
blank_count = 0; # 空格出现的次数
other_count = 0; # 其他字符出现的次数
for i in user_input:
    if i.isdigit():#判断是否是纯数字
        num+=1;
    elif i.isalpha(): # 判断是否是纯字母
        str_count+=1;
    elif i.isspace():# 判断是否是空格
        blank_count+=1;
    else:#其他字符
        other_count+=1;

print("你输入的数据中包含啦"+str(num_count)+"个数字,"+str(str_count)+"个字母,"+str(blank_count)+"个空格,"+str(other_count)+"个其他字符");
print("你输入的数据中包含啦{}个数字,{}个字母,{}个空格,{}个其他字符".format(num_count,str_count,blank_count,other_count));

#使用print和循环结构输出如下的金字塔()
for i in range(4):
    start_num = i*2+1;
    space_num = 4-i-1;
    print(' '*space_num+'*'*start_num);

#使用print函数和循环结构输出一个空心的金字塔
n = int(input("请输入数字"));
for i  in range(n):
    start_num = i * 2 + 1;
    space_num = n - i - 1;
    if i ==0 or i ==n-1:
        print(' '*space_num+'*'*start_num);
    else:
        print(' '*space_num+'*'+' '*(start_num-2)+'*');

#使用print函数和循环结构输出一个菱形
n = int(input("请输入你的数字"));
for i in range(n):
    start_num = i*2+1;
    space_num =n-i-1;
    print(" "*space_num+"*"*start_num);
for i in range(n-1):
    start_num =2*(n-1)-(i*2+1);
    print(' '*(i+1)+'*'*start_num);