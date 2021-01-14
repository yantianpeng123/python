#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/4  8:59 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_audit_project.py
# @Software: PyCharm
'''
#测试审核项目
from beidouxingauto_project.common.base_test_case import BaseTestCase;
from beidouxingauto_project.common.fixture import register,login,add_loan
from beidouxingauto_project.common.test_data_handler import replace_args;
from beidouxingauto_project import setting
from ddt import ddt,data
import json
import unittest

@ddt()
class TestAuditProject(BaseTestCase):
    name = "审核项目接口";
    auth_key = "v2";
    case_json = BaseTestCase().loads_case("audit_project");#加载数据

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass();
        #生成没有被注册手机号
        sql="select * from member where mobile_phone ='{}'";
        pwd="12345678"
        phone = cls.get_no_use_phone(sql_templeta=sql);
        cls.logger.info("审核项目生成的普通用户手机号是:{}".format(phone))
        #用户注册(普通用户)
        register(mobile_phone=phone,pwd=pwd,type_=1);
        #用户登录(普通用户)
        normal_res = login(mobile_phone=phone,pwd=pwd);
        cls.normal_member_id = normal_res["id"];
        cls.normale_token = normal_res["token_info"]["token"];
        #生成管理员用户
        admin_phone =  cls.get_no_use_phone(sql_templeta=sql);
        cls.logger.info("生成管理员用户的手机号是:{}".format(admin_phone));
        #注册管理员用户
        register(mobile_phone=admin_phone,pwd=pwd,type_=0);
        admin_res = login(mobile_phone=admin_phone,pwd=pwd);
        cls.amdin_member_id = admin_res["id"];
        cls.admin_token = admin_res["token_info"]["token"];

    def setUp(self) -> None:
        '''
        方法级前置，每次执行测试方法钱会执行一次
        :return:
        '''
        res = add_loan(member_id=self.normal_member_id,token=self.normale_token);
        #保存项目id
        self.loan_id = res["data"]["id"];

    @data(*case_json)
    def test_audit_project(self,case):
        self.logger.info("开始测试--->>{}<<---接口".format(case['title']));
        #1.测试数据准备
        case["request_data"] = replace_args(case["request_data"],loan_id = self.loan_id)
        request_data = json.loads(case["request_data"]);
        expect_data = json.loads(case["expect_data"]);
        #2.测试步骤
        base_url = setting.PROJECT_URL+setting.INTERFACE[case["interface"]];
        method =case["method"];
        headers = {"Authorization":"Bearer "+self.admin_token}
        rel_data = self.send_request(url=base_url,method=method,json=request_data,headers=headers).json();
        #3.断言
        try:
            self.assertEqual(rel_data['code'],expect_data['code']);
            self.assertEqual(rel_data['msg'],expect_data['msg']);
        except Exception as e:
            self.logger.exception("{}:测试失败".format(case["title"]));
            self.logger.warning("请求数据是:{}".format(request_data));
            self.logger.warning("期望结果是:{}".format(expect_data));
            self.logger.warning("实际结果是:{}".format(rel_data));
            raise e;

        if case["sql"]:
            try:
                if request_data["approved_or_not"]:
                    sql = "select * from loan where status=2 and id={} and member_id={}" \
                        .format(self.loan_id, self.normal_member_id);
                    self.assertTrue(self.db.Isexist(sql=sql));
                    self.logger.info("项目{}审核通过".format(self.loan_id));
                else:
                    sql = "select * from loan where status=5 and id={} and member_id={}" \
                        .format(self.loan_id, self.normal_member_id);
                    self.assertTrue(self.db.Isexist(sql=sql));
                    self.logger.info("项目{}审核失败".format(self.loan_id));
            except Exception as e:
                self.logger.exception("{}数据库校验失败".format(case['title']));
                raise e;



if __name__ == '__main__':
    unittest.main();