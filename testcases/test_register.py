#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 12:24
# @Author  : suoer
# @File    : test_register.py
# @Software: PyCharm
'''注册的用例'''
import pytest
import allure
from common.loger import Log
from common.save_value import SaveValue
from common.rw_testdatas import RWTestdatas
from common.http_requests import Requests
from conf.projectpath import *
@allure.feature("panda_api测试报告")
@pytest.mark.flyback
@pytest.mark.usefixtures('reg_params')
class TestCase():
    log=Log()
    @allure.story("注册接口")
    def test_register(self,reg_params):
        with allure.step(reg_params['title']):
            self.log.info(f'请求参数为 ：{reg_params}')
            res=Requests().httprequest(reg_params['url'],eval(reg_params['param']),reg_params['method'],eval(reg_params['header'])).json()
            self.log.info(f'请求结果为：{res}')
            actually_code=res['code']
            try:
                assert reg_params['excepted_code']==actually_code
                if reg_params['module']=='register':
                    SaveValue.PHONE.append(eval(reg_params['param'])['regName'])
                    RWTestdatas().write_data(SaveValue.PHONE,reginphone_path)
            except Exception as e:
                self.log.debug(f"未通过的用例为：{reg_params['title']}")
                raise e