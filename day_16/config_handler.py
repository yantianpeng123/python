#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/12/21  6:20 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : config_handler.py
# @Software: PyCharm
'''
import yaml
from configparser import ConfigParser;

class Config:

    def __init__(self,filename,encoding='utf-8',type_=None):
        self.filename =  filename;
        self.encoding = encoding;
        if type_:
            self.type_ = type_;
        else:
            if self.filename.split('.')[-1] not in ['conf','yaml','cnf','ini']:
                raise ValueError("你传入的配置文件有错误");
            else:
                self.type_ = self.filename.split('.')[-1];

    def parse(self):
        if self.type_ =='yaml':
           return self._parse_yaml();
        else:
            return self._pasr_ini()



    def _pasr_ini(self):
       conf =  ConfigParser();
       conf.read(self.filename,encoding=self.encoding);
       return conf;

    #_表示私有方法 只可以内部调用
    def _parse_yaml(self):
        with open(file=self.filename,mode='r',encoding=self.encoding) as f:
          return  yaml.load(f,yaml.FullLoader);




if __name__ == '__main__':
    data = Config('config.ini').parse();
    print(data['log']['file']);
    yaml_01 =  Config('config.yaml').parse();
    print(yaml_01);