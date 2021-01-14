#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/8  2:37 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_invest.py
# @Software: PyCharm
'''
#投资接口
'''
投资流程
1.注册普通用户1 账号 密码 
2.登录普通用户2 账号 密码  
3.创建项目     用户id 登录接口过来的  token登录接口过来的

4.注册普通投资用户2  账号 密码
5.登录普通投资用户2  账号 密码
6.给该普通投资用户2充值  token 用户ID 从登录接口过来


8.注册普通投资用户3     账号 密码
9.登录普通投资用户3     账号 密码
10.给该普通投资用户3充值  token 用户ID 从登录接口过来

11.注册管理员用户  账号 密码
12.登录管理员用户  账号 密码
13.审核项目   token(从登录接口过来) 项目id:从普通用户1 创建项目中过来

14.普通投资用户2投资
 
15.普通投资用户3投资


'''
from beidouxingauto_project.common.base_test_case import BaseTestCase;
from ddt import ddt,data
from beidouxingauto_project.common.test_data_handler import  replace_args_re,extract_data
from decimal import Decimal
from beidouxingauto_project.common.encrypt_handler import generator_sign
import json
from beidouxingauto_project import setting
import unittest

@ddt()
class Test_Invest_Project(BaseTestCase):

    name = "投资接口";
    auth_key = "v2";

    case_json = BaseTestCase.loads_case("invest_project");#加载数据

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass();
        #生成三个不同角色的手机号
        sql="select * from member where mobile_phone ='{}'";
        #普通用户 --创建项目
        cls.phone = cls.get_no_use_phone(sql_templeta=sql);
        cls.logger.info("该普通用户的手机号是:{}，用来创建项目".format(cls.phone));
        #普通投资用户1
        cls.invest1_phone = cls.get_no_use_phone(sql_templeta=sql);
        cls.logger.info("该普通投资用户1的手机号是:{}".format(cls.invest1_phone));
        #普通投资用户2
        cls.invest2_phone = cls.get_no_use_phone(sql_templeta=sql);
        cls.logger.info("该普通投资用户2的手机号是:{}".format(cls.invest2_phone));
        #生成管理员用户
        cls.admin_phone = cls.get_no_use_phone(sql_templeta=sql);
        cls.logger.info("该管理员用户的手机号是:{}".format(cls.admin_phone));

    @data(*case_json)
    def test_invest(self,case):
        self.logger.info("====开始测试>>{}<<接口===".format(case["title"]));
        #1.处理测试数据
        #1.1替换json字符串中的需要替换的参数
        case["request_data"] = replace_args_re(case["request_data"],self.__class__);
        #1.2反序列化字符串
        request_data = json.loads(case["request_data"]);
        expect_data =json.loads(case["expect_data"]);
        #2.测试步骤
        if case["sql"]:
            #获取投资前的金额
            sql="select leave_amount from member where id=  {}".format(request_data["member_id"]);
            before_leave_amount =self.db.select_one_data(sql=sql)["leave_amount"];
            self.logger.info("该用户投资前的金额是:{}".format(before_leave_amount));
        #发送请求
        base_url = setting.PROJECT_URL+setting.INTERFACE[case["interface"]];
        if case["headers"]:
            headers = {"Authorization": "Bearer " + getattr(self,case["headers"])};
            if self.auth_key =="v3":
                #加入时间戳和签名sign
                sign,timestamp = generator_sign(getattr(self,case["headers"]));
                request_data["sign"] = sign;
                request_data["timestamp"] =timestamp;
        else:
            headers = {};
        response = self.send_request(url=base_url,method=case["method"],json=request_data,headers=headers)
        res_text =  response.text;
        res_json = response.json();
        #3.断言
        try:
            self.assertEqual(expect_data["code"],res_json["code"]);
            self.assertEqual(expect_data["msg"],res_json["msg"]);
        except Exception as e:
            self.logger.exception("{}:测试失败".format(case["title"]));
            self.logger.warning("请求数据是:{}".format(request_data));
            self.logger.warning("期望结果是:{}".format(expect_data));
            self.logger.warning("实际结果是:{}".format(res_json));
            raise e;
        #参数提取
        if case["extract"]:
            maps = json.loads(case["extract"]);
            extract_data(maps,self.__class__,res_text);

        #数据库校验
        if case["sql"]:
            #查询投资后的余额
            sql ="select leave_amount from member where id=  {}".format(request_data["member_id"]);
            current_leave_amount = self.db.select_one_data(sql=sql)["leave_amount"];
            self.logger.info("该用户投资后的余额是:{}".format(current_leave_amount));

            try:
                #用户投资后余额变化 投资钱的余额减去投资金额等于投资后的余额
                self.assertEqual(current_leave_amount,before_leave_amount-Decimal(str(request_data["amount"])));
            except Exception as e:
                self.logger.exception("用户投资金额校验失败:{}".format(e));
                self.logger.warning("用户投资前的金额是{},用户投资金额是:{},投资后金额是:{}".
                                    format(before_leave_amount,current_leave_amount,request_data["amount"]));
                raise e;
            #2.投资记录流水生成
            sql = "select id from invest where member_id={member_id} and loan_id ={loan_id} and amount={amount} and is_valid =1"\
                .format(**request_data);
            self.logger.info("查找用户投资记录的sql是:{}".format(sql));
            try:
                self.assertTrue(self.db.Isexist(sql=sql));
                self.logger.info("该用户{},投资记录生成".format(request_data["member_id"]));
            except Exception as e:
                self.logger.exception("该用户{}投资记录生成失败:{}".format(request_data["member_id"]),e);
                raise e;
            #3.流水记录
            sql ="select * from financelog where pay_member_id = {} and amount={} and pay_member_money={}"\
                .format(request_data['member_id'],request_data["amount"],current_leave_amount);
            self.logger.info("查询流水记录是否生成的sql是:{}".format(sql));
            try:
                self.db.Isexist(sql=sql);
                self.logger.info("流水记录生成成功");
            except Exception as e:
                self.logger.exception("用户流水记录生成失败:{}".format(e));
                raise e;
            #回款记录
            #查询该项目的借款总金额
            sql ="select amount from loan where id={}".format(request_data["loan_id"]);
            loan_amount = self.db.select_one_data(sql=sql)["amount"];
            self.logger.info("查询该项目借款总金额的sql是:{}".format(sql));
            self.logger.info("该项目的借款总金额是:{}".format(loan_amount));
            #查询用户投资的金额
            sql = "select sum(amount) as total  from  invest where loan_id ={} and is_valid =1 ".format(request_data["loan_id"])
            invest_amount = self.db.select_one_data(sql=sql)["total"];
            self.logger.info("查询该项目总的投资金额的sql是:{}".format(sql));
            self.logger.info("该项目总的投资金额是:{}".format(invest_amount));
            if loan_amount==invest_amount:
                self.logger.info("该项目{}满标啦".format(request_data["loan_id"]));
                #生成回款记录
                #查询该用户的投资记录 包含投资的项目id和投资金额
                sql = "select id as invest_id, amount from  invest where loan_id ={} and is_valid =1"\
                    .format(request_data["loan_id"])
                self.logger.info("查询该用户生成的投资记录的sql是:{}".format(sql));
                data_all = self.db.select_all_data(sql=sql);
                #验证还款记录
                for item in data_all:
                    sql =  "select * from repayment where invest_id = {invest_id} and unfinished_principal={amount}".\
                        format(**item);
                    if self.db.Isexist(sql=sql):
                        self.logger.info("还款记录生成成功");
                    else:
                        self.logger.warning("还款记录生成失败");
                        raise  AssertionError("还款记录生成失败");


if __name__ == '__main__':
    unittest.main();