#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/10/31  2:35 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_01.py
# @Software: PyCharm
'''

#定义一个带有参数的函数
#x和y都是必须参数的参数
def add(x,y):
    print(x+y);



# 定义一个带有参数函数，其中x表示必须参数在调用的时候，是必须要写的 y表示默认参数在调用的时候可以不写，不写的话使用就是默认的值
def test_001(x,y=2):
    print(x+y);


#定义一个函数打印指定次数的 指定的字符串 ，默认打印一次

def my_print(content,times=1):
    for _ in range(times):
        print(content);

#定一个一个函数打印一个数的n次幂

def my_power(x,y):
    print(x**y);


# 定义一个函数可以接受2个以上的数，并且打印他们的和
def test_001(a,*args):
    print(a,args);

def test_002(a,*b):
    print(a,b);


def test_003(x,y,*args):
    sum = x+y;
    for _ in args:
        sum+=_;
    print(sum);


def test_004(a,**kwargs):
    print(a,kwargs);

def test_005(x,y,*args):
    sum = x+y;
    for _ in args:
        sum+=_;
    print(sum);

def connect(host,db_name,user,pwd):
    '''
    假设是一个数据库的链接方法
    :param host:
    :param db_name:
    :param user:
    :param pwd:
    :return:
    '''
    print("数据库的地址是:{},数据库的库名字是:{},数据库的用户名是:{},数据库的密码是:{}".format(host,db_name,user,pwd));


db_config={
    "host": '127.0.0.1',
    "db_name": "yantianpeng",
    "user": "root",
    "pwd": "123456"
}

#调用connect()方法

connect(host=db_config['host'],db_name=db_config['db_name'],user=db_config['user'],pwd=db_config['pwd']);
#使用**的时候在传递实参时候 可以通过** 对字典对象进行解包 按照key=value的关键字的形式传递参数
# 字典的键的值必须和函数的形参保持一致
connect(**db_config);

#定义一个函数接受两个或者两个以上的，并且返回他们的和
def test_006(x,y,*args):
    sum_01 = x+y;
    for _ in args:
        sum_01+=_;
    return sum_01;

aa = test_006(1,2,3);
print(aa);


#返回多个函数值;

def test_007(name1,name2,name3):
    return name1,name2,name3;#返回的是一个元组

ab =  test_007('张三','李四','王二');
print(ab);


ls  = [i for i in range(101)];
test_005(*ls);#使用*解包列表或者元组




test_004(a=1,b=2,c=3);

test_003(1,2,3,4,5,6,7,8,9,10);


test_002(1,2,3,4,5,6,7,8,9,0);


test_001(1);
test_001(1,2);
test_001(1,2,3,4,5);



my_power(2,4);

my_power(x=2,y=5)
add(1,2);
add(2,3);

test_001(1);
test_001(2)
test_001(1,7)