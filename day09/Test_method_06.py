#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
# @Time    : 2020/11/15  4:08 下午
# @Author  : yantianpeng
# @Site    : 
# @File    : Test_method_06.py
# @Software: PyCharm
'''
#多态
#python 是一门解释性语言，动态语言，不存在多态的问题
class Animal:
    def bark(self):
        print("嗷嗷叫");

class Dog(Animal):
    def bark(self):
        print("汪汪叫");

class Cat(Animal):
    def bark(self):
        print("喵喵叫");

class Duck(Animal):
    def bark(self):
        print("嘎嘎叫");


def bark(animal):
    animal.bark();

dog = Dog();
cat = Cat();
duck = Duck();

bark(dog);
bark(cat);
bark(duck);
