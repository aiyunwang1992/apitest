# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 发起http请求的类
import requests, time
from common.loger import Log

log = Log()


class Request():
    def httprequest(self, url, param, method, header=None):
        # 先判断是要发起get请求，还是post请求
        if method.upper() == 'GET':
            try:
                # 发起get请求
                result = requests.get(url, param, headers=header).json()
                log.info('请求成功，请求结果为{0}'.format(result))
            except Exception as e:
                # 如果请求报错，就将异常抛出来
                log.error('发起get请求报错！错误是{0}'.format(e))
                raise e
        elif method.upper() == 'POST':
            try:
                # 发起post请求
                result = requests.post(url, param, headers=header).json()
                log.info('请求成功，请求结果为{0}'.format(result))
            except Exception as e:
                # 如果请求报错，就将异常抛出来
                log.error('发起的post请求报错！错误是{0}'.format(e))
                raise e
        else:
            log.error('输入无效请求:{0}'.format(method))
            result = 'Error：输入请求无效{0}'.format(method)
        return result


if __name__ == '__main__':
    header = {
        'token': 'BCACCOUNT_LOGIN_eee1ad0a458a1fa77e6b9fc0f973c34b_C38DEDD0138A439E95BBB8F54FBC57F6',
        'language': 'zh-CN',
        'Content-Type': 'application/x-www-form-urlencoded'}

    ip = 'http://stg.panda.co'
    param = {'symbolId': 'BTC-PERP-REV', 'side': 'SELL_OPEN',
             'orderType': 'LIMIT', 'price': '6235.4',
             'priceType': 'INPUT', 'quantity': '1',
             'leverage': '100', 'planOrderType': 'STOP_COMMON', 'triggerPrice': ''}
    url = ip + '/api/futures/order/create'
    method = 'post'
    re = Request().httprequest(url, param, method, header=header)

    print(re)
