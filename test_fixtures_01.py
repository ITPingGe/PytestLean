#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 功能函数
def multiply(a, b):
    return a * b

# Fixture
def setup_module(module):
    print("所有用例执行之前初始化")

def teardown_module(module):
    print("所有用例执行之后初始化")

def setup_function(function):
    print("每个测试函数之前初始化")

def teardown_function(function):
    print("每个测试函数之后初始化")

def setup():
    print("运行在调用方法前")

def teardown():
    print("运行在调用方法后")

# 测试用例
def test_multiply_3_4():
    print('test_multiply_3_4')
    assert multiply(3, 4) == 12

def test_multiply_a_3():
    print('test_strings_a_3')
    assert multiply('a', 3) == 'aaa'