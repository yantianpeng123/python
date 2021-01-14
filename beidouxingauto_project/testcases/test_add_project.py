#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/3  7:00 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_add_project.py
# @Software: PyCharm
'''
#测试加标接口
from beidouxingauto_project.common.base_test_case import BaseTestCase
from beidouxingauto_project.common.fixture import register,login;
from beidouxingauto_project.common.test_data_handler import get_phone,replace_args;
from beidouxingauto_project import setting
import json
from ddt import ddt,data;
import unittest

@ddt()
class TestAddProject(BaseTestCase):
    name = "加标接口"
    auth_key = "v2";
    case_json =  BaseTestCase().loads_case("add_project");

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass();
        #1.注册
        sql="select * from member where mobile_phone ='{}'";
        phone = cls.get_no_use_phone(sql_templeta=sql);
        register(mobile_phone=phone,pwd="12345678",type_=1);
        cls.logger.info("加标接口生成的手机号是:{}".format(phone))
        #2.登录
        res = login(mobile_phone=phone,pwd="12345678");
        cls.member_id = res["id"];
        cls.token = res["token_info"]["token"];
        cls.logger.info("该用户是:{},登录成功".format(cls.member_id));

    @data(*case_json)
    def test_add_project(self,case):
        self.logger.info("开始测试-->>{}<<--接口".format(case['title']));
        #1.测试数据
        case["request_data"] = replace_args(case['request_data'],member_id = self.member_id);
        request_data = json.loads(case['request_data']);
        expect_data = json.loads(case['expect_data']);
        #2.测试步骤
        base_url =setting.PROJECT_URL+setting.INTERFACE["add_project"];
        method = case["method"];
        headers = {"Authorization":"Bearer "+self.token};
        rel_data =self.send_request(url=base_url,method=method,json=request_data,headers=headers).json();

        #3.断言
        try:
            self.assertEqual(rel_data['code'],expect_data['code']);
            self.assertEqual(rel_data['msg'],expect_data['msg']);
        except Exception as e:
            self.logger.warning("该用户->{}<-加标失败".format(self.member_id))
            self.logger.exception("用户加标失败:{}".format(e));
            self.logger.warning("测试数据是:{}".format(request_data));
            self.logger.warning("期望数据是:{}".format(expect_data));
            self.logger.warning("实际数据是:{}".format(rel_data));
            raise e;
        if case['sql']:
            try:
                # 校验数据库loan表是否新增一条加标数据
                sql = "select id from loan where member_id={} " \
                      "and amount={} and title='{}' and loan_date_type={}". \
                    format(self.member_id, request_data['amount'], request_data['title'],
                           request_data['loan_date_type']);
                self.logger.info("查询用户:{}加标的sql是:{}".format(self.member_id, sql));
                self.assertTrue(self.db.Isexist(sql=sql));
                self.logger.info("该用户:{}加标成功".format(self.member_id));
            except Exception as e:
                self.logger.warning("{}-->>数据库校验失败".format(case['title']));
                self.logger.exception("数据库异常:{}".format(e));
                raise e;


# if __name__ == '__main__':
#     unittest.main();