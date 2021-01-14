#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/10  4:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : encrypt_handler.py
# @Software: PyCharm
'''

import rsa
import base64
from time import time
import requests
import json
#非对称加密

def rsa_encry(msg):
    #公钥
    server_pub_key = """
    -----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
    O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
    tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
    kKlZFc8Br7SHtbL2tQIDAQAB
    -----END PUBLIC KEY-----
    """

    #生成公钥字节
    pub_key_byte = server_pub_key.encode("utf-8");
    #生成公钥对象
    pub_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_byte);
    #要加密的自己对象
    content = msg.encode("utf-8");

    #加密，返回文本
    crypt_msg = rsa.encrypt(content,pub_key_obj);
    #base64编码
    cipher_base64 = base64.b64encode(crypt_msg);

    return cipher_base64.decode(); #解码成字符串


def generator_sign(token):

    #取值tokan前50位
    toekn_50 = token[:50];

    #获取当前时间戳
    timestamp = int(time());

    #拼接token和时间
    msg =  toekn_50+str(timestamp);

    sign = rsa_encry(msg=msg);
    return sign,timestamp;


# if __name__ == '__main__':
#     base_url = "http://api.lemonban.com/futureloan";
#     #测试项目充值接口
#     user = {"mobile_phone":"13117787132","pwd":"12345678"};
#     login_url = base_url+"/member/login"
#     headers ={
#         "X-Lemonban-Media-Type":"lemonban.v3"
#     };
#     login_res = requests.post(url=login_url,json=user,headers=headers).json()["data"];
#     member_id = login_res["id"];
#     token= login_res["token_info"]["token"]
#     print("=====用户登录成功=====");
#     #获取签名和时间戳
#     sign,timestamp = generator_sign(token=token)
#     print("签名为： ", sign, "\n时间戳为： ", timestamp)
#
#     #用户充值
#     headers["Authorization"] = "Bearer {}".format(token);
#     recharge_url = base_url+"/member/recharge";
#     # recharge_data ={"member_id": member_id,"amount": 3000,"timestamp": timestamp,"sign": sign};
#     recharge_data = {"member_id": member_id, "amount": 2000, "sign": sign, "timestamp": timestamp}
#     print(recharge_data)
#     recharge = requests.post(url=recharge_url,json=recharge_data,headers=headers).json();
#     print(recharge);