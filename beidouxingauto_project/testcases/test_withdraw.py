#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/2  3:45 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_withdraw.py
# @Software: PyCharm
'''
from ddt import ddt,data
import unittest;
from decimal import Decimal
from beidouxingauto_project.common.base_test_case import BaseTestCase
from beidouxingauto_project.common.fixture import register,login,recharge;
from beidouxingauto_project.common.test_data_handler import replace_args;
from beidouxingauto_project import setting
import json

@ddt()
class TestWithdraw(BaseTestCase):
    name = "提现接口";
    auth_key = "v2";
    case_json = BaseTestCase.loads_case("withdraw");#加载测试数据
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass();
        #1.注册
        sql_template = "select * from member where mobile_phone ='{}'";
        phone = cls.get_no_use_phone(sql_templeta=sql_template);
        cls.logger.info("生成的手机号是:{}".format(phone))
        register(mobile_phone=phone,pwd="12345678",type_=1);
        #2.登录
        res = login(mobile_phone=phone,pwd="12345678");
        cls.member_id = res['id'];
        cls.token =  res['token_info']['token'];
        #3.充值
        recharge(member_id=cls.member_id,amount=500000,token=cls.token);
        recharge(member_id=cls.member_id, amount=100000, token=cls.token);

    @data(*case_json)
    def test_withdraw(self,case):
        self.logger.info("===开始测试{}===".format(case['title']));
        #1.测试数据
        #1.1参数替换
        case['request_data'] = replace_args(case['request_data'],member_id = self.member_id);
        request_data =  json.loads(case['request_data']);
        expect_data = json.loads(case['expect_data']);
        if case['sql']:
            #查询提现之前的余额
            sql ="select leave_amount from member where id={}".format(self.member_id);
            #提现之前的余额
            before_leave_amount = self.db.select_one_data(sql=sql)['leave_amount'];
            self.logger.info("查询提前之前的余额的sql是:{}".format(sql));
            self.logger.info("用户{}提现之前的余额是:{}".format(self.member_id,before_leave_amount));
        #2.测试步骤
        base_url = setting.PROJECT_URL+setting.INTERFACE[case['interface']];
        method =  case['method'];
        headers = {"Authorization":"Bearer "+self.token};
        rel_data =self.send_request(url=base_url,json=request_data,method=method,headers= headers).json();
        #3.断言
        try:
            self.assertEqual(rel_data['code'],expect_data['code']);
            self.assertEqual(rel_data['msg'],expect_data['msg']);
            self.logger.info("===测试{}结束====".format(case['title']));
        except Exception as e:
            self.logger.exception("{}:测试失败".format(case['title']));
            self.logger.warning("请求的数据是:{}".format(request_data));
            self.logger.warning("期望的数据是:{}".format(expect_data));
            self.logger.warning("实际的数据是:{}".format(rel_data));
            raise e;
        if case['sql']:
            #查询提现之后的余额;
            after_leave_amount =  self.db.select_one_data(sql=sql);
            self.logger.info("用户{}提现之前的余额是:{}".format(self.member_id,after_leave_amount));
            try:
                #提现的金额
                withdraw_amount = Decimal(str(request_data['amount']));
                #提现之前的余额减去提现的金额等于提现之后的余额
                leave_money =  (before_leave_amount-withdraw_amount);
                self.assertEqual(leave_money,after_leave_amount['leave_amount']);
                # 接口返回的余额和当前数据库余额是否一直
                self.assertEqual(after_leave_amount['leave_amount'],Decimal(str(rel_data['data']['leave_amount'])));
                #是否生成了流水账单;
                self.logger.info("===校验是否生成流水账单=======")
                sql = "select id from financeLog where pay_member_id={} and amount={} " \
                      "and pay_member_money ={} ".format(self.member_id,withdraw_amount,leave_money);
                self.logger.info("生成流水账单的sql是:{}".format(sql));
                self.assertTrue(self.db.Isexist(sql=sql))
                self.logger.info("=====流水账单生成成功=======");
            except Exception as e:
                self.logger.exception("{}-->>数据库校验异常".format(e));
                self.logger.warning("数据库校验失败")

if __name__ == '__main__':
    unittest.main()