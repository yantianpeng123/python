#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/3  9:40 上午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_recharge.py
# @Software: PyCharm
'''
#充值接口
from beidouxingauto_project.common.base_test_case import BaseTestCase;
from beidouxingauto_project.common.fixture import login,register
from beidouxingauto_project.common.test_data_handler import replace_args
from beidouxingauto_project import setting
from ddt import ddt,data
import json
from decimal import Decimal
import unittest

@ddt()
class TestRecharge(BaseTestCase):
    name = '充值接口';
    auth_key = 'v2';
    case_json=BaseTestCase().loads_case('recharge');

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass();
        #注册
        sql="select * from member where mobile_phone ='{}'";
        phone = cls.get_no_use_phone(sql_templeta=sql);
        cls.logger.info("测试充值接口生成的手机号是:{}".format(phone));
        register(mobile_phone=phone,pwd='12345678',type_=1);
        #登录
        res =login(mobile_phone=phone,pwd="12345678");
        cls.member_id = res['id'];
        cls.token = res['token_info']['token'];
        cls.logger.info("当前用户{}登录成功".format(cls.member_id));


    @data(*case_json)
    def test_recharge(self,case):
        self.logger.info("===开始测试->>{}<<--接口=====".format(case['title']));
        #1.测试数据
        case['request_data'] =  replace_args(case['request_data'],member_id =self.member_id);
        request_data = json.loads(case['request_data']);
        expect_data = json.loads(case['expect_data']);
        if case['sql']:
            #查询充值之前的余额
            sql = "select leave_amount from member where id='{}'".format(self.member_id);
            self.logger.info("查询该用户:{}充值之前的sql是:{}".format(self.member_id, sql));
            before_leave_amount=self.db.select_one_data(sql=sql)['leave_amount'];

            self.logger.info("该用户:{}充值之前的余额是:{}".format(self.member_id,before_leave_amount));
        #2.测试步骤
        base_url =  setting.PROJECT_URL+setting.INTERFACE[case['interface']];
        method =  case['method'];
        headers = {"Authorization":"Bearer "+self.token}
        self.logger.info("该用户:{}开始充值".format(self.member_id));
        rel_data = self.send_request(url=base_url,method=method,json=request_data,headers=headers).json();

        #3.断言
        try:
            self.assertEqual(rel_data['code'],expect_data['code']);
            self.assertEqual(rel_data['msg'],expect_data['msg']);
            # self.logger.info("该用户{}充值成功，充值的金额是:{}".format(self.member_id,request_data['amount']));
        except Exception as e:
            self.logger.exception("{}:测试失败".format(case['title']));
            self.logger.warning("请求数据是:{}".format(request_data));
            self.logger.warning("期望数据是:{}".format(expect_data));
            self.logger.warning("实际结果是:{}".format(rel_data));
        if case['sql']:
            #开始校验数据库
            #查询充值之后的余额是多少
            after_leave_money = self.db.select_one_data(sql=sql)['leave_amount'];
            self.logger.info("该用户:{},充值之后的余额是:{}".format(self.member_id,after_leave_money));
            try:
                #校验金额是否一直
                #充值之前的余额加上充值的金额等于充值之后的金额
                leave_money = Decimal(str(before_leave_amount+Decimal(str(request_data['amount']))));
                self.assertEqual(after_leave_money,leave_money);
                self.logger.info("数据库校验成功,该用户{}充值成功".format(self.member_id));
            except Exception as e:
                self.logger.warning("{}:数据库校验失败".format(case['title']));
                self.logger.exception("数据库异常是:".format(e));
                raise e;
            #校验接口返回的余额和数据库返回的余额是否一直
            try:
                leave_amount =  rel_data['data']['leave_amount'];
                self.assertEqual(Decimal(str(leave_amount)),leave_money);
                self.logger.info("数据库余额和当前接口返回是一致");
            except Exception as e:
                self.logger.exception("{}:校验数据库失败".format(case['title']));
                self.logger.info("该用户{}充值之后数据库余额是:{}和接口余额是:{}返回不一致".format(self.member_id,leave_money,rel_data['leave_amount']));
                raise e;
            try:
                #校验是否生成流水账单
                self.logger.info("开始校验该用户:{}是否生成流水账单".format(self.member_id));
                sql ="select id from financelog where " \
                     "income_member_id='{}' and amount={} and income_member_money={}".\
                    format(self.member_id,Decimal(str(request_data['amount'])),leave_money);
                self.logger.info("校验该用户:{} 生成流水账单的sql是:{}".format(self.member_id,sql));
                self.assertTrue(self.db.Isexist(sql=sql));
                self.logger.info("该用户:{}生成流水账单校验通过".format(self.member_id));
                self.logger.info("该用户{}充值成功，充值的金额是:{}".format(self.member_id, request_data['amount']));
            except Exception as e:
                self.logger.warning("该用户{}生成流水账单校验失败".format(self.member_id));
                self.logger.exception("流水账单校验失败,异常是:{}".format(e));
                raise e;



if __name__ == '__main__':
    unittest.main();