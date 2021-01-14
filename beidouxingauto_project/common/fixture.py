#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/2  11:18 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : fixture.py
# @Software: PyCharm
'''
#注册 登录等前置条件
from beidouxingauto_project import setting
from beidouxingauto_project.common.request_handler import send_method
from beidouxingauto_project.common.log_handler import log

def register(mobile_phone,pwd,type_=1):
    '''
    用户注册
    :param mobile_phone:
    :param pwd:
    :param type_:
    :return:
    '''
    data = {
        "mobile_phone":mobile_phone,
        "pwd":pwd,
        "type":type_
    }
    url = setting.PROJECT_URL+setting.INTERFACE['register'];# url
    headers =  setting.CUSTOMER_HEADER["v1"];
    log.info("开始注册用户:{}".format(data))
    res = send_method(url=url,method="POST",json=data,headers = headers).json();
    if res['code'] == 0:
        log.info("注册用户成功");
        return True;
    log.error("注册用户失败");
    log.error("错误信息是:{}".format(res));
    raise RuntimeError("错误信息是:{}".format(res));


def login(mobile_phone,pwd):
    '''
    用户登录
    :param mobile_phone:
    :param pwd:
    :return:
    '''
    data = {
        "mobile_phone":mobile_phone,
        "pwd":pwd
    }

    url = setting.PROJECT_URL+setting.INTERFACE["login"];
    headers =  setting.CUSTOMER_HEADER["v2"];
    log.info("该用户开始登录:{}".format(data["mobile_phone"]));
    res = send_method(url=url,method="POST",headers=headers,json=data).json();
    if res['code'] ==0:
        log.info("用户:{}登录成功".format(res['data']['id']));
        return res['data']
    log.error("用户登录失败:")
    log.error("用户登录失败原因:{}".format(res));
    raise RuntimeError("错误信息是:{}".format(res));

def recharge(member_id,amount,token):
    '''
    用户充值
    :param member_id:
    :param amount:
    :param token:
    :return:
    '''
    data ={
      "amount":amount,
      "member_id" :member_id
    };

    url =  setting.PROJECT_URL+setting.INTERFACE['recharge'];
    # headers["Authorization"] = "token";
    headers ={"Authorization":token};#token鉴权
    headers.update(setting.CUSTOMER_HEADER["v2"])
    log.info("用户:{member_id},充值:{amount}元".format(**data));
    res =  send_method(url=url,method="POST",headers=headers,json = data).json();
    if res['code'] ==0:
        log.info("用户:{}充值成功".format(res['data']['id']))
        return res['data'];
    else:
        log.error("用户充值失败:{}".format(res));
        raise RuntimeError("错误信息是:{}".format(res));

def add_loan(member_id,token,title="yujie专贷",amount=2000,loan_rate=12.0,loan_term=13,loan_date_type=2,bidding_days=1):
    '''
    加标接口
    :param member_id:  会员id
    :param token: token
    :param title:  加标标题
    :param amount:  加标金额
    :param loan_rate: 加标利率
    :param loan_term: 加标期限
    :param loan_date_type:借款期限类型
    :param bidding_days:竞标天数
    :return:
    '''
    data={
        "member_id": member_id,
        "title": title,
        "amount": amount,
        "loan_rate": loan_rate,
        "loan_term": loan_term,
        "loan_date_type": loan_date_type,
        "bidding_days": bidding_days
    }
    url = setting.PROJECT_URL+setting.INTERFACE["add_project"];
    #添加自定义请求头
    headers={"Authorization":"Bearer "+token}
    headers.update(setting.CUSTOMER_HEADER['v2']);
    res = send_method(url=url,method="post",json=data,headers=headers).json();
    if res['code']==0:
        log.info("该用户{}加标借款成功:金额是:{},该标的id是:{}".format(member_id,amount,res['data']['id']))
        return res;
    else:
        log.error("该用户:{}加标失败");
        raise RuntimeError("用户加标失败，错误信息是:{}".format(res));



if __name__ == '__main__':
    # register(mobile_phone="13858447643",pwd="12345678");
    lg_data = login(mobile_phone="13858447643",pwd="12345678")
    print(lg_data['token_info']['token']);
    res = recharge(member_id=lg_data['id'],amount=10000,token=lg_data['token_info']['token']);
    print(res);