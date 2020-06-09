#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 16:52
# @Author  : suoer
# @File    : build_param.py
# @Software: PyCharm
import random
from faker import Faker
from collections import namedtuple
from common.rw_testdatas import RWTestdatas
from common.save_value import SaveValue
from conf.projectpath import *
from common.decorators import singleton
from common.logindeactor import login
@singleton
class BuildParam():
    '''用于测试数据的参数化'''
    def __init__(self):
        self.faker = Faker('zh_CN')
        self.rwdata=RWTestdatas()
        self.r=random
    def register_data(self):
        """
        注册的测试数据参数化
        :return: 注册的测试数据
        """
        testdata=self.rwdata.read_data(register_path)
        email=self.faker.email()
        phone=self.faker.phone_number()
        for i in testdata:
            i['param']=i['param'].replace('email',email)
            i['param']=i['param'].replace('PHONE',phone)
        return testdata
    def login_data(self):
        """
        从已经注册了的手机号中随机取出数据来登录
        :return: 已经参数化的登录接口的数据
        """
        testdata=self.rwdata.read_data(login_path)
        phonelist=self.rwdata.read_yaml(reginphone_path)
        phone=self.r.choice(phonelist)
        for i in testdata:
            i['param']=i['param'].replace('PHONE',phone)
        return testdata
    @login
    def identity_data(self):
        testdata=self.rwdata.read_data(identify_path)
        idcard=self.faker.ssn()
        name=self.faker.name()
        token=SaveValue.TOKEN
        for i in testdata:
            i['header']=i['header'].replace('TOKEN',token)
            i['param'] = i['param'].replace('ID', idcard)
            i['param'] = i['param'].replace('NAME', name)
        return testdata
if __name__ == '__main__':
        n=BuildParam()
        print(n.identity_data())