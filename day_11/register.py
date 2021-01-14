#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/20  2:53 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : register.py
# @Software: PyCharm
'''


#用户注册模块
class Register():
        #模拟已经注册的用户
        users = [{'user':'python34','password':'123456'}];
        def __init__(self,username,password1,password2):
            self.username= username;
            self.password1 =  password1;
            self.password2 = password2;

        def register(self):
            if not all([self.username,self.password1,self.password2]):
                return {'code':0,'msg':'所有参数不能为空'};
            for user in self.users:
                if self.username == user['user']:
                    return {'code':0,'msg':'该账户已经存在'};
                else:
                    if self.password1 !=self.password2:
                        return {'code':0,'msg':'两次密码不一致'};
                    else:
                        if 6<=len(self.username)<=18  and 6<=len(self.password1)<=18:
                            self.users.append({'user':self.username,'password':self.password1});
                            return {'code':1,'msg':'注册成功'};
                        else:
                            return {'code':0,'msg':'账号和密码必须在6-18位之间'};





if __name__ == '__main__':
    msg = Register('python34','127','127').register();
    print(msg);
