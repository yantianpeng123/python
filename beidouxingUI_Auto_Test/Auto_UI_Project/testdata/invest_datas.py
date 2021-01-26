#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/24  6:47 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : invest_datas.py
# @Software: PyCharm
'''
#投标的测试用例

invest_data_fail= [
    {
        'title':'投资金额为0',
        'request_data':{"amount":0},
        'check_data':{"method":"get_pop_error_tip","value":"请正确填写投标金额"}
    },
    {
        'title':'投资金额为负数',
        'request_data':{"amount":-100},
        'check_data':{"method":"get_pop_error_tip","value":"请正确填写投标金额"}
    },
    {
        'title':'投资金额为空',
        'request_data':{"amount":' '},
        'check_data':{"method":"get_pop_error_tip","value":"请正确填写投标金额"}
    },
    {
        'title':'投资金额大于标剩余金额',
        'request_data':{"amount":900000000},
        'check_data':{"method":"get_pop_error_tip","value":"购买标的金额不能大于标总金额"}
    },
    {
        'title':'投资金额大于标剩余金额',
        'request_data':{"amount":80000},
        'check_data':{"method":"get_pop_error_tip","value":"购买标的金额不能大于标剩余金额"}
    }
]

success_invest_data = [
    {
     'title':'投资100成功',
     'request_data':{"amount":100},
      'check_data':{"method":"get_pop_success_tip","value":True}
    },
    {
      'title':'投资200成功',
      'request_data':{"amount":200},
      'check_data':{"method":"get_pop_success_tip","value":True}
    },
    {
      'title':'投资500成功',
      'request_data':{"amount":500},
      'check_data':{"method":"get_pop_success_tip","value":True}
    }
]

fail_invest_notIsten=[
    {
        'title':'不是10的整数倍',
        'request_data':{"amount":11},
        'check_data':{"method":"get_error_tip_notIs","value":"请输入10的整数倍"}
    },
    {
        'title':'投标金额为非数字',
        'request_data':{"amount":"qwe"},
        'check_data':{"method":"get_error_tip_notIs","value":"请输入10的整数倍"}
    }
]