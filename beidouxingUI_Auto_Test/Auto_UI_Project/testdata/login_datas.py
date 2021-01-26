#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  8:16 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : login_datas.py
# @Software: PyCharm
'''
#测试用例
#正向用例
success_datas =[
    {
        'title':'登录成功',
        'request_data':{"username":"18684720553","password":"python"},
        'check_data':{"method":"is_login","value":True}
    }
];

#反向用例
fail_datas=[
    #手机号为空
    {
        'titile':'手机号为空',
        'request_data':{"username":"","password":"python"},
        'check_data':{"method":"get_error_tip","value":"请输入手机号"}
    },
    #手机号为10
    {
        'titile': '手机号为10位',
        'request_data': {"username": "1868472055", "password": "python"},
        'check_data': {"method": "get_error_tip", "value": "请输入正确的手机号"}
    },
    #手机号大于11位
    {
        'titile': '手机号大于11位',
        'request_data': {"username": "186847205534", "password": "python"},
        'check_data': {"method": "get_error_tip", "value": "请输入正确的手机号"}
    },
    #手机号为非数字
    {
        'titile': '手机号大于11位',
        'request_data': {"username": "qwertyuiop", "password": "python"},
        'check_data': {"method": "get_error_tip", "value": "请输入正确的手机号"}
    },
    #密码为空 密码长度没有做校验 因此在次不测试密码长度
    {
        'title':'密码为空',
        'request_data':{"username":"18684720553","password":""},
        'check_data':{"method": "get_error_tip", "value": "请输入密码"}
    },
    #正确的手机号，错误的密码
    # {
    #     'title': '正确的手机号，错误的密码',
    #     'request_data': {"username": "18684720553", "password": "pyth"},
    #     'check_data': {"method": "get_error_tip", "value": True}
    # },
    # #正确的密码，错误的手机号
    # {
    #     'title': '正确的密码，错误的手机号',
    #     'request_data': {"username": "18684720", "password": "python"},
    #     'check_data': {"method": "get_error_tip", "value": True}
    # }
];