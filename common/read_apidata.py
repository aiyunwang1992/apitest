# !/usr/bin/python
# -*- encoding: utf-8 -*-
# 读取测试数据
from common.readyaml import ReadYaml
from conf.projectpath import *
from common.config import Config

ip = Config().configer(http_path, 'HTTP', 'ip')


class ReadData():
    def read_data(self):
        test_datas = ReadYaml().read_yaml(test_data_path)
        for i in test_datas:
            i['url'] = ip + i['url']
        return test_datas


if __name__ == '__main__':
    r = ReadData().read_data()
    print(r)
