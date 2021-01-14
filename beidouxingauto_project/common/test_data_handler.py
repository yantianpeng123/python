#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/26  2:45 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_data_handler.py
# @Software: PyCharm
'''
import random
import re
def get_phone():

    #规则 第一位是1 第二为是 358 任意一个 后面9为是0到9
    phone = ['1',random.choice('358')]
    for i in range(9):
        phone.append(random.choice('012356789'));
    return ''.join(phone);


def replace_args(fs,flag ='#',**kwargs):
    """

    :param fs:
    :param kwargs:
    :return:
    """
    for args ,values in  kwargs.items():
         fs = fs.replace("{0}{1}{0}".format(flag,args),str(values));
    return fs;


def replace_args_re(s,cls):
    """
    正则表达式动态替换参数
    :param s:
    :param cls:
    :return:
    """
    args = re.findall('#(.*?)#',s);
    for arg in args:
        value = getattr(cls,arg,None);
        if value:
            s = s.replace('#{}#'.format(arg),str(value));
    return s;


def extract_data(map,cls,json_res_str):
    """
    提取需要存储的数据
    :param map:
    :param cls:
    :param json_res_str:
    :return:
    """
    #排除到干扰字符

    json_res_str = json_res_str.replace(' ','').replace('\n', '')
    # json_res_str = json_res_str.replace(' ','').repalce('\n','');
    for agr,key in map.items():
        res_strs = [
            r'"{}":"(.*?)"'.format(key), #字符串参数
            r'"{}":"(\d+?\.\d+?),"'.format(agr),#浮点型参数，放在前面
            r'"{}":(\d+?),'.format(key)#数字参数
        ]
        for res_str in res_strs:
            value = re.findall(res_str,json_res_str);
            if value:
                setattr(cls,agr,value[0]);
                break;




if __name__ == '__main__':
    # # print(get_phone());
    # s='{\n    "mobile_phone":"#phone#",\n    "pwd":"#pwd#",\n    "type":0,\n    "reg_name":"yujie"\n}';
    # phone="13858389567";
    # pwd="12345678";
    # s = replace_args(s,flag="#",phone=phone,pwd=pwd)
    # print(s)
    # pass;
    # class A:
    #     phone=100;
    #     pwd='123456'
    #
    # s = replace_args_re(s,A)
    # print(s)

    class A:
        id =100;
        token=200;
    s='{"member_id":"id","token":"token"}';
    s_1='{"member_id":100,"token":200}'
    extract_data(s,A.__class__,s_1);