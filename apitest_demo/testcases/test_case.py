# !/usr/bin/python
# -*- encoding: utf-8 -*-
import pytest#, allure
from common.regular_pick import Regular
from common.save_value import SaveValue
from common.http_request import Request
from common.loger import Log

log = Log()
reg = Regular()


#@allure.feature('panda的接口测试报告')
@pytest.mark.flyback
@pytest.mark.usefixture('parm')
class TestCases():
    def test_case(self, param):
        # 发起请求
        log.info('请求参数为：{0}'.format(param))
        re = Request().httprequest(param['url'], eval(param['param']), param['method'], eval(param['header']))
        log.info('请求结果为：{0}'.format(re))
        actually_code = re['code']
        try:
            assert param['excepted_code'] == actually_code
        except Exception as e:
            log.debug('未通过用例为:{0}；未通过原因为：{1}'.format(param['title'], re))
            raise e
