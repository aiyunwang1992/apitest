#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 20:37
# @Author  : suoer
# @File    : test_login.py
# @Software: PyCharm
import pytest
import allure
import jsonpath
from common.loger import Log
from common.replace_value import ReplaceValue
from common.save_value import SaveValue
from common.http_requests import Requests
@allure.feature("panda_api测试报告")
@pytest.mark.flyback
@pytest.mark.usefixtures('lg_params')
class Testcases():
    log=Log()
    @allure.story("登录接口")
    def test_login(self,lg_params):
        allure.dynamic.title(lg_params['title'])
        with allure.step(lg_params['title']):
            self.log.info(f'请求参数为：{lg_params}')
            #ticket替换
            lg_params=ReplaceValue(lg_params).replace_param('TICKET',SaveValue.TICKET)
            res=Requests().httprequest(lg_params['url'],eval(lg_params['param']),lg_params['method'],eval(lg_params['header'])).json()
            self.log.info(f'请求结果为:{res}')
            #保存ticket
            if jsonpath.jsonpath(res,"$..ticket") :
                SaveValue.TICKET=res['data']['ticket']
            else:
                pass
            actually_code=res['code']
            try:
                assert lg_params['excepted_code']==actually_code
            except Exception as e:
                self.log.debug(f"用例{lg_params['title']}未通过: 报错为{e}")
                raise e