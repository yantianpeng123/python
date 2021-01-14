#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/1  8:21 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
'''
#登录测试用例
import json
from beidouxingauto_project.common.base_test_case import BaseTestCase
from ddt import ddt,data #倒入ddt模块


@ddt()
class Test_Login(BaseTestCase):

    name = "登录接口"

    cases_json =  BaseTestCase.loads_case('login'); #读取数据
    @data(*cases_json)
    def test_login(self,case):
        #1.测试数据
        request_data =  json.loads(case['request_data']);
        expect_data  = json.loads(case['expect_data']);
        #2.测试步骤
        base_url = self.setting.PROJECT_URL+self.setting.INTERFACE[case['interface']];
        method =  case['method'];
        rel_data =self.send_request(url=base_url,method=method,json=request_data).json();
        #3.断言
        try:
            self.assertEqual(rel_data['code'],expect_data['code']);
            self.assertEqual(rel_data['msg'],expect_data['msg']);
        except Exception as e:
            self.logger.warning("{}:测试失败".format(case['title']));
            self.logger.warning("测试数据是:{}".format(request_data));
            self.logger.warning("测试结果是:{}".format(rel_data));
            self.logger.warning("期望结果是:{}".format(expect_data));
            raise e;


# if __name__ == '__main__':
#     unittest.main()