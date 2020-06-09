#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 9:55
# @Author  : suoer
# @File    : http_requests.py
# @Software: PyCharm

import requests
from common.loger import Log
from common.decorators import singleton
@singleton
class Requests():
    '''用于发起http请求'''
    log=Log()
    def httprequest(self,url,params,method,header=None):
        re=requests
        if method.upper()=='GET':
            try:
                result=re.get(url,params,headers=header,timeout=1.5)
                self.log.info(f'{url}的请求结果为{result}')
            except Exception as e:
                self.log.debug(f'请求出错,错误为：{e}')
                raise e
        elif method.upper()=='POST':
            try:
                result = re.post(url, params, headers=header,timeout=1.5)
                self.log.info(f'{url}的请求结果为{result}')
            except Exception as e:
                self.log.debug(f'请求出错,错误为：{e}')
                raise e
        else:
            result=f'参数错误{method}'
            self.log.debug(result)
        return result


