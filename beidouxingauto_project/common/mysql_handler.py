#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/26  12:53 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : mysql_handler.py
# @Software: PyCharm
'''
import pymysql
from beidouxingauto_project import setting
class MysqlDB:

    def __init__(self,**kwargs):
        self.con = pymysql.connect(**kwargs);
        self.cur = self.con.cursor(pymysql.cursors.DictCursor);
        # self.cur = self.con.cursor();

    def Isexist(self,sql):
        '''
        根据sql判断是否查询到数据
        :param sql:
        :return:
        '''
        self.cur.execute(sql);
        if self.cur.fetchone():
            return True;
        else:
            return False;#返回


    def select_one_data(self,sql):
        '''
        返回一条数据
        :param sql:
        :return:
        '''
        self.cur.execute(sql);
        return self.cur.fetchone();

    def select_many(self,sql,size):
        '''
        返回指定的条数
        :param sql:
        :param size:
        :return:
        '''
        self.cur.execute(sql);
        return self.cur.fetchmany(size=size);


    def select_all_data(self,sql):
        '''
        返回所有的结果
        :param sql:
        :return:
        '''
        self.cur.execute(sql);
        return self.cur.fetchall();

    def get_count(self,sql):
        '''
        获取查询条数的结果
        :param sql:
        :return:
        '''
        return self.cur.execute(sql);

    def insert_data(self,sql):
       try:
           self.cur.execute(sql);
           self.con.commit();
       except:
           self.con.rollback();
       finally:
           self.cur.close();
           self.con.close();

    #析构方法 当对象被销毁的时候，自动调用
    def __del__(self):
        self.cur.close();
        self.con.close();



db = MysqlDB(**setting.MYSQL_DATA_CONFIG);


if __name__ == '__main__':
    mysql_info = {
        "host": "api.lemonban.com",
        "port": 3306,
        "user": "future",
        "password": "123456",
        "db": "futureloan",
        "charset": "utf8"
    }



    sql ='select * from member where mobile_phone = \'18203027509\' and type =0 ';
    res = MysqlDB(**mysql_info).select_one_data(sql=sql);
    # res = MysqlDB(**mysql_info).Isexist(sql=sql);
    print(res);
