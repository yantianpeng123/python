#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/24  12:44 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_register.py
# @Software: PyCharm
'''
#测试注册
import json
from ddt import ddt ,data
from beidouxingauto_project.common.base_test_case import BaseTestCase
from beidouxingauto_project.common.test_data_handler import replace_args

@ddt()
class TestRegister(BaseTestCase):

    name = "注册接口"

    case_json = BaseTestCase.loads_case('register');# 读取excle数据
    #测试注册功能
    @data(*case_json)
    def test_register(self,case):
        #1.测试数据(request_data,expect_data)

        if "#phone#" in case['request_data']:
            sql_template ="select * from member where mobile_phone ='{}'";
            phone = self.get_no_use_phone(sql_templeta=sql_template);  # 生成手机号码
            self.logger.info("生成的手机号码是：{}".format(phone));
            case['request_data'] = replace_args(case['request_data'],phone=phone);
        request_data = json.loads(case['request_data']);
        expect_data =  json.loads(case['expect_data']);
        if case['sql']:
            case['sql'] = case['sql'].replace('#phone#',phone);

        #2.测试步骤
        base_url =  self.setting.PROJECT_URL+self.setting.INTERFACE[case['interface']]
        method = case['method'];
        res = self.send_request(url=base_url,method=method,json=request_data)
        #3.断言
        rel_data = res.json();
        try:
            self.assertEqual(rel_data['code'], expect_data['code']);
            self.assertEqual(rel_data['msg'],expect_data['msg'])
        except Exception as e:
            # log.warning('{}:测试失败'.format(case['title']));
            # log.warning('测试数据:{}'.format(request_date));
            # log.warning('测试结果:{}'.format(rel_data));
            # log.warning('期望结果是:{}'.format(expect_data));

            self.logger.warning('{}:测试失败'.format(case['title']));
            self.logger.warning('测试数据:{}'.format(request_data));
            self.logger.warning('测试结果:{}'.format(rel_data));
            self.logger.warning('期望结果是:{}'.format(expect_data));

            raise e;
        #判断是否需要校验数据库
        if case['sql']:
            # 1.创建链接
            # 2.创建游标

            try:
                self.logger.warning('数据库校验执行的sql:{}'.format(case['sql']));
                self.assertTrue(self.db.Isexist(sql=case['sql']));
            except Exception as ex:
                self.logger.warning('{}:数据库校验失败'.format(case['title']));
                self.logger.warning('数据库校验执行的sql:{}'.format(case['sql']));
                raise ex;





# if __name__ == '__main__':
#     unittest.main();