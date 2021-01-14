#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/25  9:07 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : python_mysql.py
# @Software: PyCharm
'''
import pymysql

#创建链接
# con = pymysql.connect(
#     host="api.lemonban.com",
#     port=3306,
#     user="future",
#     password="123456",
#     db="futureloan",
#     charset="utf8"
# );
# #创建游标
# cus = con.cursor(cursor=pymysql.cursors.DictCursor);#cursor=pymysql.cursors.DictCursor 返回的字典
# #执行sql
# sql ="select * from member limit 10";
# cus.execute(sql);
#
# one =cus.fetchone()#获取一条 默认情况返回的是元组
# many_size =cus.fetchmany(5);#获取5条 默认情况下返回的元组
# max_size =cus.fetchmany();#获取全部结果；默认情况下返回是元组
#
#
# # print(one);
# print("----")
# print(many_size);
# print("---")
# print(max_size);
# #关闭游标
# cus.close();
# #关闭连接
# con.close();


def mysql_connect(host,user,password,db,sql,size,charset='utf8',port=3306):

    #创建连接
    con = pymysql.connect(host=host,port=port,user=user,password=password,db=db,charset=charset)
    #创建游标
    cus =con.cursor(pymysql.cursors.DictCursor);
    #执行sql
    cus.execute(sql);
    #获取结果


    data = cus.fetchall();
    cus.close();
    con.close();
    return data;

mysql_info = {
    "host":"api.lemonban.com",
    "port":3306,
    "user":"future",
    "password":"123456",
    "db":"futureloan",
    "charset":"utf8"
}

# res = mysql_connect(**mysql_info);
# print(res);


class mysql_handler:

    def __init__(self,host,user,password,db,port=3306,charset='utf8'):
        self.host = host;
        self.user = user;
        self.password = password;
        self.db = db;
        self.charset = charset;
        self.port = port;

    def __connectMysql(self):
        self.con = pymysql.connect(host =self.host,user =self.user,password=self.password,db = self.db,charset =self.charset,port=self.port)
        return self.con.cursor(pymysql.cursors.DictCursor)



    def select_Onedata(self,sql):
        self.cus = self.__connectMysql()
        self.cus.execute(sql);
        self.one = self.cus.fetchone();
        self.__close();
        return self.one

    def select_manydata(self,sql,size):
        self.cus = self.__connectMysql()
        self.cus.execute(sql);
        self.cus.execute(sql);
        self.many = self.cus.fetchmany(size=size)
        self.__close();
        return self.many

    def select_alldata(self,sql):
        self.cus = self.__connectMysql()
        self.cus.execute(sql);
        self.all = self.cus.fetchall()
        self.__close()
        return  self.all;

    def get_count(self,sql):
        self.cus = self.__connectMysql()
        self.cus.execute(sql);
        self.__close()
        return self.cus;
    def Isexist(self,sql):
        self.cus = self.__connectMysql()
        self.cus.execute(sql);
        if self.cus.fetchone():
            print('存在');
        else:
            print('不存在')
        self.cus.close();
        self.con.close();


    def __close(self):
        self.con.close();
        self.cus.close();

# sql_01 = "delete from member where id = 18873951379 ";
sql_02 = "update member set reg_name='yujie_01' where mobile_phone = '13133172226' "
res =  mysql_handler(**mysql_info).get_count(sql=sql_02)
print(res);


# select * from member where mobile_phone = '13858780434' and type =1

# sql= 'select * from member where mobile_phone = \'13858780279\' and type =1'
sql ='select * from member where mobile_phone = \'18542013234\' and type =0 '
resOne = mysql_handler(**mysql_info).select_Onedata(sql=sql);
print(resOne)

print("=================")
resMany =  mysql_handler(**mysql_info).select_manydata(sql=sql,size=2);
print(resMany);

print("--------------------")
resAll = mysql_handler(**mysql_info).select_alldata(sql=sql);
print(resAll)


Isexist =  mysql_handler(**mysql_info).Isexist(sql);
