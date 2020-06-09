#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 10:38
# @Author  : suoer
# @File    : read_config.py
# @Software: PyCharm
import configparser
from common.decorators import singleton
@singleton
class Config():
    def config(self,filepath,section,option):
        """
        用于读取conf的配置文件
        :param filepath: 配置文件所处路径
        :param section: 键
        :param option: 值
        :return: 返回配置文件内容
        """
        cf=configparser.ConfigParser()
        cf.read(filepath,encoding='utf-8')
        result=eval(cf.get(section,option))
        return result
