#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 17:03
# @Author  : suoer
# @File    : logindeactor.py
# @Software: PyCharm
import random
import jsonpath
from functools import wraps
from common.loger import Log
from common.http_requests import Requests
from common.read_config import Config
from common.rw_testdatas import RWTestdatas
from common.save_value import SaveValue
from conf.projectpath import httpconf_path,reginphone_path
from functools import partial
def login(func):
    '''实现前置登录获取token'''
    @wraps(func)
    def warpper(*args,**kwargs):
        if not SaveValue.TOKEN:
            header = {'language': 'zh_CN', 'Content-Type': 'application/x-www-form-urlencoded'}
            method = 'post'
            re = Requests()
            request = partial(re.httprequest, method=method, header=header)
            ip = Config().config(httpconf_path, 'HTTP', 'ip')
            log=Log()
            lgname_list=RWTestdatas().read_yaml(reginphone_path)
            lgname=random.choice(lgname_list)
            lg_param= {
                'loginName': lgname, 'password': '123456Abc',
                'csessionid': '1', 'sig': '1',
                'token': '1', 'platform': '1'}
            #调登录接口生成ticket
            lg_url=ip+'/api/v1/user/login'
            try:
                lg_re=request(lg_url,lg_param).json()
                log.info(f'前置登录的请求结果为{lg_re}')
            except Exception as e:
                log.error(f'前置登录请求报错：{e}')
                raise e
            ticket=jsonpath.jsonpath(lg_re,'$..ticket')[0]
            sms_url=ip+'/api/v1/user/sendSms'
            sms_param={
                'type':'127','msgtype':'1',
                'areaCode':'86','phone':'1',
                'csessionid':'1','sig':'1',
                'token':'1','ticket':ticket}
            #发送短信验证码
            try:
                sms_re=request(sms_url,sms_param).json()
                log.info(f'前置发送短信接口请求结果为：{sms_re}')
            except Exception as e:
                log.error(f'前置发送短信接口报错为：{e}')
                raise e
            token_url=ip+'/api/v1/user/getLoginToken'
            token_param={'code':'123456','ticket': ticket}
            try:
                token_re = request(token_url, token_param).json()
                log.info(f'前置生成token的请求结果为：{token_re}')
            except Exception as e:
                log.error(f'前置生成token的请求报错为：{e}')
                raise e
            token=jsonpath.jsonpath(token_re,'$..data')[0]
            SaveValue.TOKEN=token
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return warpper