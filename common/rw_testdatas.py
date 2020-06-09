#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 10:36
# @Author  : suoer
# @File    : rw_testdatas.py
# @Software: PyCharm
from ruamel import yaml
from common.read_config import Config
from common.decorators import singleton
from conf.projectpath import *
@singleton
class RWTestdatas():
    def __init__(self):
        self.ip=Config().config(httpconf_path,'HTTP','ip')
    def read_yaml(self,filepath):
        """
        读取yaml文件的数据
        :param filepath: 文件的路径
        :return: 读取的数据
        """
        with open(filepath,encoding='utf-8') as file:
            data=yaml.load(file.read(),Loader=yaml.Loader)
        return data
    def read_data(self,filepath):
        """
        读取测试数据
        :param filepath: 测试数据的路劲
        :return: 读取的测试数据
        """
        with open(filepath,encoding='utf-8') as file:
            data=yaml.load(file.read(),Loader=yaml.Loader)
        for i in data:
            i['url']=self.ip+i['url']
        return data
    def write_data(self,data,filepath):
        with open(filepath,'a',encoding='utf-8') as file:
            yaml.dump(data,file,Dumper=yaml.RoundTripDumper)
if __name__ == '__main__':
    # r=RWTestdatas()
    # r.write_data(reginphone_path)
    with open(reginphone_path, encoding='utf-8') as file:
        data = yaml.load(file.read(), Loader=yaml.Loader)
        print(data)