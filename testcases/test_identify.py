#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 19:44
# @Author  : suoer
# @File    : test_identify.py
# @Software: PyCharm
import pytest
import allure
from common.loger import Log
from common.http_requests import Requests
@allure.feature("panda_api测试报告")
@pytest.mark.flyback
@pytest.mark.usefixtures('identify_params')
class TestCases():
    log=Log()
    @allure.story("身份认证接口")
    def test_identify(self,identify_params):
        with allure.step(identify_params["title"]):
            self.log.info(f'请求的参数为：{identify_params}')
            re=Requests().httprequest(identify_params['url'],eval(identify_params['param']),identify_params['method'],eval(identify_params['header'])).json()
            self.log.info(f'返回参数为：{re}')
            actually_code=re['code']
            try:
                identify_params['excepted_code']==actually_code
            except Exception as e:
                self.log.debug(f"未通过的用例为{identify_params['title']}")
                raise e