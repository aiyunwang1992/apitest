#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 12:23
# @Author  : suoer
# @File    : conftest.py
# @Software: PyCharm
'''测试驱动，前置后置条件'''
import pytest
from common.build_param import BuildParam
#把测试数据读取出来
#注册
register_data=BuildParam().register_data()
#登录，
login_data=BuildParam().login_data()
#身份认证
identify_data=BuildParam().identity_data()
#通过数据驱动
@pytest.fixture(params=register_data)
def reg_params(request):
    return request.param
@pytest.fixture(params=login_data)
def lg_params(request):
    return request.param
@pytest.fixture(params=identify_data)
def identify_params(request):
    return request.param


