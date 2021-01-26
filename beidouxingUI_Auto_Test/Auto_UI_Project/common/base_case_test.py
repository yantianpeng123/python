#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2021/1/22  7:44 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : base_case_test.py
# @Software: PyCharm
'''
from beidouxingUI_Auto_Test.Auto_UI_Project.common.login_handler import log
from beidouxingUI_Auto_Test.Auto_UI_Project import setting
class BaseCase:
    """
    测试用例基类
    """
    #功能模块
    name =None;
    log =log;
    setting =setting;

    @classmethod
    def setup_class(cls):
        cls.log.info("===>>>{}:测试开始<<<====".format(cls.name));

    @classmethod
    def teardown_class(cls):
        cls.log.info("====>>>{}:测试结束<<======".format(cls.name));

    def beidouxing_assert(self, check_data,msg='XX功能'):
        """
        自定义登录断言
        :param check_data:
        :return:
        """
        method = getattr(self, check_data['method']);
        res =  method();
        try:
           self.assert_equal(res,check_data['value'],msg);
        except Exception as e:
            self.log.exception("{}:断言失败".format(msg));
            self.log.warning("测试函数返回的实际结果是:{}".format(res));
            self.log.warning("期望结果是:{}".format(check_data['value']));
            raise e;
        else:
            self.log.info("{}:断言成功".format(msg))


    def assert_equal(self,first,second,msg=''):
        if first !=second:
            if msg:
                raise AssertionError(msg);
            else:
                raise AssertionError('{}!={}'.format(first,second));
